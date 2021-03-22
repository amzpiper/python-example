import pecan

from six import remove_move
from webob.exc import status_map
from pecan_project.controllers import dns
from pecan_project.controllers import dns2

class RootController(object):

    @pecan.expose()
    def _lookup(self,kind,*remainder):
        if kind == 'dns':
            return dns.DNSController(), remainder
        elif kind == 'dns2':
            return dns2.DNSController(), remainder
        else:
            pecan.abort(404)

    @pecan.expose(generic=True, template='index.html')
    def index(self):
        return dict()
        