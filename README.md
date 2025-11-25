# SayIt 

Платформа для блогов, с возможностью писать посты, комментарии и управлять пользователями.

## Функциональность

- Создание и управление постами и комментариями
- Кастомная модель пользователя  
- Разграничение прав доступа
- Валидация пароля и почты
- Валидация возраста автора (18+)
- Фильтрация запрещенных слов в заголовках
- Админ-панель с фильтром по дате создания постов и ссылками на авторов

## Технологии

- Django 5.2
- Django REST Framework
- PostgreSQL/SQLite

## Установка

1. Клонируйте репозиторий: 
git@github.com:NataliaBazhina/SayIt.git
2. Создайте виртуальное окружение: 

python -m venv venv

source venv/bin/activate  # Linux/Mac

venv\Scripts\activate  # Windows 
3. Установите зависимости: `pip install -r requirements.txt`
4. Примените миграции: `python manage.py migrate`
5. Запустите сервер: `python manage.py runserver`