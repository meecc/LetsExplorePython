
# Modules, Classes, and Objects & OOPS
----
Python is something called an “object- oriented programming language.” What this means is
there’s a construct in Python called a class that lets you structure your software in a particular
way. Using classes, you can add consistency to your programs so that they can be used in a cleaner
way, or at least that’s the theory.

Classes and objects are the two main aspects of object oriented programming. A class creates a new type where objects are instances of the class. An analogy is that you can have variables of type i n t which translates to saying that variables that store integers are variables which are instances (objects) of the int class.

Objects can store data using ordinary variables that belong to the object. Variables that
belong to an object or class are referred to as fields. Objects can also have functionality by
using functions that belong to a class. Such functions are called methods of the class. This
terminology is important because it helps us to differentiate between functions and
variables which are independent and those which belong to a class or object. Collectively,
the fields and methods can be referred to as the attributes of that class.

Fields are of two types - they can belong to each instance/object of the class or they can
belong to the class itself. They are called instance variables and class variables
respectively.

A class is created using the ***`class`*** keyword. The fields and methods of the class are listed
in an indented block.

## The self

Class methods have only one specific difference from ordinary functions - they must have an extra first name that has to be added to the beginning of the parameter list, but you do not give a value for this parameter when you call the method, Python will provide it. This particular variable refers to the object itself, and by convention, it is given the name ***`self`***.

## Classes
---
A class is merely a container for static data members or function declarations, called a class's attributes. Classes provide something which can be considered a blueprint for creating "real" objects, called class instances. Functions which are part of classes are called ***`methods`***.

The simplest class possible is shown in the following example.


```python
# Declare a Class
class class_name(object):
    pass
```


```python
class Class_name(base_classes_if_any):
    """optional documentation string"""

    static_member_declarations = 1
    
    def method_declarations(self):
        pass
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-ff0ccfbdd8d2> in <module>()
    ----> 1 class Class_name(base_classes_if_any):
          2     """optional documentation string"""
          3 
          4     static_member_declarations = 1
          5 


    NameError: name 'base_classes_if_any' is not defined



```python
# first.py

class First:
   pass

fr = First()
print (type(fr))
print (type(First))
print(type(int))
```

    <class '__main__.First'>
    <class 'type'>
    <class 'type'>



```python
# first.py

class First(object):
   pass

fr = First()
print (type(fr))
print (type(First))
print(type(int))
```

    <class '__main__.First'>
    <class 'type'>
    <class 'type'>



```python
# first.py
# Class with it's methods  

class Second:
    def set_name(self, name):
        self.fullname = name
        
    def get_name(self):
        return self.fullname

sec = Second()
print(sec.get_name())
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-8-326a847a64c0> in <module>()
         10 
         11 sec = Second()
    ---> 12 print(sec.get_name())
    

    <ipython-input-8-326a847a64c0> in get_name(self)
          7 
          8     def get_name(self):
    ----> 9         return self.fullname
         10 
         11 sec = Second()


    AttributeError: 'Second' object has no attribute 'fullname'



```python
# first.py

class Second:
    def set_name(self, name):
        self.fullname = name
        
    def get_name(self):
        return self.fullname

sec = Second()
sec.set_name("Manish Gupta")
print(sec.get_name())
```

    Manish Gupta



```python
# first.py

class Second:
    def set_name(self, name):
        self.fullname = name
        
    def get_name(self):
        return self.fullname

sec = Second()
sec2 = Second()

print(dir(sec))
print("^"*20)
sec.set_name("Manish")
print(sec.get_name())
print("~"*20)
print(sec2.get_name())
```

    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'get_name', 'set_name']
    ^^^^^^^^^^^^^^^^^^^^
    Manish
    ~~~~~~~~~~~~~~~~~~~~



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-13-5125b4dda67b> in <module>()
         16 print(sec.get_name())
         17 print("~"*20)
    ---> 18 print(sec2.get_name())
    

    <ipython-input-13-5125b4dda67b> in get_name(self)
          6 
          7     def get_name(self):
    ----> 8         return self.fullname
          9 
         10 sec = Second()


    AttributeError: 'Second' object has no attribute 'fullname'



```python
# first.py

class Second:
    def __init__(self, name, age=35):
        self.name(name)
        self.age = age
        
    def name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name

sec = Second("Arya")
print(sec.get_name())
print(sec.age)
```

    Arya
    35



```python
class Second:
    def __init__(self, name, age=55):
        self.name(name)
        self.age = age
        
    def name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name

sec = Second("Rajneekanth")
print(sec.get_name())
print(sec.age)
```

    Rajneekanth
    55



