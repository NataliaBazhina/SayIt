from rest_framework import serializers
from users.models import User
from users.validators import validate_password, validate_email_domain


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "login",
            "password",
            "phone",
            "birth_date",
            "created_at",
            "updated_at",
            "is_superuser",
            "is_staff",
            "is_active",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "is_superuser",
            "is_staff",
            "is_active"
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):
        validate_password(value)
        return value


    def validate_login(self, value):
        validate_email_domain(value)
        return value