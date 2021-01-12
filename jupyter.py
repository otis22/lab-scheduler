import os
c = get_config()

if os.environ.get("JUPYTER_PASSWORD", None) != None:
	c.NotebookApp.password = os.environ.get("JUPYTER_PASSWORD")

c.NotebookApp.ip = '*'
c.NotebookApp.allow_remote_access = True
c.NotebookApp.open_browser = False