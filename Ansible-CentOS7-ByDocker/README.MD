## 项目描述

- 通过ansible部署在centos7上，通过Docker提供服务

## 系统要求

- Centos7+

## 设置主机参数

1.设置主机参数：./hosts

```conf
[groups_name]
Your_target_IP ansible_ssh_user="username" ansible_ssh_pass='passwd'

eg:
[docker]
192.168.0.107 ansible_ssh_user=root ansible_ssh_pass='wg199489'
```

## 修改剧本配置

1.修改剧本配置：./site_server.yml

在首行hosts:后修改上步设置的groups_name

```conf
- hosts: groups_name

eg:
- hosts: docker
```

### 一键部署

1. `ansible-playbook -i ./hosts site_server.yml`



### 使用

1. 打开浏览器输入127.0.0.1即可
2. 用户名：admin    密码： 56e1E@ab1234