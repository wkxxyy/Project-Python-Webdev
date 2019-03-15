FROM python:3.6.8

RUN apt-get update && \
    apt-get install -y nginx python-pip supervisor systemd
RUN mkdir /home/www && \
    mkdir /home/www/AccountOnline2 && \
    mkdir /home/www/AccountOnline2/logs && \
    mkdir /home/www/AccountOnline2/tool && \
    git clone https://github.com/wu-wenxiang/ZZLARGE-Project-DjangoTest /home/www/AccountOnline2/src
RUN cd /home/www/AccountOnline2/src && \
    pip3 install -r requirements.txt
RUN cd /home/www/AccountOnline2/src/mysite && \
    python3 manage.py collectstatic
ADD ./deployconfig/supervisord.conf /etc/supervisor/supervisord.conf
ADD ./deployconfig/supervisor.conf /etc/supervisor/conf.d/AccountOnline2.conf
ADD ./deployconfig/nginx.conf /etc/nginx/conf.d/my_site.conf
ADD ./deployconfig/start.sh /tmp/start.sh
EXPOSE 80
CMD [ "sh", "/tmp/start.sh" ]
