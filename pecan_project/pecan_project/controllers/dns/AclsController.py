from webob.exc import status_map
from pecan_project.controllers.dns import base

class AclsController(base.BaseRestController):
    
    def __init__(self):
        super(AclsController, self).__init__()

    # http://127.0.0.1:8080/acl
    def list(self, req, *args, **kwargs):
        return "Welcome to Acl of list."
    
    # http://127.0.0.1:8080/acl/1
    def show(self, req, id, *args, **kwargs):
        return "We have acl of %s . " % id
