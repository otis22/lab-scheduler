# jupyter lab with scheduller

# How to use 

1. Fork this repo and clone to localy 
1. `make all` for starting services
1. Open in browser http://localhost:8888
1. Default password `test`

*On first start press Build button on popup. Wait a couple of minutes and press Reload button on pop. That is all. You can use scheduler.*

* `make down` for stop service
* `make up` for start service
* for run scheduller - press right button on your note

# How to change password

1. Get the hash of your password `make hash-pass PASSWORD=test` where test is your password
1. Copy hashed password and put it into .env 
Example `JUPYTER_PASSWORD=argon2:$argon2id$v=19$m=10240,t=10,p=8$uZm69HinKbMOVcaw112HPA$ZwTZE8/BtrgNygeZ8PjRjw`
1. `make down` and `make up` for restart services


# Other

`make exec` - for go to jupyter-lab container

`make exec-cron` - for go to jupyter-cron container

jupyter_scheduler can to broke crontab file, if schedule does not work check this line exist in crontab `PATH=/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin`  