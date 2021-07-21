FROM jupyter/scipy-notebook

USER root

RUN apt-get update
RUN apt install -y python-dev python3-dev default-libmysqlclient-dev build-essential tzdata cron less libssl-dev

#public directory
RUN groupadd jupyterhub-users
RUN mkdir -p /srv/scratch
RUN chown root:jupyterhub-users /srv/scratch
RUN chmod 777 /srv/scratch
RUN chmod g+s /srv/scratch
RUN ln -s /srv/scratch /etc/skel/scratch

USER jovyan
RUN pip install --upgrade pip
RUN pip install mysqlclient && pip install ipython-cache ipython-sql mysql-connector-python pymysql jupyterlab-scheduler requests gspread oauth2client oauthenticator
RUN conda install -c conda-forge ipyleaflet jupyterlab nodejs
RUN pip install jupyterlab_scheduler


ENV TZ Europe/Kiev

CMD USER=jovyan jupyterhub --config=/conf/jupyter.py