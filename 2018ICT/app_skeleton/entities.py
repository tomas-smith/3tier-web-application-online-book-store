import json
import config
from pony.orm import *

'''
The entity module contains all the entities of your application.
We will be using PonyORM; please, refer to http:ponyorm.com for more info.
'''

# instance of the class Database to create and map tables
db = Database()

#######################################################
### Begin entities declaration
#######################################################


#customer entity, contains the details for the cutstomer
#has a many to one relationship to Order entity in this assignment
#realistically should be One to many relationship with order, i.e one customer can have multiple orders 
class Customer(db.Entity):
	customer_id = PrimaryKey(int, auto=True)
	nameCustomer = Required(str)
	lastname = Required(str)
	phone = Required(str)
	address = Required(str)
	city = Required(str)
	country = Required(str)
	order = Set('Order')
#Order entity, contains the data from customer and book tables, whiles also keeping Date Of Purcase
#has one to many relationships with book and customer e.i. one order can have multiple customers and multiple books
#in a real life scenario it should have one customer - one order.
class Order(db.Entity):
	order_id=PrimaryKey(int, auto=True)
	customer= Required('Customer')
	books = Required('Book')
	dop = Required(str)
#Author entity, contains the information about the author's name and surname
# has a many to one relationship with books, since it common for a book to have multiple writers	
class Author(db.Entity):
	author_id=PrimaryKey(int, auto=True)
	lastname = Required(str)
	firstname = Required(str)
	book = Set('Book')
#publisher entity, contains name and country of the publisher
#has a many to one relationship with book, since multiple publishers can publish a book 
# i.e. dark horse comics publishes in USA, whiles in EU it could be a different publisher	
class Publisher(db.Entity):
	publisher_id=PrimaryKey(int, auto=True)
	name = Required(str)
	country = Required(str)
	book = Set('Book')
#genre entity, contains the title of a genre
# has a many to one relationship with book e.g. a book can be too complex to fall under one category
class Genre(db.Entity):
	Genre_id=PrimaryKey(int, auto=True)
	genreName = Required(str)
	book = Set('Book')
#book entity, contains all the details about the book and possible orders
#has a one to many relationship with author publisher and genre 
#has a many to one relationship with order, since many books can go to one order
class Book(db.Entity):
	book_id = PrimaryKey(int, auto=True)
	title = Required(str)
	author = Required('Author')
	publisher = Required('Publisher')
	genre = Required('Genre')
	year = Required(str)
	order = Set('Order')




#######################################################
### END entities declaration
#######################################################

#######################################################
### The following 2 instructions bind the db to the
### SQLite file and generate the tables if needed.
#######################################################
# binding the entities to an sqlite database
db.bind('sqlite', config.DB_FILE_NAME, create_db=True)

# create the tables
db.generate_mapping(create_tables=True)
