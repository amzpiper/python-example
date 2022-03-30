from re import template
from pecan import expose, redirect
from webob.exc import status_map
import othersystem.controllers.accesstoke as accesstoke
import othersystem.controllers.userinfo as userinfo


class HelloController(object):

    @expose(generic=True, template='hello.html')
    def index(self,**args):
        name = args.get("name")
        get_user_response = args.get("result")
        print("name:"+name)
        print("get_user_response:"+get_user_response)
        return dict(name=name,result=get_user_response)

    @expose('error.html')
    def error(self, status):
        try:
            status = int(status)
        except ValueError:  # pragma: no cover
            status = 500
        message = getattr(status_map.get(status), 'explanation', '')
        return dict(status=status, message=message)