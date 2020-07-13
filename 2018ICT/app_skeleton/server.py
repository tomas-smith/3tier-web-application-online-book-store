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


#the main root page, contains links to all the manages
@route('/')
@view('index')
def index():
    return template('index')



#--------------------------------------------------


#main root for authors page
#displays the list of all authors via select a from a
@route('/author')
def all_authors():
    authors = select(a for a in Author)
    return template('author/index', authors = authors)

#when in the main page of authors, you can select from the list
#you can open a new window and see a more formated version of authors
@route('/author/<id>/')
def show_author(id):
	author = Author[id]
	return template('author/show_author', author = author)

#template to create a new author 
#sends variables to author/create 
@route('/author/new')
@view('/author/new_author')
def add_author_page():
	author = select(a for a in Author)
	return template('author/new_author', author = author)

#takes from author/new the variables and populates via request forms
#redirects back to author index
@route('/author/create', method ="POST")
def create_author():
	lastname = request.forms.get('lastname')
	firstname = request.forms.get('firstname')
	
	print(lastname, firstname)
	
	author = Author(lastname = lastname, firstname = firstname)
	redirect('/author')	
#template to take changes for author
#sends the changes to author/id/update	
@route('/author/<id>/edit')
def edit_author(id):
	author = Author[id]
	return template('author/edit', author=author)
	
#updates the author
#has forms for lastname and firstname	
@post('/author/<id>/update')
def update_author(id):

	author = Author[id]
	author.lastname = request.forms.get('lastname')
	author.firstname = request.forms.get('firstname')
	redirect('/author')

	
#deletes an author from the table
@route('/author/<id>/delete')
def delete_author(id):
	author = Author[id]
	author.delete()
	redirect('/author')

#allows to search for an author
#sends the pre-requisites to searchTitle
@route('/author/search')
@view('/author/search_author')
def search_author():
	return template('author/search_author')

#makes a search based on the input in author/search	
@route('/author/searchTitle', method='POST')
@view('author/search_results')
def search_title():
	lastname = request.forms.get('lastname')
	author = Author.select(lambda a: a.lastname ==lastname)
	return dict(author = author)

	
	
#--------------------------------------------------







#--------------------------------------------------	
#index page for publisher
#shows the list of publishers
@route('/publisher')
def all_publishers():
    publishers = select(p for p in Publisher)
    return template('publisher/index', publishers = publishers)
#shows in more detail publisher info	
@route('/publisher/<id>/')
def show_publisher(id):
	publisher = Publisher[id]
	return template('publisher/show_publisher', publisher = publisher)
#creates a new publisher
#sends info to the publisher/create	
@route('/publisher/new')
@view('/publisher/new_publisher')
def add_publisher_page():
	publisher = select(p for p	in Publisher)
	return template('publisher/new_publisher', publisher = publisher)
#creates a publisher from the input in publisher/new
#uses request form for name and country
#after its done creating it goes to the publisher index page
@route('/publisher/create', method ="POST")
def create_publisher():
	name = request.forms.get('name')
	country = request.forms.get('country')
	
	
	print(name, country)
	
	publisher = Publisher(name = name, country = country)
	redirect('/publisher')	
#allows to edit publishers name and country
#sends the changes to publisher/id/update	
@route('/publisher/<id>/edit')
def edit_publisher(id):
	publisher = Publisher[id]
	return template('publisher/edit', publisher = publisher)
	
#updates a publisher based on id from the input in publisher/id/edit	
@post('/publisher/<id>/update')
def update_publisher(id):

	publisher = Publisher[id]
	publisher.name = request.forms.get('name')
	publisher.country = request.forms.get('country')
	redirect('/publisher')

	
#deletes a publisher based on id
@route('/publisher/<id>/delete')
def delete_publisher(id):
	publisher = Publisher[id]
	publisher.delete()
	redirect('/publisher')
	
#makes a search for publisher, sends the requested search to SearchtTitle class	
@route('/publisher/search')
@view('/publisher/search_publisher')
def search_publisher():
	return template('publisher/search_publisher')
	
