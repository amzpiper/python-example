from pecan import expose, redirect
from webob.exc import status_map
import othersystem.controllers.accesstoke as accesstoke
import othersystem.controllers.userinfo as userinfo
import othersystem.controllers.getToken as token
import othersystem.controllers.getUserInfo as user
import othersystem.controllers.login as login
import othersystem.controllers.OAuthServer as oauthserver
import othersystem.controllers.Hello as hello

class RootController(object):

    @expose(generic=True, template='index.html')
    def index(self):
        return dict()

    @index.when(method='POST')
    def index_post(self, q):
        redirect('https://pecan.readthedocs.io/en/latest/search.html?q=%s' % q)

    @expose('error.html')
    def error(self, status):
        try:
            status = int(status)
        except ValueError:  # pragma: no cover
            status = 500
        message = getattr(status_map.get(status), 'explanation', '')
        return dict(status=status, message=message)

    @expose('josn')
    def _lookup(self, primary_key, *remainder):
        print("primary_key:",primary_key)
        print("_lookup")
        if primary_key=="accesstoke":
            return accesstoke.AccessTokenController(),remainder
        elif primary_key=="userinfo":
            return userinfo.UserInfoController(),remainder
        elif primary_key=="getToken":
            return token.AccessTokenController(),remainder
        elif primary_key=="getUserInfo":
            return user.UserInfoController(),remainder
        elif primary_key=="login":
            return login.LoginController(),remainder
        elif primary_key=="oauthserver":
            return oauthserver.OAuthServerController(),remainder
        elif primary_key=="hello":
            return hello.HelloController(),remainder
        else:
            return 404