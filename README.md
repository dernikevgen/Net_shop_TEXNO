# Net_shop_TEXNO
Сайт интернет-магазина бытовой техники, cозданный на языке Python, платформа Django v2.2/
созданный с целью изучения данного фреймворка и охвата основных функций и возможностей.

В данном проекте используется Python версии 3.6.

Для разворота проекта на локальном компьютере потребуется:

1)создать базу данных sql, внести в файле settings.py (shop_py2/py_shop/py_shop/settings.py)
в разделе DATABASES необходимые данные для её подключения.

2)Активировать виртуальную среду в проекте

2.2)Установить необходимые пакеты в виртуальную среду, указанные в файле  requirements.txt (shop_py2/py_shop/requirements.txt)
с помощью командной строки в директории проекта (shop_py2/py_shop/)

3)Cоздать аккаунт администратора командой("python manage.py createsuperuser")
п.с в той же директории, (смотреть пункт 2 )

4)Создать миграции в базу данных("python manage.py makemigrations", а после "python manage.py migrate")

5)Запустить сервер ("python manage.py runserver")

6)Авторизироваться в Django administrator 
Добавить всё необходимое на сайт через таблицы в аккаунте администратора.
