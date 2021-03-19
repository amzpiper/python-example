'''
Date:2021/3/19
Author:Guoyha
'''

import pecan

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
    
    # http://127.0.0.1:8080/dns2/acls/show?id=1
    @pecan.expose()
    def show(self,id):
        return "We have acl of %s . " % id

    
    def return_msg(self, status, message, content):
        # dic = {"ret_code": ret_code, "ret_msg": ret_msg}
        dic = {
         "status": status,
         "message": message,
         "content": content
         }
        return dic