
# Databases
----

There are many ways one can access 


## DB-API
---
The Python Database API (DB-API) defines a standard interface for Python database access modules. It’s documented in PEP 249 https://www.python.org/dev/peps/pep-0249/. Nearly all Python database modules such as sqlite3, psycopg and mysql-python conform to this interface.

### Example


```python
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 07:37:10 2016

@author: mayank johri
"""

try:
    from sqlite3 import dbapi2 as sqlite
except ImportError:
    from pysqlite2 import dbapi2 as sqlite

import os 

DB_FILE = 'db/comment.sqlite3'
    
def createDB():
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)    
    db_conn = sqlite.connect(DB_FILE)
        
    db_curs = db_conn.cursor()
    db_curs.execute("""CREATE TABLE people (
                    id INTEGER PRIMARY KEY, first_name VARCHAR(20),
                    last_name VARCHAR(30), date_of_birth DATE)""")
    
    db_curs.execute("""INSERT INTO people (first_name, last_name, date_of_birth)
                         VALUES ('Mayank', 'Johri', '1976-7-10')""")
    db_curs.close()
    return db_conn

def getData(db_conn):
    db_cur = db_conn.cursor()
    sql = "select first_name, last_name, date_of_birth from people"
    db_cur.execute(sql)
    data = db_cur.fetchall()
    db_cur.close()
    return data

def getAllData(db_conn):
    db_cur = db_conn.cursor()
    sql = "select first_name, last_name, date_of_birth from people"
    db_cur.execute(sql)
    data = db_cur.fetchall()
    db_cur.close()
    return data
    

def setUser(db_conn, first_name, last_name, date_of_birth):
    stmt = """INSERT INTO people (first_name, 
                                  last_name, 
                                  date_of_birth) VALUES (?,?,?)"""
    db_cur = db_conn.cursor()
    db_cur.execute(stmt, (first_name, last_name, date_of_birth))
    
def rollback(db_conn):
    pass

def commit(db_conn):
    db_conn.commit()
    
if __name__ == "__main__":
    db_conn = None
    try:
      db_conn = createDB()
      setUser(db_conn, "Subhas", "Chandra Bose", "January 23, 1897")
      setUser(db_conn, "Bhagat", "Singh", "September 28, 1907")      
      data = getAllData(db_conn)
      print(type(data))
      for d in data:
          print("{0} {1} was born in {2}".format(d[0], d[1], d[2]))
    except:
      rollback(db_conn)
      raise 
    else:
      commit(db_conn)
    finally:
        if db_conn != None:
            db_conn.close()
```

    <class 'list'>
    Mayank Johri was born in 1976-7-10
    Subhas Chandra Bose was born in January 23, 1897
    Bhagat Singh was born in September 28, 1907



```python
try:
    from sqlite3 import dbapi2 as sqlite
except ImportError:
    from pysqlite2 import dbapi2 as sqlite

DB_FILE = 'db/comment.sqlite3'


```

## SQLAlchemy
---
SQLAlchemy is a commonly used database toolkit. Unlike many database libraries it not only provides an ORM (Object-relational mapping) layer but also a generalized API for writing database-agnostic code without SQL.
> $ pip install sqlalchemy

### Example


```python
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# engine.dispose()
engine = create_engine('sqlite:///userlist.db', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

session_dec = Session()

ed_user = User(name='Meenu', fullname='Meenakshi Johri', password='meenuInIndia')
print(ed_user)
session.add(ed_user)
print("Ued_user.id")
session.add(User(name='GV',fullname='GV', password='gv@ibm'))
session.flush()
print(ed_user.id)

#Now let’s commit the changes:
session.commit()

# #SQLAlchemy sends the COMMIT statement that permanently commits the flushed changes and ends the transaction.

# # Delete
# #To delete the test_page object from the database you would use:
session.delete(ed_user)
session.flush()
# #At this point you can either commit the transaction or do a rollback. Let’s do a rollback this time:
session.commit()
session.close()
engine.dispose()
```

    2017-10-05 19:32:29,759 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
    2017-10-05 19:32:29,766 INFO sqlalchemy.engine.base.Engine ()
    2017-10-05 19:32:29,767 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
    2017-10-05 19:32:29,768 INFO sqlalchemy.engine.base.Engine ()
    2017-10-05 19:32:29,771 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("users")
    2017-10-05 19:32:29,773 INFO sqlalchemy.engine.base.Engine ()
    <User(name='Meenu', fullname='Meenakshi Johri', password='meenuInIndia')>
    Ued_user.id
    2017-10-05 19:32:29,779 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
    2017-10-05 19:32:29,781 INFO sqlalchemy.engine.base.Engine INSERT INTO users (name, fullname, password) VALUES (?, ?, ?)
    2017-10-05 19:32:29,782 INFO sqlalchemy.engine.base.Engine ('Meenu', 'Meenakshi Johri', 'meenuInIndia')
    2017-10-05 19:32:29,785 INFO sqlalchemy.engine.base.Engine INSERT INTO users (name, fullname, password) VALUES (?, ?, ?)
    2017-10-05 19:32:29,786 INFO sqlalchemy.engine.base.Engine ('GV', 'GV', 'gv@ibm')
    5
    2017-10-05 19:32:29,790 INFO sqlalchemy.engine.base.Engine COMMIT
    2017-10-05 19:32:29,801 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
    2017-10-05 19:32:29,811 INFO sqlalchemy.engine.base.Engine SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname, users.password AS users_password 
    FROM users 
    WHERE users.id = ?
    2017-10-05 19:32:29,812 INFO sqlalchemy.engine.base.Engine (5,)
    2017-10-05 19:32:29,814 INFO sqlalchemy.engine.base.Engine DELETE FROM users WHERE users.id = ?
    2017-10-05 19:32:29,819 INFO sqlalchemy.engine.base.Engine (5,)
    2017-10-05 19:32:29,823 INFO sqlalchemy.engine.base.Engine COMMIT



