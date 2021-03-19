import re
import pecan
from webob.exc import status_map
from pecan_project.controllers.dns import base


class ZonesController(base.BaseRestController):
    
    def __init__(self):
        super(ZonesController, self).__init__()

    def list(self, req, *args, **kwargs):
        return 'We have zone of Any All'
    
    def show(self, req, id, *args, **kwargs):
        zone_id = id
        view_id = None
        response = None
        print(len(args))
        # http://127.0.0.1:8080/zones/view/456
        if len(args) == 1:
            view_id = args[0]
            response = "We have zone of /zone/view/%s . "% view_id
            # todo: select list of zone's view_id is %s 
        # http://127.0.0.1:8080/zones/123/view/456
        elif len(args) == 2:
            view_id = args[1]
            response = "We have zone of /zone/%s/view/%s . " % (zone_id, view_id)
            # todo: select one of zone
        # http://127.0.0.1:8080/zones/456
        elif len(args) == 0:
            response = "We have zone of /zone/%s . "% zone_id
            # todo: select all of zone
        else:
            response = '''
            Bad Requset at Path
            Please check the Path
            '''
        return response

    @pecan.expose('json')
    def show2(self,zone_id,view,view_id):

        return "zone/%s/view/%s" % (zone_id,view_id)

