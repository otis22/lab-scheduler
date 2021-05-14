FROM jupyter/scipy-notebook

USER root

RUN apt-get update
RUN apt install -y python-dev python3-dev libmysqlclient-dev tzdata cron less

ENV TZ Europe/Kiev
ENV PATH ${PATH}:/usr/local/bin:/opt/conda/bin/

USER jovyan
RUN pip install --upgrade pip
RUN pip install mysqlclient && pip install ipython-cache ipython-sql mysql-connector-python pymysql jupyterlab-scheduler requests
RUN conda install -c conda-forge ipyleaflet jupyterlab nodejs
RUN pip install jupyterlab_scheduler




USER root

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD cron && env >> /etc/environment && tail -f /var/log/cron.log
