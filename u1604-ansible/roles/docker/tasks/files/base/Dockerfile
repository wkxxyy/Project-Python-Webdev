FROM python:3.6.8

RUN apt-get update && \
    apt-get install -y nginx python-pip
RUN mkdir /home/www && \
    mkdir /home/www/AccountOnline2 && \
    mkdir /home/www/AccountOnline2/logs && \
    mkdir /home/www/AccountOnline2/tool && \
    git clone https://github.com/wu-wenxiang/ZZLARGE-Project-DjangoTest /home/www/AccountOnline2/src
RUN cd /home/www/AccountOnline2/src && \
    pip3 install -r requirements.txt
RUN cd /home/www/AccountOnline2/src/mysite && \
    python3 manage.py collectstatic
