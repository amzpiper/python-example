from pecan import expose, redirect
from webob.exc import status_map
import uuid


class AccessTokenController(object):
    
    @expose('json',force_canonical=False)
    def index(self,grant_type,code,client_id,client_secret,redirect_uri):
        print("grant_type:",grant_type)
        print("code:",code)
        print("client_id:",client_id)
        print("client_secret:",client_secret)
        print("redirect_uri:",redirect_uri)
        uid = str(uuid.uuid1())
        access_token = ''.join(uid.split('-'))
        print("access_token:",access_token)
        return {
                # "message":"this is AccessTokenController Api",
                # "grant_type":grant_type,
                # "code":code,
                # "client_id":client_id,
                # "client_secret":client_secret,
                # "redirect_uri":redirect_uri,
                "access_token":access_token
            }

    @expose('error.html')
    def error(self, status):
        try:
            status = int(status)
        except ValueError:  # pragma: no cover
            status = 500
        message = getattr(status_map.get(status), 'explanation', '')
        return dict(status=status, message=message)
