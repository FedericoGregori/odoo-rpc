# Try it by editing the library.py file,
# changing
# from library_api import LibraryAPI
# ->
# from library_odoorpc import LibraryAPI

# Now test drive the library.py client application, and it should perform the same.

from odoorpc import ODOO

class LibraryAPI:

    def __init__(self, srv, port, db, user, pwd):
        self.api = ODOO(srv, port=port)
        self.api.login(db, user, pwd)
        self.uid = self.api.env.uid
        self.model = 'library.book'
        self.Model = self.api.env[self.model]

    def execute(self, method, arg_list, kwarg_dict=None):
        return self.api.execute(
            self.model,
            method,
            *arg_list,
            **kwarg_dict
        )

    def search_read(self, text=None):
        domain = [('name', 'ilike', text)] if text else []
        fields = ['id', 'name']
        return self.Model.search_read(domain, fields)

    def create(self, title):
        vals = {'name': title}
        return self.Model.create(vals)

    def write(self, title, id_book):
        vals = {'name': title}
        self.Model.write(id_book, vals)

    def unlink(self, id_book):
        return self.Model.unlink(id_book)

