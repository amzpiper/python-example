'''
Date:2021/3/19
Author:Guoyha
'''

import re
import pecan
from pecan.core import redirect

from webob.exc import status_map
from pecan_project.controllers.dns import base

class AclsController(object):

    @pecan.expose('json')
    def index(self):
        return {"Information": "The url is for Acl base RestApi "
                "interface"}

    # http://127.0.0.1:8080/dns2/acls/list
    @pecan.expose()
    def list(self):
        return "Welcome to Acl of list."
    
    # http://127.0.0.1:8080/dns2/acls/show?acl_id=1
    @pecan.expose()
    def show(self,acl_id,*args):
        # http://127.0.0.1:8080/dns2/acls/show
        # 不输入参数会报错，且无法捕捉
        if acl_id == None:
            return {
                "status": 400,
                "message": 'view_id is inqure',
                "content": None
            }
        if str(acl_id) == 0 :
            return {
                "status": 400,
                "message": 'view_id is inqure',
                "content": None
            }
        else:
            return "We have acl of %s . " % acl_id

