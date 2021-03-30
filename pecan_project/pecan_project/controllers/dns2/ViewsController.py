'''
Date:2021/3/19
Author:Guoyha
'''

import pecan

from webob.exc import status_map
from pecan_project.controllers.dns2.zdns_driver import dns_zone_driver

class ViewsController(object):

    def __init__(self):
        self.msg='msg'
        self.manager = dns_zone_driver.get_instance()


    @pecan.expose('json')
    def index(self):
        return {"Information": "The url is for Views base RestApi "
                "interface"}
                
    # http://127.0.0.1:8080/dns2/views/list
    @pecan.expose('json')
    def list(self):
        return "Welcome to view of list."
    
    # http://127.0.0.1:8080/dns2/views/show?view_id=123
    @pecan.expose('json')
    def show(self, view_id):
        if str(view_id) == 0 :
            return self.return_msg('error', 'view_id is inqure', None)

        return "We have view of %s " % view_id

    def return_msg(self, status, message, content):
        # dic = {"ret_code": ret_code, "ret_msg": ret_msg}
        dic = {
         "status": status,
         "message": message,
         "content": content
         }
        return dic