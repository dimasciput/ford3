docker run -ti -v /Users/timlinux/dev/python/projecta/deployment/static/:/home/web/static/ --link projecta-uwsgi -p 8889:80 -v /Users/timlinux/dev/python/projecta/deployment/media/:/home/web/media/ kartoza/nginx-django