```python
# first.py

class Second:
    fullname = "Mayank Johri"
    age = 33
        
    def name(self, name):
        self.fullname = name
        
    def get_name(self):
        return self.fullname

sec = Second()
print(dir(sec))
print(sec.get_name())
print(id(sec.fullname))
sec2 = Second()
print(id(sec2.fullname))

```

    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'fullname', 'get_name', 'name']
    Mayank Johri
    83953904
    83953904



```python
# first.py

class Second:
    fullname = "Mayank Johri"
    age = 33
        
    def name(self, name):
        self.fullname = name
        
    def get_name(self):
        return self.fullname

sec = Second()
print(sec.get_name())
print(id(sec.fullname))
sec2 = Second()
print(id(sec2.fullname))
sec2.name("Roshan")
print(id(sec2.fullname))
print(id(sec.fullname))
print(sec.fullname)
sec.name("Roshan")
print(id(sec2.fullname))
print(id(sec.fullname))
name = "Roshan"
print(id(name))
```

    Mayank Johri
    140698168231784
    140698168231784
    140698168761536
    140698168231784
    Mayank Johri
    140698168761536
    140698168761536
    140698168761536



```python
# Example
class FooClass:
    """my very first class: FooClass"""
    __version = 0.11 # class (data) attribute
    ver = 0.1
    
    def __init__(self, nm='John Doe'):
        'constructor'
        self.name = nm # class instance (data) attribute
    
    def showName(self):
        'display instance attribute and class name'
        print ('Your name is: ', self.name)
#         print( 'My name is: ', self.__class__ )# full class name

    def showVersion(self):
        'display class(static) attribute'
        print( self.__version )# references FooClass.version
    
    def showVer(self):
        'display class(static) attribute'
        print( self.ver )# references FooClass.version 
    
    def setVersion(self, ver):
        'display class(static) attribute'
        self.__version = ver
        print( self.__version )# references FooClass.version  

# Create Class Instances
foo = FooClass()
arya = FooClass("Arya")
arya.showName()
```

    Your name is:  Arya



```python
# Calling class methods
foo.showName()
# print(foo.showName())
foo.showVer()
print(foo.ver)
foo.setVersion(10)
foo.ver = 2020202
```

    Your name is:  John Doe
    0.1
    0.1
    10



```python
foo.name
```




    'John Doe'




```python
foo.name = "Anamika Johri"
foo.name
```




    'Anamika Johri'




```python
foo.showVer()
print(foo.ver)
print("-"*20)
print(arya.showVer())

# print(FooClass.__version)
```


```python
print(foo.__version)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-26-e91d1af69f53> in <module>()
    ----> 1 print(foo.__version)
    

    AttributeError: 'FooClass' object has no attribute '__version'



```python
# Example
class User:
    """my very first class: FooClass"""
    __version = 0.11 # class (data) attribute
    ver = 0.1
    
    def __init__(self, firstname='John', surname="Doe"):
        'constructor'
        self.name = firstname + " " + surname 
        print ('Created a class instance for: ', self.name)
    
    def showName(self):
        'display instance attribute and class name'
        print ('Your name is: ', self.name)
        print( 'My name is: ', self.__class__ )# full class name

    def showVersion(self):
        'display class(static) attribute'
        print( self.__version )# references FooClass.version
    
    def showVer(self):
        'display class(static) attribute'
        print( self.ver )# references FooClass.version 
    
    def setVersion(self, ver):
        'display class(static) attribute'
        self.__version = ver
        print( self.__version )# references FooClass.version  

# Create Class Instances
user = User()
arya = User("Arya")
gupta = User(surname="Gupta")
print(arya.showName())
```

    Created a class instance for:  John Doe
    Created a class instance for:  Arya Doe
    Created a class instance for:  John Gupta
    Your name is:  Arya Doe
    My name is:  <class '__main__.User'>
    None



```python
# Example
class User:
    """my very first class: FooClass"""
    __version = 0.11 # class (data) attribute
    ver = 0.1
    
    def __init__(self, firstname, surname):
        'constructor'
        self.name = firstname + " " + surname 
        print ('Created a class instance for: ', self.name)
    
    # full class name
    def showName(self):
        'display instance attribute and class name'
        print ('Your name is: ', self.name)
        print( 'My name is: ', self.__class__ )

    def showVersion(self):
        'display class(static) attribute'
        print( self.__version )# references FooClass.version
    
    def showVer(self):
        'display class(static) attribute'
        print( self.ver )# references FooClass.version 
    
    def setVersion(self, ver):
        'display class(static) attribute'
        self.__version = ver
        print( self.__version )# references FooClass.version  

# Create Class Instances
# user = User()
# arya = User("Arya")
# gupta = User(surname="Gupta")
gupta = User(surname="Gupta", firstname="Manish")
arya.showName()
```

    ('Created a class instance for: ', 'Manish Gupta')
    ('Your name is: ', 'Arya')



```python
class PrivateVariables():
    __version = 1.0
    _vers = 11.0
    ver = 10.0
    
    def show_version(self):
        return(self.__version)
    
    def show_vers(self):
        print(self._vers)

