from rest_framework.exceptions import ValidationError
from datetime import date


def validate_author_age(user):
    """
    Валидатор возраста автора: должен быть не менее 18 лет
    """
    today = date.today()
    age = today.year - user.birth_date.year

    if today.month < user.birth_date.month or (
            today.month == user.birth_date.month and today.day < user.birth_date.day):
        age -= 1

    if age < 18:
        raise ValidationError("Автор поста должен быть старше 18 лет.")


def validate_title_no_bad_words(value):
    """
    Валидатор заголовка: проверяет отсутствие запрещенных слов
    """
    forbidden_words = ['ерунда', 'глупость', 'чепуха']
    title_lower = value.lower()
    found_words = []
    for word in forbidden_words:
        if word in title_lower:
            found_words.append(word)

    if found_words:
        raise ValidationError(f"Заголовок содержит запрещенные слова: {', '.join(found_words)}")