#takes the values from publisher/search and posts the results
#it searches via publisher name	
@route('/publisher/searchTitle', method = 'POST')
@view('publisher/search_results')
def search_title():

	name = request.forms.get('name')
	publisher= Publisher.select(lambda p: p.name == name)
	return dict(publisher = publisher)


	
#--------------------------------------------------	

#the main index page for the book section
@route('/book')
def all_books():
    books = select(b for b in Book)
    return template('book/index', books = books)
#allows to look in more detail 	of books
@route('/book/<id>/')
def show_book(id):
	book = book	[id]
	return template('book/show', book = book)
#creates a new book	
#takes values from author publisher and genre via .select, and then returns a dict
#the values are then taken via book/create
@route('/book/new')
@view('book/new_book')
def add_book_page():
	author = Author.select()
	publisher = Publisher.select()
	genre = Genre.select()
	
	return dict( author = author, publisher = publisher, genre = genre)
	
		
#takes the values from book/new and creates a new addition to the book table

@route('/book/create', method ="POST")
def create_book():
	title = request.forms.get('title')
	author = request.forms.get('author')
	publisher = request.forms.get('publisher')
	genre = request.forms.get('genre')
	year = request.forms.get('year')

	print(title, author, publisher, genre, year)
	
	book = Book (title=title, author=author, publisher=publisher, genre=genre, year=year)
	redirect('/book')
#edits a currently existing book
#has to take values from author publisher and genre tables via .select	
@route('/book/<id>/edit')
def edit_book(id):
	book = Book[id]
	author = Author.select()
	publisher = Publisher.select()
	genre = Genre.select()
	
	
	return dict( book=book, author= author, publisher = publisher, genre = genre)
#takes the values from book/edit and makes changes 	
#updates the book based on id aka PrimaryKey
#redirect to the main index of the book section
@route('/book/<id>/update')
def update_book(id):
	title = request.forms.get('title')
	author = request.forms.get('author')
	publisher = request.forms.get('publisher')
	genre = request.forms.get('genre')
	year = request.forms.get('year')	
	redirect('/book')
	
#deletes a book based on ID	
@route('/book/<id>/delete')
def delete_book(id):
	book = Book[id]
	book.delete()
	redirect('/book')
#searches a book via the title criteria	
@route('/book/search')
@view('/book/search_book')
def search_book():
	
	return template('book/search_book')
	
#takes the template of results and prints out the search
#uses lambda function to search via title, is case sensitive and 
@route('/book/searchTitle', method = 'POST')
@view('book/search_results')
def search_title():

	title = request.forms.get('title')
	book= Book.select(lambda b: b.title == title)
	return dict(book = book)
	 
	
#---------------------------------------------------------------------------------------------

#the main index for genre
@route('/genre')
def all_genres():
    genres = select(g for g in Genre)
    return template('genre/index', genres = genres)

#allows to see more in detail of genres	
@route('/genre/<id>/')
def show_genre(id):
	genre = Genre[id]
	return template('genre/show_genre', genre = genre)
#creates a new genre
	
@route('/genre/new')
@view('/genre/new_genre')
def add_genre_page():
	genre = select(g for g in Genre)
	return template('genre/new_genre', genre = genre)
#takes from genre/create and finalizes the creation
#formats the input from /create via request forms
@route('/genre/create', method ="POST")
def create_genre():
	genreName = request.forms.get('genreName')
	
	
	print(genreName)
	
	genre = Genre(genreName = genreName)
	redirect('/genre')	
#allows to edit genre
#more specifically, rename a name of the genre	
@route('/genre/<id>/edit')
def edit_genre(id):
	genre = Genre[id]
	return template('genre/edit', genre=genre)
	
#updates the genre
#takes values from genre/edit	
@post('/genre/<id>/update')
def update_genre(id):

	genre = Genre[id]
	genre.genreName = request.forms.get('genreName')
	
	redirect('/genre')
#deletes a genre
@route('/genre/<id>/delete')
def delete_genre(id):
	genre = Genre[id]
	genre.delete()
	redirect('/genre')
	
#takes values for a search of genre
#takes the name of the genre and parses to search_title
@route('/genre/search')
@view('/genre/search_genre')
def search_genre():
	return template('genre/search_genre')