```python
# from sqlalchemy import create_engine, ForeignKey
# from sqlalchemy import Column, Date, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship

# # engine.dispose()
# engine = create_engine('sqlite:///userlist.db', echo=True)
# Base = declarative_base()


# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
    
#     def __repr__(self):
#         return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

    
# class Address(Base):
#     __tablename__ = 'address'
    
#     address_id = Column(Integer, primary_key=True)
#     house_name = Column(String)
#     house_no = Column(String)
#     city = Column(String)
#     user_id = Column(Integer, ForeignKey('User.id'))


# Base.metadata.create_all(engine)
```


```python
# from sqlalchemy.orm import sessionmaker
# Session = sessionmaker(bind=engine)
# session = Session()

# session_dec = Session()

# ed_user = User(name='Meenu', fullname='Meenakshi Johri', password='meenuInIndia')
# # ed_user.address = Address(house_no="20", house_name="Raj Ghar", city= "Jaipur")

# session.commit()
# session.close()
# engine.dispose()
```

## Records

Records is minimalist SQL library, designed for sending raw SQL queries to various databases. Data can be used programmatically, or exported to a number of useful data formats.

> $ pip install records

Also included is a command-line tool for exporting SQL data.


```python
import json # https://docs.python.org/3/library/json.html
import requests # https://github.com/kennethreitz/requests
import records # https://github.com/kennethreitz/records

# randomuser.me generates random 'user' data (name, email, addr, phone number, etc)
r = requests.get('http://api.randomuser.me/0.6/?nat=us&results=3')
j = r.json()['results']

# Valid SQLite URL forms are:
#   sqlite:///:memory: (or, sqlite://)
#   sqlite:///relative/path/to/file.db
#   sqlite:////absolute/path/to/file.db

# records will create this db on disk if 'users.db' doesn't exist already
db = records.Database('sqlite:///users.db')

db.query('DROP TABLE IF EXISTS persons')
db.query('CREATE TABLE persons (key int PRIMARY KEY, fname text, lname text, email text)')

for rec in j:
    user = rec['user']
    name = user['name']

    key = user['registered']
    fname = name['first']
    lname = name['last']
    email = user['email']
    db.query('INSERT INTO persons (key, fname, lname, email) VALUES(:key, :fname, :lname, :email)',
            key=key, fname=fname, lname=lname, email=email)

rows = db.query('SELECT * FROM persons')
print(rows.export('csv'))
```

    key,fname,lname,email
    1204253136,melissa,hughes,melissa.hughes80@example.com
    1269157646,brennan,henry,brennan.henry46@example.com
    930355634,enrique,holland,enrique.holland66@example.com
    


## SQLObject
--------
SQLObject is yet another ORM. It supports a wide variety of databases: Common database systems MySQL, Postgres and SQLite and more exotic systems like SAP DB, SyBase and MSSQL.

SQLObject is a popular Object Relational Manager for providing an object interface to your database, with tables as classes, rows as instances, and columns as attributes.

SQLObject includes a Python-object-based query language that makes SQL more abstract, and provides substantial database independence for applications.


```python
import sqlobject
from sqlobject.sqlite import builder
conn = builder()('sqlobject_demo.db')

 
class PhoneNumber(sqlobject.SQLObject):
    _connection = conn
    number = sqlobject.StringCol(length=14, unique=True)
    owner = sqlobject.StringCol(length=255)
    lastCall = sqlobject.DateTimeCol(default=None)
    
PhoneNumber.createTable(ifNotExists=True)

myPhone = PhoneNumber(number='(415) 555-1212', 
                      owner='Leonard Richardson')

```


```python
# Running code with partial information will result in error 
duplicatePhone = PhoneNumber(number="(415) 555-1212")
```


```python
duplicatePhone = PhoneNumber(number="(415) 555-1212")
```

### Defining relationships among tables

SQLObject lets you define relationships among tables as foreign keys


```python
import sqlobject
from sqlobject.sqlite import builder
conn = builder()('sqlobject_demo_relationships.db')
 
 
class PhoneNumber(sqlobject.SQLObject):
    _connection = conn
    number = sqlobject.StringCol(length=14, unique=True)
    owner = sqlobject.ForeignKey('Person')
    lastCall = sqlobject.DateTimeCol(default=None)
 
 
class Person(sqlobject.SQLObject):
    _idName='fooID'
    _connection = conn
    name = sqlobject.StringCol(length=255)
    #The SQLObject-defined name for the "owner" field of PhoneNumber
    #is "owner_id" since it's a reference to another table's primary
    #key.
    numbers = sqlobject.MultipleJoin('PhoneNumber', joinColumn='owner_id')
Person.createTable(ifNotExists=True)
PhoneNumber.createTable(ifNotExists=True)

```


```python
person = Person(name='Vinay')
p = PhoneNumber(number="2222", owner=person)
```
