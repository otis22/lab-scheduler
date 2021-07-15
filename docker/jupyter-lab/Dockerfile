FROM jupyter/scipy-notebook

USER root

RUN apt-get update
RUN apt install -y python-dev python3-dev default-libmysqlclient-dev build-essential tzdata cron less libssl-dev

USER jovyan
RUN pip install --upgrade pip
RUN pip install mysqlclient && pip install ipython-cache ipython-sql mysql-connector-python pymysql jupyterlab-scheduler requests gspread oauth2client
RUN conda install -c conda-forge ipyleaflet jupyterlab nodejs
RUN pip install jupyterlab_scheduler


ENV TZ Europe/Kiev

CMD USER=jovyan jupyterhub --config=/conf/jupyter.py