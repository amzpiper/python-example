from re import template
from pecan import expose, redirect
from webob.exc import status_map
import othersystem.controllers.accesstoke as accesstoke
import othersystem.controllers.userinfo as userinfo
import requests
import json

class OAuthServerController(object):

    # @expose('hello.html')
    @expose('json')
    def index(self,**args):
        print("args:",args)
        code = args.get("code")
        print("获取到Authorization Code:",code)

        # 获取到Authorization Code后，需要根据认证流程做以下开发适配。
        # 1.通过Authorization Code获取Access Token
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type":"authorization_code",
            "client_id":"e3077f17a85541eaa0b1823188b099a2",
            "client_secret":"67fffddc9085d0f477ce1a6233e1b71059bfba3017967f62",
            "redirect_uri":"http://www.amzpiper.com/oauthserver/",
            "code":code
        }
        response = requests.post(url="https://studio.e.huawei.com/baas/auth/v1.0/oauth2/token",data=body,headers=headers)
        print("get_token_response:",response.text)
        get_token_response = json.loads(response.text)
        print("access_token:",get_token_response['access_token'])
        access_token = get_token_response['access_token']

        # 2.通过Access Token获取User信息
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization":"Bearer "+access_token
        }
        response = requests.get(url="https://studio.e.huawei.com/u-route/baas/oauth/v1.0/third/userinfo",headers=headers)
        print("get_user_response:",response.text)
        get_user_response = json.loads(response.text)
        result = get_user_response['result']
        name = result['name']
        redirect("/hello?name="+name+"&"+"result="+str(get_user_response))
        # return dict(name=name,result=get_user_response)

    @expose('error.html')
    def error(self, status):
        try:
            status = int(status)
        except ValueError:  # pragma: no cover
            status = 500
        message = getattr(status_map.get(status), 'explanation', '')
        return dict(status=status, message=message)
