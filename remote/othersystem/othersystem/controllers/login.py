from re import template
from types import MethodType
from pecan import expose, redirect
from webob.exc import status_map
import othersystem.controllers.accesstoke as accesstoke
import othersystem.controllers.userinfo as userinfo
import uuid

class LoginController(object):

    @expose(generic=True, template='login.html')
    def index(self):
        return dict()

    @expose(template='json')
    def sign(self, username,password):
        print("username:",username,"password:",password)

        redirect("https://studio.e.huawei.com/magno/render/SmartCampus__SystemManagement_0000000000c9Kx3qtwsT/Login")
    
    @expose('json',MethodType)
    def authorize(self,client_id,response_type,redirect_uri,scope):
        print(
            "client_id:",client_id,
            "response_type:",response_type,
            "redirect_uri:",redirect_uri,
            "scope:",scope
            )
        
        # oauth2配置登录
        # xianjin
        # redirect("https://studio.e.huawei.com/magno/render/SmartCampus__SystemManagement_0000000000c9Kx3qtwsT/Login?code=0000000000c9Kx3qtwsT")
        # huamao
        # https://studio.e.huawei.com/magno/render/SmartCampus__SystemManagement_0000000000hdy26HBtdx/Login?code=0000000000c9Kx3qtwsT
        
        # IAM手动登录
        print("redirect:",redirect_uri+"?code=123")
        redirect(redirect_uri+"?code=123")

    @expose('error.html')
    def error(self, status):
        try:
            status = int(status)
        except ValueError:  # pragma: no cover
            status = 500
        message = getattr(status_map.get(status), 'explanation', '')
        return dict(status=status, message=message)