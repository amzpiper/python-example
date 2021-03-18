from webob.exc import status_map
from pecan_project.controllers.dns import base


class ZonesController(base.BaseRestController):
    
    def list(self):
        return "Welcome to Zones of list."
    
    def get_one(self, zone_id):
        return "We have zone of %s . " % zone_id
