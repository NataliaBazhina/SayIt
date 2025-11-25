from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


def validate_password(value):
    """
    Валидатор пароля:
    - минимум 8 символов
    - хотя бы одна цифра
    """
    if len(value) < 8:
        raise ValidationError(
            _("Пароль должен содержать минимум 8 символов."),
            code='password_too_short',
        )

    if not any(char.isdigit() for char in value):
        raise ValidationError(
            _("Пароль должен содержать хотя бы одну цифру."),
            code='password_no_digit',
        )


def validate_email_domain(value):
    """
    Валидатор почты: разрешены только mail.ru и yandex.ru
    """
    allowed_domains = ['mail.ru', 'yandex.ru']
    domain = value.split('@')[-1]

    if domain not in allowed_domains:
        raise ValidationError(
            f"Разрешены только почтовые домены: {', '.join(allowed_domains)}"
        )