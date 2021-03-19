'''
Date:2021/3/19
Author:Guoyha
'''
import pecan

from webob.exc import status_map
from pecan_project.controllers.dns import base


class RecordsetController(object):

    @pecan.expose('json')
    def index(self):
        return {"Information": "The url is for RRS base RestApi "
                "interface"}

    # http://127.0.0.1:8080/dns2/rrs/list?views_id=123&zones_id=123
    @pecan.expose()
    def list(self,**args):
        if args.get('view_id',-1) or args.get('zone_id',-1):
            self.view_id=args.get('view_id')
            self.zone_id=args.get('zone_id')
        else:
            return 'error'
        
        return 'self.view_id:%s,self.zone_id:%s' % (self.view_id,self.zone_id)