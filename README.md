# jupyter lab with scheduller

# How to install

1. Fork this repo and clone to localy
2. Copy `.env.example` to `.env`
3. `make all` for build and run services
3. Get the hash of your password `make hash-pass PASSWORD=test` where test is your password
4. Copy hashed password and put it into .env instead `pass`. 
Example `JUPYTER_PASSWORD=argon2:$argon2id$v=19$m=10240,t=10,p=8$uZm69HinKbMOVcaw112HPA$ZwTZE8/BtrgNygeZ8PjRjw`
5. `make down` and `make up` for restart services

You can add your variables to .env and change jupyter.py 

# How to use 

1. `make all` for starting services
2. Open in browser http://localhost:8888