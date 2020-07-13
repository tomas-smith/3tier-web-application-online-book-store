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

class Book(db.Entity):
    title = Required(str)
    artist = Required(str)
    year = Required(str)
    genre = Set('Genre')
'''
class Book(db.Entity):
	title = Required(str)
	author = Set('Author')
	publisher = Set('Publisher')
	genre = Set('Genre')
	year = Required(str)
	order = Set('Order')
'''
class Author(db.Entity):
	firstname = Required(str)
	lastname = Required(str)
	book = Set('Book')
	
class Publisher(db.Entity):
	name = Required(str)
	country = Required(str)
	book = Set('Book')

class Genre(db.Entity):
	name = Required(str)
	book = Set('Book')

class Customer(db.Entity):
	name = Required(str)
	lastname = Required(str)
	phone = Required(str)
	address = Required(str)
	city = Required(str)
	country = Required(str)
	order = Set('Order')
	
class Order(db.Entity):
	customer= Set('Customer')
	books = Set('Book')
	dop = Required(str)

'''
class Genre(db.Entity):
    name = Required(str)
    vinyl = Set('Vinyl')
 '''   

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

