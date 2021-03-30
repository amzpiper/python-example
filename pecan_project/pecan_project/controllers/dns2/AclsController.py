'''
Date:2021/3/19
Author:Guoyha
'''

import re
import pecan
from webob.exc import status_map
from pecan_project.controllers.dns2.zdns_driver import dns_zone_driver

class AclsController(object):

    def __init__(self):
        self.msg='msg'
        self.manager = dns_zone_driver.get_instance()

        
    @pecan.expose('json')
    def index(self):
        return {"Information": "The url is for Acl base RestApi "
                "interface"}

    # http://127.0.0.1:8080/dns2/acls/list
    @pecan.expose('json')
    def list(self):
        response = self.manager.get_acls_driver()
        return response
    
    # http://127.0.0.1:8080/dns2/acls/show?acl_id=1
    @pecan.expose('json')
    def show(self,acl_id,*args):
        # http://127.0.0.1:8080/dns2/acls/show
        # 不输入参数会报错，且无法捕捉
        if str(acl_id) == 0 :
            return {
                "status": 400,
                "message": 'view_id is inqure',
                "content": None
            }

        self.manager.get_acls_driver()
        return "We have acl of %s . " % acl_id

