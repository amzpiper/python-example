'''
Date:2021/3/19
Author:Guoyha
'''

import pecan

from webob.exc import status_map
from pecan_project.controllers.dns import base


class ZonesController(object):
    
    @pecan.expose('json')
    def index(self):
        return {"Information": "The url is for Zones base RestApi "
                "interface"}

    # http://127.0.0.1:8080/dns2/zones/list?view_id=1
    @pecan.expose('json')
    def list(self, view_id):
        if str(view_id) == 0 :
            return self.return_msg('error', 'view_id is inqure', None)

        return 'We have zone of View id is %s' % view_id
    
    # http://127.0.0.1:8080/dns2/zones/show?views_id=123&zones_id=123
    @pecan.expose('json')
    def show(self, **args):
        if args.get('view_id',-1) or args.get('zone_id',-1):
            self.view_id=args.get('view_id')
            self.zone_id=args.get('zone_id')
        else:
            return self.return_msg('error', 'view_id or zone_id is inqure', None)
        
        return str(args)

    def return_msg(self, status, message, content):
        # dic = {"ret_code": ret_code, "ret_msg": ret_msg}
        dic = {
         "status": status,
         "message": message,
         "content": content
         }
        return dic
