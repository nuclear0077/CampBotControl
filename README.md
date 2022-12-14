## CampBotControl

## About
Управление для camp бота образовательно платформы.

Реализовано наполнение базы данных через веб интерфейс и API для получения информацию из базы данных.

Данный бот разрабатывался в коммерческих целях и обезличен.

Сам клиент для получения данных по API и Бот [CampBot](https://github.com/nuclear0077/CampBot)

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

Data - таблица для хранения описания профилей, таблица связанна с таблицами TypeEducation, Faculties, Profile.

Данные таблицы доступны для редактирования через меню администирования http://localhost:8000/admin

Авторизация API: 

Для доступа к API необходимо получить токен авторизации

Отправляем POST запрос на адрес http://localhost:8000/api-token-auth/ тела сообщения JSON формата:
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

Для получения доступа к API мы должны передать токен в заголовке с каждым запросом, пример передачи токена:

```
{'Authorization': 'Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'}
```

### Методы API
#### Работа с пользователями
Получить список всех пользователей:
Метод GET
```
http://127.0.0.1:8000/api/v1/users/
```
Пример ответа:
```
[
    {
        "user_id": 376894637,
        "first_name": "Александр",
        "last_name": "М",
        "age": 28,
        "gender": "М",
        "city": "Москва",
        "is_active": true,
        "department": 99,
        "admin": true
    }
]
```

Работа с конкретным пользователем, реализованы методы CRUD
```
http://127.0.0.1:8000/api/v1/users/user_id/
```
Пример ответа:
```
  {
      "user_id": 376894637,
      "first_name": "Александр",
      "last_name": "М",
      "age": 28,
      "gender": "М",
      "city": "Москва",
      "is_active": true,
      "department": 99,
      "admin": true
  }
```

#### Работа с типами образования.
Режим работы только чтение.

Получить список всех типов образования.

Метод GET
```
http://127.0.0.1:8000/api/v1/type/
```
Пример ответа:
```
[
    {
        "id": 1,
        "name": "СПО"
    },
    {
        "id": 2,
        "name": "БАК"
    }
]
```

Получить информацию о конкретном образовании.

Метод GET
```
http://127.0.0.1:8000/api/v1/type/pid/
```
Пример ответа:
```
  {
      "id": 1,
      "name": "СПО"
  }
```

#### Работа с типами факультетами.
Режим работы только чтение.

Получить список всех факультетов по типу образования.

Значения могут дублироваться, так как пересекаются в типах обарзования.

Метод GET
```
http://127.0.0.1:8000/api/v1/faculties/type_pk/
```
Пример ответа:
```
[
    {
        "id": 1,
        "name": "Коммерция"
    },
    {
        "id": 2,
        "name": "Гостиничное дело"
    }
]
```

#### Работа с типами профилями.
Режим работы только чтение.

Получить список всех профилей по факультету и типу образования.

Метод GET
```
http://127.0.0.1:8000/api/v1/profiles/type_pk/facultie_pk/
```
Пример ответа:
```
[
    {
        "id": 3,
        "name": "Коммерция (по отраслям)"
    },
    {
        "id": 4,
        "name": "Предпринимательство"
    }
]
```


#### Получение информации о описании профиля.
Режим работы только чтение.

Получить описание профиля по факультету и типу образования.

Метод GET
```
http://127.0.0.1:8000/api/v1/descriptions/type_pk/facultie_pk/profile_pk/
```
Пример ответа:
```
[
    {
        "id": 1,
        "name": "Подробное описание, данное поле переименовано в сериализаторе для удобства парсинга JSON"
    }
]
```


## Developer

- [Aleksandr M](https://github.com/nuclear0077)
- Telegram @nuclear0077

