'''
Date:2021/3/19
Author:Guoyha
'''

import pecan

from pecan_project.controllers.dns2 import AclsController
from pecan_project.controllers.dns2 import ViewsController
from pecan_project.controllers.dns2 import ZonesController
from pecan_project.controllers.dns2 import RecordsetController

class DNSController(object):
    def __init__(self):
        return

    @pecan.expose('json')
    def index(self):
        return {"Information": "The url is for DNS base RestApi "
                "interface"}

    @pecan.expose()
    def _lookup(self, kind, *remainder):
        if kind == 'acls':
            return AclsController.AclsController(), remainder
        elif kind == 'views':
            return ViewsController.ViewsController(), remainder
        elif kind == 'zones':
            return ZonesController.ZonesController(), remainder
        elif kind == 'rrs': 
            return RecordsetController.RecordsetController(), remainder
        else:
            pecan.abort(404)
    
