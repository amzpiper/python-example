from webob.exc import status_map
from pecan_project.controllers.dns import base


class ViewsController(base.BaseRestController):
    
    def list(self):
        return "Welcome to view of list."
    
    def get_one(self, view_id):
        return "We have view of %s . " % view_id
