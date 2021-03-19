from webob.exc import status_map
from pecan_project.controllers.dns import base

class ViewsController(base.BaseRestController):

    def __init__(self):
        super(ViewsController, self).__init__()

    # http://127.0.0.1:8080/views
    def list(self, req, *args, **kwargs):
        return "Welcome to view of list."
    
    # http://127.0.0.1:8080/views/1
    def show(self, req, id, *args, **kwargs):
        return "We have view of %s " % id
