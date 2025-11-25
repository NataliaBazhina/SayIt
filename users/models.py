from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    login = models.EmailField(
        unique=True, verbose_name="логин", help_text="Введите вашу почту"
    )

    phone = models.CharField(
        max_length=35,
        verbose_name="телефон",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    birth_date = models.DateField(
        verbose_name="Дата рождения",
        help_text="Введите дату рождения",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")

    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.login
