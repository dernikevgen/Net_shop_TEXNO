# Net_shop_TEXNO
Сайт интернет-магазина бытовой техники, cозданный на фреймворке Django, с использованием языка Python.
В данном проекте используется версия Python 3.6
Для развора проекта на локальном компьютере потребуется:
1)создать базу данных sql, внести в файле settings.py (shop_py2/py_shop/py_shop/settings.py)
в разделе DATABASES необходимые данные.
2)Установить пакеты версий указанных в файле  requirements.txt (shop_py2/py_shop/requirements.txt)
3)Cоздавать аккаунт администратора командой(python manage.py createsuperuser) 
из командной строки в репозитории (shop_py2/py_shop/)
4)Создать миграции в базу данных(python manage.py makemigrations а после python manage.py migrate)
5)Запустить сервер (python manage.py runserver)
