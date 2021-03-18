import re
from pecan import expose, redirect
import pecan
from six import remove_move
from webob.exc import status_map
from pecan_project.controllers.dns import AclsController
from pecan_project.controllers.dns import ViewsController
from pecan_project.controllers.dns import ZonesController
from pecan_project.controllers.dns import RecordsetController

class RootController(object):

    @expose()
    def _lookup(self,kind,*remainder):
        if kind == 'acl':
            return AclsController.AclsController(), remainder
        elif kind == 'views':
            return ViewsController.ViewsController(), remainder
        elif kind == 'zones':
            return ZonesController.ZonesController(), remainder
        elif kind == 'recordsets':
            return RecordsetController.RecordsetController(), remainder
        else:
            pecan.abort(404)

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

    @expose()
    def hours(self):
        return "Open 24/7 on the web"
