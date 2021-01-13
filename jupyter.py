import os
c = get_config()
c.NotebookApp.password = os.environ.get("JUPYTER_PASSWORD")
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.allow_remote_access = True
c.NotebookApp.open_browser = False