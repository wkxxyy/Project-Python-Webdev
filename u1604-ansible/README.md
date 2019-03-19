## Reference

- [ansible reference](https://www.ansible.com/resources/get-started)

## Pre-Requirement

- Python3
- Ubuntu 18.04 (Ubuntu 16.04)

## QuickStart

```bash
$ cd u1604-ansible
```

## Set your Ansible config

file path: /etc/ansible/hosts

```conf
[node2] # servers group name
ip_addr # server ip
```

### One step to deploy

1. `ansible-playbook ./site.yml`

### Play step by step

1. init `ansible-playbook ./playbooks/init_os.yml`
2. deploy project `ansible-playbook ./playbooks/copy_project.yml`
3. configure supervisor `ansible ./playbooks/configure_supervisor.yml`
4. configure nginx `ansible ./playbooks/configure_nginx.yml`
