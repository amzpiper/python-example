from webob.exc import status_map
from pecan_project.controllers.dns import base

class AclsController(base.BaseRestController):
    
    def list(self):
        return "Welcome to Acl of list."
    
    def get_one(self, acl_id):
        return "We have acl of %s . " % acl_id
