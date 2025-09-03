# DjangoDockerNginxRedisCelery

Шаблон Django-приложения, обернутого в docker-контейнер, с подключенными celery и redis, работающего через Nginx.

Для запуска:

1. Склонировать репозиторий

   ```git clone https://github.com/artemmj/django_docker_nginx_redis_celery.git```

   и перейти в него

   ```cd django_docker_nginx_redis_celery```
2. Создать файл .env.dev (сюда складывать нужные переменные окружения, пока достаточно пустого файла)

   ```touch .env.dev```

3. Создать виртуальное окружение, установить в него зависимости
   
   ```python -m venv venv```
   
   ```. venv/bin/activate```
   
   ```pip install -r requirements.txt```

   при желании обновить pip

   ```pip install --upgrade pip```
4. Запустить сборку и запуст контейнеров
   
   ```docker-compose up -d --build```
5. Применить миграции и собрать статику - войти в контейнер и запустить команды
   
   ```docker-compose exec app bash```
   
   ```./manage.py collectstatic```
   
   ```./manage.py migrate```
