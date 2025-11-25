from rest_framework.serializers import ModelSerializer
from posts.models import Post, Comment
from posts.validators import validate_author_age, validate_title_no_bad_words


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ('owner', 'created_at', 'updated_at')

    def validate(self, attrs):
        """
        Общая валидация, проверяющая и возраст автора, и запрещенные слова в заголовке
        """
        attrs = super().validate(attrs)

        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validate_author_age(request.user)

        title = attrs.get('title')
        if title:
            validate_title_no_bad_words(title)

        return attrs


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('owner', 'created_at', 'updated_at')