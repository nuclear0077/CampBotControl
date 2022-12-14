## CampBotControl

## About
Управление для camp бота образовательно платформы.
Реализовано наполнение базы данных через веб интерфейс и API для получения информацию из базы данных.


## Documentation

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/nuclear0077/CampBotControl.git
```

```
cd CampBotControl
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Создать файл .env пример файла:
```
SECRET_KEY = ключ безопасности Django прописывается в settings.py
#подключение к базе данных postgres
NAME_DB = имя бд
USER_DB = имя пользователя
PASSWORD_DB = пароль
HOST_DB = IP
PORT_DB = порт
```
Создать супер пользователя:

```
python manage.py createsuperuser
```

Запустить проект:

```
python3 manage.py runserver
```

В проекте используются 4 таблицы:
Users - для хранения информации о пользователях Telegram.
TypeEducation - таблица для хранения информация о типах обучения.
Faculties - таблица для хранения информации о факультетах.
Profile - таблица для хранения информации о профилях.
Data - таблица для хранения описания профилей, таблица связанна с таблицами TypeEducation, Faculties, Profile связь многие к одному.
Данные таблицы доступны для редактирования через меню администирования http://localhost:8000/admin

Авторизация API: 
Для доступа к API необходимо получить токен авторизации

Отправляем POST запрос на адрес http://localhost:8000/api-token-auth/ тела сообщения JSON файл формата:
```
{
"username": "current_username",
"password": "current_password"
}
```

Пример ответа:
```
{ 'token' : '9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b' }
```

Для получения доступа к API мы должны передать токен с каждым запросом, пример:
{'Authorization': 'Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'}

## Developers

- [Aleksandr M](https://github.com/nuclear0077)
- Telegram @nuclear0077

