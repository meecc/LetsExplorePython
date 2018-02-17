
# SQLAlchemy DBAPI Suppport Examples: Code Samples

Most of the below code is copied/inspired from https://www.pythonsheets.com/notes/python-sqlalchemy.html

## Sqlalchemy Support DBAPI - PEP249


```python
def create_db():
    import os 

    DB_FILE = "db.sqlite"
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
    db_uri = "sqlite:///" + DB_FILE
    return create_engine(db_uri)
```


```python
from sqlalchemy import create_engine

engine = create_db()
# DBAPI - PEP249
# create table
engine.execute('CREATE TABLE "EX1" ('
               'id INTEGER NOT NULL,'
               'name VARCHAR, '
               'PRIMARY KEY (id));')
# insert a raw
engine.execute('INSERT INTO "EX1" '
               '(id, name) '
               'VALUES (1,"raw1")')

# select *
result = engine.execute('SELECT * FROM '
                        '"EX1"')
for _r in result:
    print(_r)

# delete *
engine.execute('DELETE from "EX1" where id=1;')
result = engine.execute('SELECT * FROM "EX1"')
print (result.fetchall())
```

    (1, u'raw1')
    []


## Metadata - Generating Database Schema


```python
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String

engine = create_db()

# Create a metadata instance
metadata = MetaData(engine)
# Declare a table
table = Table('Example',metadata,
              Column('id',Integer, primary_key=True),
              Column('name',String))
# Create all tables
metadata.create_all()
for _t in metadata.tables:
    print ("Table: ", _t)
```

    ('Table: ', 'Example')


## Inspect - Get Database Information


```python
from sqlalchemy import create_engine
from sqlalchemy import inspect

engine = create_db()

inspector = inspect(engine)

# Get table information
print inspector.get_table_names()

# Get column information
print inspector.get_columns('EX1')
```

    [u'EX1', u'Example']
    [{'primary_key': 1, 'nullable': False, 'default': None, 'autoincrement': 'auto', 'type': INTEGER(), 'name': u'id'}, {'primary_key': 0, 'nullable': True, 'default': None, 'autoincrement': 'auto', 'type': VARCHAR(), 'name': u'name'}]


## Reflection - Loading Table from Existing Database


```python
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table

engine = create_db()

# Create a MetaData instance
metadata = MetaData()
print metadata.tables

# reflect db schema to MetaData
metadata.reflect(bind=engine)
print metadata.tables
```

    immutabledict({})
    immutabledict({u'Example': Table('Example', MetaData(bind=None), Column('id', INTEGER(), table=<Example>, primary_key=True, nullable=False), Column('name', VARCHAR(), table=<Example>), schema=None), u'EX1': Table('EX1', MetaData(bind=None), Column('id', INTEGER(), table=<EX1>, primary_key=True, nullable=False), Column('name', VARCHAR(), table=<EX1>), schema=None)})


## Create all Tables Store in “MetaData”


```python
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String

engine = create_db()
meta = MetaData(engine)

# Register t1, t2 to metadata
t1 = Table('EX1', meta,
           Column('id',Integer, primary_key=True),
           Column('name',String))

t2 = Table('EX2', meta,
           Column('id',Integer, primary_key=True),
           Column('val',Integer))
# Create all tables in meta
meta.create_all()
```

## Create Specific Table


```python
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String

engine = create_db()

meta = MetaData(engine)
t1 = Table('Table_1', meta,
           Column('id', Integer, primary_key=True),
           Column('name',String))
t2 = Table('Table_2', meta,
           Column('id', Integer, primary_key=True),
           Column('val',Integer))
t1.create()
```

## Drop a Table


```python
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import inspect
from sqlalchemy import Table
from sqlalchemy import Column, Integer, String
from sqlalchemy.engine.url import URL

engine = create_db()
m = MetaData()
table = Table('Test', m,
              Column('id', Integer, primary_key=True),
              Column('key', String, nullable=True),
              Column('val', String))

table.create(engine)
inspector = inspect(engine)
print ('Test' in inspector.get_table_names())

table.drop(engine)
inspector = inspect(engine)
print ('Test' in inspector.get_table_names())
```

    True
    False


## SQL Expression Language


```python
# Think Column as "ColumnElement"
# Implement via overwrite special function
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy import or_

meta = MetaData()
table = Table('example', meta,
              Column('id', Integer, primary_key=True),
              Column('l_name', String),
              Column('f_name', String))
# sql expression binary object
print repr(table.c.l_name == 'ed')
# exhbit sql expression
print str(table.c.l_name == 'ed')

print repr(table.c.f_name != 'ed')

# comparison operator
print repr(table.c.id > 3)

# or expression
print (table.c.id > 5) | (table.c.id < 2)
# Equal to
print or_(table.c.id > 5, table.c.id < 2)

# compare to None produce IS NULL
print (table.c.l_name == None)
# Equal to
print (table.c.l_name.is_(None))

# + means "addition"
print (table.c.id + 5)
# or means "string concatenation"
print (table.c.l_name + "some name")

# in expression
print (table.c.l_name.in_(['a','b']))
```

    <sqlalchemy.sql.elements.BinaryExpression object at 0x7f766c0eb790>
    example.l_name = :l_name_1
    <sqlalchemy.sql.elements.BinaryExpression object at 0x7f766c0eb790>
    <sqlalchemy.sql.elements.BinaryExpression object at 0x7f766c0eb8d0>
    example.id > :id_1 OR example.id < :id_2
    example.id > :id_1 OR example.id < :id_2
    example.l_name IS NULL
    example.l_name IS NULL
    example.id + :id_1
    example.l_name || :l_name_1
    example.l_name IN (:l_name_1, :l_name_2)


## insert() - Create an “INSERT” Statement


```python
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

engine = create_db()

# create table
meta = MetaData(engine)
table = Table('user', meta,
   Column('id', Integer, primary_key=True),
   Column('l_name', String),
   Column('f_name', String))
meta.create_all()

# insert data via insert() construct
ins = table.insert().values(
      l_name='Hello',
      f_name='World')
conn = engine.connect()
conn.execute(ins)

# insert multiple data
conn.execute(table.insert(),[
   {'l_name':'Hi','f_name':'bob'},
   {'l_name':'yo','f_name':'alice'}])
```




    <sqlalchemy.engine.result.ResultProxy at 0x7ff176de8dd0>



## Delete Rows from Table


```python
from sqlalchemy import create_engine
from sqlalchemy import MetaData

# engine = create_db()
conn = engine.connect()

meta = MetaData(engine)
user_t = meta.tables['user']

# select * from user_t
sel_st = user_t.select()
res = conn.execute(sel_st)
for _row in res: print (_row)

# delete l_name == 'Hello'
del_st = user_t.delete().where(
      user_t.c.l_name == 'Hello')
print '----- delete -----'
res = conn.execute(del_st)

# check rows has been delete
sel_st = user_t.select()
res = conn.execute(sel_st)
for _row in res: print (_row)
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-20-a9593c1a0e78> in <module>()
          6 
          7 meta = MetaData(engine)
    ----> 8 user_t = meta.tables['user']
          9 
         10 # select * from user_t


    KeyError: 'user'

