from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner_link', 'created_at', 'updated_at']
    list_filter = ['created_at', 'owner']

    def owner_link(self, obj):
        url = reverse('admin:users_user_change', args=[obj.owner.id])
        return format_html('<a href="{}">{}</a>', url, obj.owner.login)

    owner_link.short_description = 'Автор'