#tales the values from search_genre def
#shows results	
@route('/genre/searchTitle', method='POST')
@view('genre/search_results')
def search_title():
	genreName = request.forms.get('genreName')
	genre = Genre.select(lambda g: g.genreName ==genreName)
	return dict(genre = genre)

#-------------------------------------------------------------------------------------
#main web page 
@route('/customer')
def all_customers():
    customers = select(c for c in Customer)
    return template('customer/index', customers = customers)
#allows to see more in detail of customers	
@route('/customer/<id>/')

def show_customer(id):
	customer = Customer[id]
	return template('customer/show_customer', customer = customer)
#creates a new customer
@route('/customer/new')
@view('/customer/new_customer')
def add_customer_page():
	customer = select(c for c in Customer)
	return template('customer/new_customer', customer = customer)
#takes from customer/create and finalizes the creation
#formats the input from /create via request forms
@route('/customer/create', method ="POST")
def create_customer():
	nameCustomer = request.forms.get('nameCustomer')
	lastname = request.forms.get('lastname')
	phone = request.forms.get('phone')
	address = request.forms.get('address')
	city = request.forms.get('city')
	country = request.forms.get('country')
	print(nameCustomer, lastname, phone, address, city, country)
	
	customer = Customer(nameCustomer = nameCustomer, lastname = lastname, phone = phone, address = address, city = city, country = country)
	redirect('/customer')	
#allows to edit customer
#more specifically, rename a name of the customer		
@route('/customer/<id>/edit')
def edit_customer(id):
	customer = Customer[id]
	return template('customer/edit', customer=customer)
	
#updates the customer
#takes values from customer/edit		
@post('/customer/<id>/update')
def update_customer(id):

	customer = Customer[id]
	
	
	
	
	
	redirect('/customer')	
#deletes a customer
@route('/customer/<id>/delete')
def delete_customer(id):
	customer = Customer[id]
	customer.delete()
	redirect('/customer')

#takes values for a search of genre
#takes the name of the genre and parses to search_title
@route('/customer/search')
@view('/customer/search_customer')
def search_genre():
	return template('customer/search_customer')
#tales the values from search_genre def
#shows results	
@route('/customer/searchTitle', method='POST')
@view('customer/search_results')
def search_title():
	lastname = request.forms.get('lastname')
	customer = Customer.select(lambda g: g.lastname ==lastname)
	return dict(customer = customer)
#-----------------------------------------------------------------------------

#the main index for order
@route('/order')
def all_orders():
    orders = select(o for o in Order)
    return template('order/index', orders = orders)
#allows to see more in detail of orders	
@route('/order/<id>/')

def show_order(id):
	order = order[id]
	return template('order/show_order', order = order)
#creates new order	
@route('/order/new')
@view('order/new_order')
def add_order_page():
	customer = Customer.select()
	book = Book.select()
	
	
	return dict(customer = customer, book = book)
	
#takes from order/create and finalizes the creation
#formats the input from /create via request forms

@route('/order/create', method ="POST")
def create_order():
	
	customer = request.forms.get('customer')
	books = request.forms.get('book')
	dop = request.forms.get('dop')

	
	order = Order( customer = customer,books = books, dop = dop)
	redirect('/order')	

#allows to edit order
#more specifically, rename a name of the order		
@route('/order/<id>/edit')
@view
def edit_order(id):
	order = Order[id]
	customer = Customer.select()
	book = Book.select()
	
	
	return dict(order= order, customer = customer, book = book)
	
#updates the order
#takes values from order/edit		
@post('/order/<id>/update')
def update_order(id):

	order = Order[id]
	order.customer = request.forms.get('customer')
	order.books = request.forms.get('books')
	order.dop = request.forms.get('dop')
	redirect('/order')
#deletes a order
@route('/order/<id>/delete')
def delete_order(id):
	order = Order[id]
	order.delete()
	redirect('/order')

#-------------------------------------------------------------------------------



#######################################################
### END route declaration
#######################################################

run(host='localhost', port=8080, debug=True, reloader=True)
