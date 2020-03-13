from argparse import ArgumentParser
from library_api import LibraryAPI


parser = ArgumentParser()
parser.add_argument(
    'command',
    choices=['list', 'add', 'set-title', 'del'])
parser.add_argument('params', nargs='*')  # optional args
args = parser.parse_args()

srv, port, db = 'localhost', 8069, 'odoo-12-dev-essentials-library'
user, pwd = 'admin', 'admin'
api = LibraryAPI(srv, port, db, user, pwd)

if args.command == 'list':
    books = api.search_read(args.params)
    for book in books:
        print('%(id)d %(name)s' % book)

if args.command == 'add':
    for title in args.params:
        new_id = api.create(title)
        print('Book added with ID %d.' % new_id)

if args.command == 'set-title':
    if len(args.params) != 2:
        print("set command requires a Title and ID.")
    book_id, title = int(args.params[0]), args.params[1]
    api.write(title, book_id)
    print('Title set for Book ID %d.' % book_id)

if args.command == 'del':
    for param in args.params:
        api.unlink(int(param))
        print('Book with ID %s deleted.' % param)

