Kemp Load balancencer restarter
=============


First run
---------

- set up public key acceess to localhost . Add 	`~/.ssh/id_rsa.pub` to 	`~/.ssh/authorized_keys`
- Run `ansible-playbook -i hosts main.yml`


Configuration
------------

The configuration is done uing file `group_vars/local`

loadmaster: is a dictionary with ip, username and password of Kemp Load Master

all_servers: is a list of virtual IP list. All virtual IP list specified in `all_servers` will be restarted.   
A virtual IP list is a list of virtual IP dictionary. A single virtual IP dictionary contains `ip` aand `port` of the virtual IP 


TODO
----

- Rolling deploy. TBD
