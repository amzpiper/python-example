import functools
import pecan
from pecan import rest


def expose(function):
    """
    Packaging pecan RestController expose method. Resolving WSGi request body.
    """

    @pecan.expose('json')
    @functools.wraps(function)
    def decorated_function(self, *args, **kwargs):
        func = functools.partial(function, self, pecan.request)
        try:
            func = func(*args, **kwargs)
        except Exception:
            pecan.response.status = 500
            return {"ret_code": 500, "ret_msg": "Bad Method Request"}
        return func

    return decorated_function


class BaseRestController(rest.RestController):
    """
    A base class implement pecan RestController.
    """
    @property
    def response(self):
        return pecan.response

    @expose
    def post(self, req, *args, **kwargs):
        return self.create(req, *args, **kwargs)

    @expose
    def put(self, req, id, *args, **kwargs):
        return self.update(req, id, *args, **kwargs)

    @expose
    def delete(self, req, id, *args, **kwargs):
        return self.remove(req, id, *args, **kwargs)

    @expose
    def get_all(self, req, *args, **kwargs):
        return self.list(req, *args, **kwargs)

    @expose
    def get_one(self, req, id, *args, **kwargs):
        return self.show(req, id, *args, **kwargs)

    def create(self, req, *args, **kwargs):
        raise Exception('create')

    def update(self, req, id, *args, **kwargs):
        raise Exception('update')

    def remove(self, req, id, *args, **kwargs):
        raise Exception('remove')

    def list(self, req, *args, **kwargs):
        raise Exception('list')

    def show(self, req, id, *args, **kwargs):
        raise Exception('show')
