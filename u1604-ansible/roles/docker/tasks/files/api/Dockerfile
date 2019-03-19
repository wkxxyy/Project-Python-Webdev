FROM python:3.6.8

RUN apt-get update && \
    apt-get install -y python-pip
RUN mkdir /home/www && \
    mkdir /home/www/AccountOnline2 && \
    mkdir /home/www/AccountOnline2/logs && \
    mkdir /home/www/AccountOnline2/tool && \
    git clone https://github.com/wu-wenxiang/ZZLARGE-Project-DjangoTest /home/www/AccountOnline2/src
RUN cd /home/www/AccountOnline2/src && \
    pip3 install -r requirements.txt
WORKDIR /home/www/AccountOnline2/src/mysite
EXPOSE 8000
CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "--workers", "5", "--worker-class" ,"gevent" ,"mysite.wsgi:application" ]
