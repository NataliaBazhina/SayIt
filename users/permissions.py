from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """Проверка, что пользователь состоит в группе администраторов"""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Admins").exists()


class IsOwner(permissions.BasePermission):
    """Проверка, что пользователь является владельцем объекта"""
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class CanEditUser(permissions.BasePermission):
    """Разрешает редактирование: пользователь может редактировать только СЕБЯ"""

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj == request.user


class CanDeleteUser(permissions.BasePermission):
    """Разрешает удаление: только админ"""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="Admins").exists()