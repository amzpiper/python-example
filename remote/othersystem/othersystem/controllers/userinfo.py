from pecan import expose, redirect
from webob.exc import status_map
import uuid

class UserInfoController(object):

    @expose('json')
    def index(self,access_token,scope,client_id):
        print("accesstoken:",access_token,",scope:",scope,",client_id:",client_id)
        uid = "amzpiper"
        print("uid:",uid)
        return {
            "id":123,
            "uid":uid
        } 

    @expose('error.html')
    def error(self, status):
        try:
            status = int(status)
        except ValueError:  # pragma: no cover
            status = 500
        message = getattr(status_map.get(status), 'explanation', '')
        return dict(status=status, message=message)