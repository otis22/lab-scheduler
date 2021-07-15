# jupyter lab with scheduller

# How to use 

1. Fork this repo and clone to localy 
1. `make all` for starting services
1. Create admin user by `docker exec -it jupyter-lab adduser admin`
1. Open in browser http://localhost:47755 and log in


*On first start press Build button on popup. Wait a couple of minutes and press Reload button on pop. That is all. You can use scheduler.*

* `make down` for stop service
* `make up` for start service
* for run scheduller - press right button on your note


# Other

`make exec` - for go to jupyter-lab container

`make exec-cron` - for go to jupyter-cron container

jupyter_scheduler can to broke crontab file, if schedule does not work check this line exist in crontab `PATH=/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin`  

example crontab

```shell
# DO NOT EDIT THIS FILE - edit the master and reinstall.
# (/tmp/tmpe1eziqdg installed on Tue Jan 12 23:07:20 2021)
# (Cron version -- $Id: crontab.c,v 2.13 1994/01/17 03:20:37 vixie Exp $)
PATH=/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
* * * * * echo "`date` [Cronjob executing]" >> /tmp/my_ipynb.log && papermill /home/jovyan/my.ipynb /dev/null >> /tmp/my_ipynb.log 2>&1 # jupyterlab_scheduler job script: my.ipynb
```

Add your ssl certificates - put variables to .env `JUPYTER_CERTFILE` and `JUPYTER_KEYFILE` for example `JUPYTER_KEYFILE=/home/jovyan/.cert/mykey.key`

# Google Sheets Intergration with gspread

You can upluad pandas frame to google sheets by schedule


Steps 

1. Read the [instructions](https://gspread.readthedocs.io/en/latest/oauth2.html#enable-api-access-for-a-project)
2. Make json auth file and download it
3. Copy generated email for auth like that `key@key-id.iam.gserviceaccount.com`
3. Create Table in Goggle Sheets 
4. Share the table with generated email
5. Write and run for upload, or do another thisn

```python
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'myauthjson.json', scopes=scope)
gc = gspread.authorize(credentials)

sht1 = gc.open_by_url('https://docs.google.com/spreadsheets/d/secret/edit#gid=0')
worksheet = sht1.worksheets()[0]
worksheet.update([df.columns.values.tolist()] + df.values.tolist())

```

After first run you can get url for enabling integration follow the instruction.

[More features](https://gspread.readthedocs.io/)
