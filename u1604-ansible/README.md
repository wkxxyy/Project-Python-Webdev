## Reference

- [ansible reference](https://www.ansible.com/resources/get-started)

## Pre-Requirement

- Python3

## QuickStart

```bash
cd u1604-ansible
```

### One step to deploy

1. `ansible-playbook ./site.yml`

### play step by step

1. init `ansible-playbook ./init_os.yml`
2. deploy project `ansible-playbook ./copy_project.yml`
3. configure supervisor `ansible ./configure_supervisor.yml`
4. configure nginx `ansible ./configure_nginx.yml`
