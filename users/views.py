from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import User
from users.serializers import UserSerializer
from users.permissions import IsAdmin, IsOwner, CanEditUser, CanDeleteUser


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (AllowAny,)
        elif self.action == "list":
            self.permission_classes = (IsAdmin | IsAuthenticated,)
        elif self.action == "retrieve":
            self.permission_classes = (IsAdmin | IsOwner,)
        elif self.action in ["update", "partial_update"]:
            self.permission_classes = (CanEditUser,)
        elif self.action == "destroy":
            self.permission_classes = (CanDeleteUser,)
        return super().get_permissions()



    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

