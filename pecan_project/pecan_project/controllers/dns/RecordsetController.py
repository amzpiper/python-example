from webob.exc import status_map
from pecan_project.controllers.dns import base


class RecordsetController(base.BaseRestController):
    
    def list(self):
        return "Welcome to Recordset of list."
    
    def get_one(self, zone_id):
        return "We have Recordset of %s . " % zone_id