pv = PrivateVariables()
print(pv.ver)
print(pv._vers)
# print(pv.__version)

pv.ver = 111
print(pv.ver)
pv._vers = 1000
print(pv._vers) # Convension only 
print(pv.show_version())
```

    10.0
    11.0
    111
    1000
    1.0



```python
print(pv.__version)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-29-f93eea81cbcc> in <module>()
    ----> 1 print(pv.__version)
    

    AttributeError: 'PrivateVariables' object has no attribute '__version'



```python
### static variables
```

## attributes
In Python, attribute is everything, contained inside an object. In Python there is no real distinction between plain data and functions, being both objects.

The following example represents a book with a title and an author. It also provides a `get_entry()` method which returns a string representation of the book.


```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_entry(self):
        return "{0} by {1}".format(self.title, self.author)
```

Every instance of this class will contain three attributes, namely `title, author`, and `get_entry`, in addition to the standard attributes provided by the object ancestor.


```python
b = Book(title="Akme", author="Mayank")
print(b.title)
b.title = "Lets Go"
print(b.title)
print(b.get_entry())
```

    Akme
    Lets Go
    Lets Go by Mayank



```python
data = b.get_entry
print(data)
print(data())
print(type(b.__dict__))
print(b.__dict__)
#print(b.nonExistAttribute())
```

    <bound method Book.get_entry of <__main__.Book object at 0x0000013DDBEB6DA0>>
    Lets Go by Mayank
    <class 'dict'>
    {'title': 'Lets Go', 'author': 'Mayank'}



```python
def testtest(func):
    print(func())

testtest(data)
```

    Lets Go by Mayank


Instead of using the normal statements to access attributes, you can use the following functions −

getattr
: to access the attribute of the object

The getattr(obj, name[, default]) 
: to access the attribute of object.
    
The hasattr(obj,name) 
: to check if an attribute exists or not.

The setattr(obj,name,value) 
    : to set an attribute. If attribute does not exist, then it would be created.

The delattr(obj, name)
    : to delete an attribute.

## Properties
Sometimes you want to have an attribute whose value comes from other attributes or, in general, which value shall be computed at the moment. The standard way to deal with this situation is to create a method, called getter, just like I did with get_entry().

In Python you can "mask" the method, aliasing it with a data attribute, which in this case is called __***`property`***__.


```python
class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_entry(self):
        return "{0} by {1}".format(self.title, self.author)

    entry = property(get_entry)

b = Book(title="Pawn of Prophecy", author="David Eddings")
print(b.entry)
```

    Pawn of Prophecy by David Eddings


Properties allow to specify also a write method (a setter), that is automatically called when you try to change the value of the property itself.

> NOTE: 

>    Don't Worry to much about properties, we have entire chapter dedicated for it. 


```python
class User():
    def __init__(self, name):
        self.name = name
    
    def getname(self):
        return "User's full name is: {0}".format(self.name) 
    
    def setname(self, name):
        self.name = name
        
    fullname = property(getname, setname)
    
user = User("Roshan Musheer")
print(user.fullname)
user.fullname = "Shaeel Parez"
print(user.fullname)
# print(x)
# print(p.name)
```

    Users full name is: Roshan Musheer
    Users full name is: Shaeel Parez



```python
class TestSetter():
    def setter(self, name):
        self.name = name
    myname = property(fset=setter)
    
ts = TestSetter()

ts.myname = "Mayank"
print(ts.name)
```

    Mayank



```python
#print(help(property))
```


```python
class A:
    def get_x(self, neg=False):
        return -5 if neg else 5
    x = property(get_x)
    
a = A()
print(a.x)
```

    5



```python
class Book(object):
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def _get_entry(self):
        print("_get_entry")
        return "{0} by {1}".format(self.__title, self.__author)

    def _set_entry(self, value):
        if " by " not in value:
            raise ValueError("Entries shall be formatted as '<title> by <author>'")
        self.__title, self.__author = value.split(" by ")
    
    entry = property(_get_entry, _set_entry)

    def __getattr__(self, attr):
        print("Sorry attribure do not exist")
        return None


b = Book(title="Step in C", author="Mayank Johri")
print(b.entry)
b.entry = "Lets learn C by Mayank Johri"
print("*"*20)
print(b.entry)
print("*"*20)
b.entry = "Explore Go by Mayank Johri"
print("*"*20)
print(b.entry)
b.nonExistAttribute
```

    _get_entry
    Step in C by Mayank Johri
    ********************
    _get_entry
    Lets learn C by Mayank Johri
    ********************
    ********************
    _get_entry
    Explore Go by Mayank Johri
    Sorry attribure do not exist

