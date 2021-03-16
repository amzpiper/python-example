from pecan import expose, redirect
from webob.exc import status_map

class BooksController(object):
    @expose()
    def index(self):
        return "Welcome to book section."
    
    @expose()
    def bestsellers(self):
        return "We have 5 books in the top 10."


class CatalogController(object):
    @expose()
    def index(self):
        return "Welcome to the catalog."

    books = BooksController()


class RootController(object):

    @expose(generic=True, template='index.html')
    def index(self):
        return dict()
    

    @index.when(method='POST')
    def index_post(self, q):
        redirect('https://pecan.readthedocs.io/en/latest/search.html?q=%s' % q)

    @expose('error.html')
    def error(self, status):
        try:
            status = int(status)
        except ValueError:  # pragma: no cover
            status = 500
        message = getattr(status_map.get(status), 'explanation', '')
        return dict(status=status, message=message)

    @expose()
    def hours(self):
        return "Open 24/7 on the web"

    catalog = CatalogController()
    