FROM webdev_base

#ADD ./deployconfig/nginx.conf /etc/nginx/nginx.conf
ADD ./deployconfig/AccountOnline2.conf /etc/nginx/conf.d/AccountOnline2.conf
ADD ./deployconfig/AccountOnline2.conf /etc/nginx/sites-enabled/AccountOnline2
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
