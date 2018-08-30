## Reference
- [fabric reference](http://docs.fabfile.org/en/2.3/getting-started.html)

## Pre-Requirement
- Django
- DB
	- if set git_db_url, copy git_db_url/demo.sqlite3 src/mysite/production.sqlite3 
	- else, cp src/mysite/demo.sqlite3 src/mysite/production.sqlite3

## QuickStart

1. `git clone https://github.com/wu-wenxiang/Project-Python-Webdev`
1. `cd Project-Python-Webdev/u1604-fabric`
1. `virtualenv -p python3 env`
1. `. env/bin/activate`
1. `pip install -r requirements.txt`
1. `cp .fabricrc fabricrc`，然后修改fabricrc文件
1. `fab -c fabricrc init_deploy_u1604`
1. [Demo](http://wuchunlong.eastasia.cloudapp.azure.com)
1. 用户名 / 密码：admin / 56e1E@ab1234
