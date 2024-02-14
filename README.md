# Store project

## Описание проекта 
 
Store - это интернет магазин мебели созданный на Django с использованием templates! 
* Главная страница интернет-магазина содержит: 
слайдер, ряд товаров по скидке, краткое описание коллекций мебели с фотографиями; 
* На внутренних страницах сайта включена колонка, в которой размещены: 
корзина покупок, поиск по сайту, дополнительное меню, мебель из каталога по акции и контакты; 
* Каталог позволяет разделить мебель по рубрикам: 
кровати, шкафы и прочее;
 
## Установка и запуск проекта локально

Для того, чтобы запустить сайт локально на своем компьютере, нужно выполнить следующие шаги:

1. Клонировать репозиторий на компьютер:
```
git clone https://github.com/Eduard-Latypov/Store.git
```

2. Перейти в директорию проекта:
```
cd app
```

3. Cоздать и активировать виртуальное окружение:

```
python -m venv venv

# linux
source venv/bin/activate

# windows
source venv/source/activate
```
4. Скачать и создать базу данных PostgreSQL
```
На оф. сайте PosgreSQL ест вся инфа
```

5. Создать базу данных 
```
CREATE USER <username> WITH PASSWORD <password>; - user и password запишутся в одноименные переменные в Django.settings
CREATE DATABASE <name> OWNER <user> ENCODING ‘UTF-8’; - name запишется в одноименную переменную в Django.settings
```

6. Создать файл `.env`:

```
touch .env
```

7. Заполнить файл следующим содержанием:
```
SECRET_KEY=секретная комбинация из одноименного параметра в settings.py
NAME=<DATABASE> из созданного раннее БД 
USER=<USER> юзер которого вы создали в Postgres
PASSWORD=<PASSWORD> соответственно пароль
```

8. Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

9. Сформировать и выполнить миграции:

```
python manage.py makemigrations

# в случае, если файлы миграций не формируются командой выше, запустить команду
# последовательно с указанием имен приложений в следующем формате
python manage.py makemigrations [имя приложения]

python manage.py migrate
```

9. Создать супер-пользователя:
```
python manage.py createsuperuser
```

10. Собрать статику:
```
python manage.py collectstatic
```

11. Запустить dev-сервер:
```
python manage.py runserver
```

## Технологическй стек

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)


## Авторы

[Eduard-Latypov](https://github.com/Eduard-Latypov)

