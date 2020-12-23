# Тестовое задание "Places Remember"

Веб-приложение, которое позволяет хранить воспоминания о посещаемых местах.


## Условие задания

Пользователь заходит на сайт и видит страницу с кратким описанием сервиса. Также, он замечает
кнопку “Войти с помощью Facebook”, нажимая на которую FB предлагает ему разрешить доступ к его
базовой информации.
Он разрешает доступ, после которого должна открыться страница. В ее шапке будет имя и фотография
(информация взята из профиля FB), по центру страницы надпись “У вас нет ни одного воспоминания”,
кнопка “Добавить воспоминание” (ее расположение на ваше усмотрение), при нажатии на которую
должна открываться форма с возможностью указания места на карте, а также поле для ввода названия
и поле для ввода комментария об этом месте.
Далее пользователь может нажать на кнопку “Сохранить”, после чего он снова попадает на домашнюю
страницу со списком из этого элемента и возможностью добавлять новые места. Весь добавленный
список мест будет отображаться на домашней странице.
На домашней странице пользователя также есть кнопка, позволяющая ему выйти из своего аккаунта.
После выхода он должен попасть на приветственную страницу сервиса без возможности видеть список
посещаемых мест. При повторной авторизации через FB пользователь снова видит все свои
добавленные места.


## Запуск

На [Facebook developers](https://developers.facebook.com) создайте приложение.

ID-приложения и секретный ключ приложения - нужно вынести в перменные окружения.

В поле "Домены приложения" указать `localhost`.

В самом низу страницы настроек добавить платформу веб-сайт. Указать URL сайта - `https://localhost/`.

Установите Python третьей версии.

Скачайте код с GitHub.

Установите зависимости:

`pip3 install requirements.txt`

Проведите миграции:

`python3 manage.py migrate`

Запустите:

`python3 manage.py runsslserver`

Перейдите на [https://localhost:8000/](https://localhost:8000/).


## Переменные окружения

Часть настроек проекта берётся из переменных окружения.
Чтобы их определить, создайте файл .env рядом с manage.py 
и запишите туда данные в таком формате: ПЕРЕМЕННАЯ=значение.

* `DEBUG` - режим дебага. 
* `SECRET_KEY` - секретный ключ для Django.
* `ALLOWED_HOSTS` - доступные хосты. По умолчанию 127.0.0.1
* `FACEBOOK_APP_ID` - id приложения facebook.
* `FACEBOOK_APP_SECRET` - секретный ключ приложения facebook.
* `DATABASE_URL` - путь к БД.
* `ENV=development` - чтобы не было проблем с `django-heroku`.


## Используемые библиотеки

* [social-auth-app-django](https://pypi.org/project/social-auth-app-django/) - для авторизации через Facebook.
* [django-sslserver](https://pypi.org/project/django-sslserver/) - facebook требует, чтобы был ssl-сертификат.
* [environs](https://pypi.org/project/environs/) - для переменных окружения.
* [folium](https://pypi.org/project/folium/) - карта.
* [dj-database-url](https://pypi.org/project/dj-database-url/) - для подключения к БД через переменные окружения.
* [psycopg2](https://pypi.org/project/psycopg2/) - работы с Postgres.


## Цели проекта

Выполнение тестового задания.