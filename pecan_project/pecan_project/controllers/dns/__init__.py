import pecan

from pecan_project.controllers.dns import AclsController
from pecan_project.controllers.dns import ViewsController
from pecan_project.controllers.dns import ZonesController
from pecan_project.controllers.dns import RecordsetController

class DNSController(object):
    def __init__(self):
        return

    @pecan.expose('json')
    def index(self):
        return {"Information": "The url is for DNS base RestApi "
                "interface"}

    @pecan.expose()
    def _lookup(self, kind, *remainder):
        if kind == 'acl':
            return AclsController.AclsController(), remainder
        elif kind == 'view':
            return ViewsController.ViewsController(), remainder
        elif kind == 'zone':
            return ZonesController.ZonesController(), remainder
        elif kind == 'rrs': 
            return RecordsetController.RecordsetController(), remainder
        else:
            pecan.abort(404)
    
