
# SQLAlchemy - Relationships - Code Samples

## One to many relationships


```python
class Book(Base):
    __tablename__  = "books"    # matches the name of the actual database table
    id             = Column(Integer, primary_key=True) 
    name           = Column(String(50))                                    
    author_id      = Column(Integer,ForeignKey('authors.id'))   # Why ???? Ask question
    # The backref will create references on both tables. 
    author = relationship("Author",backref="books")             # <-----------------------
    
class Author(Base):
    __tablename__  = "books"    # matches the name of the actual database table
    id             = Column(Integer, primary_key=True) 
    name           = Column(String(50))
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-1-9a5cb785ff3d> in <module>()
    ----> 1 class Book(Base):
          2     __tablename__  = "books"    #matches the name of the actual database table
          3     id             = Column(Integer,Sequence('book_seq'),primary_key=True)
          4     name           = Column(String(50))
          5     author_id      = Column(Integer,ForeignKey('authors.id'))


    NameError: name 'Base' is not defined


## One to one relationships


```python
class Parent(Base):
    __tablename__ = 'parent'
    id = ColumnColumn(Integer,Sequence('p_seq'),primary_key=True) 
    child_id = Column(Integer, ForeignKey('child.id'))
    # uselist comes to your help
    child = relationship("Child", backref=backref("parent", uselist=False)) 

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer,Sequence('c_seq'),primary_key=True) 
```

### what is uselist 

## Many to many relationships


```python
class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer,Sequence('cat_seq'),primary_key=True) 
    name = Column(String(20))

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer,Sequence('prod_seq'),primary_key=True) 
    name = Column(String(20))
    
class Map(Base):
    __tablename__ = 'map'
    id = Column(Integer,Sequence('map_seq'),primary_key=True) 
    cat_id = Column(Integer,ForeignKey('categories.id'))
    prod_id = Column(Integer,ForeignKey('products.id'))
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-2-0d7ab09aac76> in <module>()
    ----> 1 class Category(Base):
          2     __tablename__ = 'categories'
          3     id = Column(Integer,Sequence('cat_seq'),primary_key=True)
          4     name = Column(String(20))
          5 


    NameError: name 'Base' is not defined

