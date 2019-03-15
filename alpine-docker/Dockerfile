FROM frolvlad/alpine-python3

RUN mkdir /run/nginx
RUN \
    apk update && \
    apk upgrade && \
    apk add --no-cache bash git openssh nginx build-base python3-dev zlib-dev py-pip jpeg-dev supervisor openrc
RUN mkdir /home/www && \
    mkdir /home/www/AccountOnline2
RUN mkdir /home/www/AccountOnline2/logs && \
    mkdir /home/www/AccountOnline2/tool
RUN git clone https://github.com/wu-wenxiang/ZZLARGE-Project-DjangoTest /home/www/AccountOnline2/src
RUN cd /home/www/AccountOnline2/src && \
    pip3 install -r requirements.txt
RUN cd /home/www/AccountOnline2/src/mysite && \
    python3 manage.py collectstatic
RUN mkdir /etc/supervisor && \
    mkdir /etc/supervisor/conf.d
RUN touch /var/run/supervisor.sock
ADD ./deployconfig/supervisord.conf /etc/supervisord.conf
ADD ./deployconfig/supervisor.conf /etc/supervisor/conf.d/AccountOnline2.conf
ADD ./deployconfig/nginx.conf /etc/nginx/conf.d/my_site.conf
ADD ./deployconfig/start.sh /tmp/start.sh
RUN rc-update add nginx default && rc-update add supervisord default
EXPOSE 80
CMD [ "sh", "/tmp/start.sh" ]
