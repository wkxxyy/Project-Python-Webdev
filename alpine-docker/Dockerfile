FROM frolvlad/alpine-python3

RUN apk update && \
    apk add --no-cache bash git nginx build-base python3-dev zlib-dev jpeg-dev supervisor openrc
RUN mkdir /home/www && \
    mkdir /home/www/AccountOnline2 && \
    mkdir /home/www/AccountOnline2/logs && \
    mkdir /home/www/AccountOnline2/tool && \
    git clone https://github.com/wu-wenxiang/ZZLARGE-Project-DjangoTest /home/www/AccountOnline2/src
RUN cd /home/www/AccountOnline2/src && \
    pip3 install -r requirements.txt
RUN cd /home/www/AccountOnline2/src/mysite && \
    python3 manage.py collectstatic
RUN mkdir /etc/supervisor && \
    mkdir /etc/supervisor/conf.d &&\
    mkdir /run/nginx
ADD ./deployconfig/supervisord.conf /etc/supervisord.conf
ADD ./deployconfig/supervisor.conf /etc/supervisor/conf.d/AccountOnline2.conf
ADD ./deployconfig/nginx.conf /etc/nginx/conf.d/my_site.conf
ADD ./deployconfig/start.sh /tmp/start.sh
EXPOSE 80
CMD [ "sh", "/tmp/start.sh" ]
