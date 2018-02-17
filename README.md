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
- dd