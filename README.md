# Net_shop_TEXNO
Сайт интернет-магазина бытовой техники, cозданный на фреймворке Django, с использованием языка Python,
созданный с целью изучения данного фреймворка и охвата основных функций и возможностей

В данном проекте используется версия Python 3.6

Для разворота проекта на локальном компьютере потребуется:

1)создать базу данных sql, внести в файле settings.py (shop_py2/py_shop/py_shop/settings.py)
в разделе DATABASES необходимые данные.

2)Установить пакеты версий указанных в файле  requirements.txt (shop_py2/py_shop/requirements.txt)
с помощью командной строки в репозитории прроекта (shop_py2/py_shop/)
(для python2 "pip install -r requirements.txt", для python3 "pip3 install -r requirements.txt")

3)Cоздавать аккаунт администратора командой("python manage.py createsuperuser")
п.с в том же репозитории, (смотреть пункт 2 )

4)Создать миграции в базу данных("python manage.py makemigrations", а после "python manage.py migrate")

5)Запустить сервер ("python manage.py runserver")

6)Авторизироваться в Django administrator (http://localhost:8000(порт браузера по умолчанию "8000")/admin)
Добавить всё необходимое на сайт через таблицы в аккаунте администратора.
