from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer
from users.permissions import IsOwner
from posts.validators import validate_author_age


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (IsAuthenticated,)
        elif self.action in ["update", "partial_update"]:
            self.permission_classes = (IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (IsOwner,)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (IsAuthenticated,)
        elif self.action in ["update", "partial_update"]:
            self.permission_classes = (IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (IsOwner,)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)