# Qualia-AC
Qualia Engine for the Artcasting Project http://www.artcastingproject.net


## Building the Environment

### Requirements

* [Ansible](https://github.com/ansible/ansible)
* [Vagrant](https://www.vagrantup.com)
* [VirtualBox](https://www.virtualbox.org)

### Starting up

From the project directory:
```shell
vagrant up
```
This will download the relevant Vagrant box, create the development environment and install the required packages. Once finished, you can use:
```shell
vagrant ssh
```
to connect to the box. To start the development server:
```shell
cd /var/www/qualia
python manage.py runserver 0.0.0.0:8000
```
The engine will be running on your machine. You can load the homepage in a web browser: http://127.0.0.1:8000
