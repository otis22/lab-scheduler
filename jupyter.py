import os
from oauthenticator.google import LocalGoogleOAuthenticator

c = get_config()

c.JupyterHub.authenticator_class = LocalGoogleOAuthenticator
c.LocalGoogleOAuthenticator.delete_invalid_users = True
c.LocalGoogleOAuthenticator.create_system_users=True
c.LocalGoogleOAuthenticator.add_user_cmd = ['adduser', '--ingroup=jupyterhub-users', '-q', '--gecos', '""', '--disabled-password', '--force-badname']
c.LocalGoogleOAuthenticator.client_id = os.environ.get('GOOGLE_OAUTH_CLIENT_ID')
c.LocalGoogleOAuthenticator.client_secret = os.environ.get('GOOGLE_OAUTH_SECRET')


if os.environ.get('JUPYTER_CERTFILE') and os.environ.get('JUPYTER_KEYFILE'):
	c.NotebookApp.certfile = os.environ.get('JUPYTER_CERTFILE')
	c.NotebookApp.keyfile = os.environ.get('JUPYTER_KEYFILE')