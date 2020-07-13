from config import *
from bottle import *
from entities import *
from pony.orm.integration.bottle_plugin import PonyPlugin
install(PonyPlugin())

'''
    Server module
    =============
    This module provides all the basic functionalities of the application.
    The module is a standard Bottle application and runs on port 8080.
'''

#######################################################
### Begin route declaration
#######################################################

@route('/')
@view('index')
def index():
    books = book.select()
    return dict(books = books)

@route('/books/new')
@view('new_book')
def new_book():
    genres = Genre.select()
    return dict(genre = genres)

@route('/books/<id>/')
@view('show_book')
def show_book(id):
    book = book[id]
    return dict(book = book)

@route('/books/create', method="POST")
def create_book():
    title = request.forms.get('title')
    artist = request.forms.get('artist')
    year = request.forms.get('year')
    genre = request.forms.get('genre')

    print(title, artist, year, genre)

    book = book(title = title, artist = artist, year = year, genre = genre)

    redirect('/')

@route('/books/<id>/edit')
@view('edit_book')
def show_book(id):
    book = book[id]
    genre = Genre.select()
    return dict(book = book, genre = genre)

@post('/books/<id>/update')
def update_book(id):
    book = book[id]
    book.title = request.forms.get('title')
    book.artist = request.forms.get('artist')
    book.year = request.forms.get('year')
    book.genre = request.forms.get('genre')
    redirect('/')

@route('/books/search')
@view('search_book')
def search_book():
    return template('search_book')

@route('/books/searchTitle', method="POST")
@view('search_results')
def search_title():
    title = request.forms.get('title')
    book = book.select(lambda p: p.title == title)
    return dict(books = book)

@route('/books/<id>/delete')
def delete_book(id):
    book = book[id]
    book.delete()
    redirect('/')

#######################################################
### END route declaration
#######################################################

run(host='localhost', port=8080, debug=True, reloader=True)
