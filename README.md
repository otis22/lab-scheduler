# jupyter lab with scheduller

# How to use 

1. Fork this repo and clone to localy 
1. `make all` for starting services
1. Open in browser http://localhost:8888
1. Default password `test`
1. `make down` for stop all services

# How to change password

1. Get the hash of your password `make hash-pass PASSWORD=test` where test is your password
1. Copy hashed password and put it into .env 
Example `JUPYTER_PASSWORD=argon2:$argon2id$v=19$m=10240,t=10,p=8$uZm69HinKbMOVcaw112HPA$ZwTZE8/BtrgNygeZ8PjRjw`
1. `make down` and `make up` for restart services

