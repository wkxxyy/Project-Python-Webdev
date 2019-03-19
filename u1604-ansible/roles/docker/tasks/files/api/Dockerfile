FROM webdev_base

WORKDIR /home/www/AccountOnline2/src/mysite
EXPOSE 8000
CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "--workers", "5", "--worker-class" ,"gevent" ,"mysite.wsgi:application" ]
