FROM webdev_base

ADD ./deployconfig/nginx.conf /etc/nginx/conf.d/my_site.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
