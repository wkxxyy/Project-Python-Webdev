# Project-Python-Webdev

## SSH Config
- `sudo apt-get install ssh sudo`
- `ssh-keygen -t rsa`
- `ssh-copy-id pear@192.168.206.129`
- `sudo passwd`
- `su`
- `vi /etc/ssh/sshd_config`
- `PermitRootLogin yes`
- `sudo /etc/init.d/ssh restart`

## Ansible
- `touch playbook.yml && touch hosts`
- `mkdir roles && cd roles`
- `ansible-galaxy init server`
- `ansible-playbook playbook.yml -i hosts -u root`
- Set Python

		cd /usr/bin/
		ln -s pip3 pip
		ln -s python3 python
- [Refer](https://thecustomizewindows.com/2016/06/ansible-ubuntu-16-04-1-click-install-wordpress-nginx-playbook-tutorial/)
- [Refer to Docker](https://docs.docker.com/get-started/part2/)

## Nginx
- Hosts

		cat /private/etc/hosts
		
		127.0.0.1	localhost
		255.255.255.255	broadcasthost
		::1             localhost
		
		192.168.206.170	test170.wenwtest.com
		192.168.206.171	test171.wenwtest.com
