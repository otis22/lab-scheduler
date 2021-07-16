import os
c = get_config()

c.Authenticator.admin_users = {'admin'}
c.LocalAuthenticator.create_system_users=True

if os.environ.get('JUPYTER_CERTFILE') and os.environ.get('JUPYTER_KEYFILE'):
	c.NotebookApp.certfile = os.environ.get('JUPYTER_CERTFILE')
	c.NotebookApp.keyfile = os.environ.get('JUPYTER_KEYFILE')