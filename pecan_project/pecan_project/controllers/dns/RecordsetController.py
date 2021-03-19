from webob.exc import status_map
from pecan_project.controllers.dns import base


class RecordsetController(base.BaseRestController):

    def __init__(self):
        super(RecordsetController, self).__init__()
    
    def list(self, req, *args, **kwargs):
        return "Welcome to Recordset of list."
    
    def show(self, req, id, *args, **kwargs):
        rrs_id = id
        zone_id = None
        view_id = None
        body = None
        print(len(args))
        
        # http://127.0.0.1:8080/records/zones/view/456
        if len(args) == 1:
            view_id = args[0]
            body = "We have zone of /zone/view/%s . "% view_id
            # todo: select list of zone's view_id is %s 
        
        # http://127.0.0.1:8080/records/000/zones/123/
        elif len(args) == 2:
            zone_id = args[1]
            body = "We have zone of /records/%s/zone/%s/view/%s . " % (rrs_id,zone_id)
        
        # http://127.0.0.1:8080/zones/456
        elif len(args) == 0:
            body = "We have zone of /records/%s . "% rrs_id
            # todo: select all of zone
        else:
            body = '''
            Bad Requset at Path
            Please check the Path
            '''
        return body
