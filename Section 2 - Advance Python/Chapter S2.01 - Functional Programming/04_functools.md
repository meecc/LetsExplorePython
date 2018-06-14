
# functools

The functools module is for higher-order functions: functions that act on or return other functions. In general, any callable object can be treated as a function for the purposes of this module.

Common functions in functools are as follows

* partial
* reduce

## partial

functools.partial does the follows:

* Makes a new version of a function with one or more arguments already filled in.
* New version of a function documents itself.


```python
def power(base, exponent):
    return base ** exponent
```


```python
def square(base):
    return power(base, 2)

def cube(base):
    return power(base, 3)
```

Now lets see the magic of partial


```python
from functools import partial

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(2))
print(cube(2))

print(square(2, exponent=4))
print(cube(2, exponent=9))
```

    4
    8
    16
    512



```python
from functools import partial

def multiply(x,y):
        return x * y

# create a new function that multiplies by 2
db2 = partial(multiply,2)
print(db2(4))
db4 = partial(multiply, 4)
print(db4(3))
```

    8
    12



```python
from functools import partial
 
#----------------------------------------------------------------------
def add(x, y):
    """"""
    return x + y
 
#----------------------------------------------------------------------
def multiply(x, y):
    """"""
    return x * y
 
#----------------------------------------------------------------------
def run(func):
    """"""
    print (func())
 
#----------------------------------------------------------------------
def main():
    """"""
    a1 = partial(add, 1, 2)
    m1 = partial(multiply, 5, 8)
    run(a1)
    run(m1)
 
if __name__ == "__main__":
    main()
```

    3
    40



```python
def another_function(func):
    """
    A function that accepts another function
    """
 
    def wrapper():
        """
        A wrapping function
        """
        val = "The result of %s is %s" % (func(),
                                          eval(func())
                                          )
        return val
    return wrapper
 
#----------------------------------------------------------------------
@another_function
def a_function():
    """A pretty useless function"""
    return "1+1"
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    print (a_function.__name__)
    print (a_function.__doc__)
    print(a_function())
```

    wrapper
    
            A wrapping function
            
    The result of 1+1 is 2



```python
from functools import wraps
 
#----------------------------------------------------------------------
def another_function(func):
    """
    A function that accepts another function
    """
 
    @wraps(func)
    def wrapper():
        """
        A wrapping function
        """
        val = "The result of %s is %s" % (func(),
                                          eval(func())
                                          )
        return val
    return wrapper
 
#----------------------------------------------------------------------
@another_function
def a_function():
    """A pretty useless function"""
    return "1+1"
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    #a_function()
    print (a_function.__name__)
    print (a_function.__doc__)
    print(a_function())
```

    a_function
    A pretty useless function
    The result of 1+1 is 2


Here we import wraps from the functools module and use it as a decorator for the nested wrapper function inside of another_function to map the __name__ and __doc__ to the wrapper function

### update_wrapper

The partial object does not have __name__ or __doc__ attributes by default, and without those attributes decorated functions are more difficult to debug. Using update_wrapper(), copies or adds attributes from the original function to the partial object.


```python
import functools


def myfunc1(a, b=2):
    print ('\tcalled myfunc1 with:', (a, b))
    return

def myfunc(a, b=2):
    """Docstring for myfunc()."""
    print ('\tcalled myfunc with:', (a, b))
    return

def show_details(name, f):
    """Show details of a callable object."""
    print ('%s:' % name)
    print ('\tobject:', f)
    print ('\t__name__:',) 
    try:
        print (f.__name__)
    except AttributeError:
        print ('(no __name__)')
    print ('\t__doc__', repr(f.__doc__))
    print
    return


show_details('myfunc1', myfunc1)
print("~"*20)
show_details('myfunc', myfunc)

p1 = functools.partial(myfunc, b=4)
print("+"*20)
show_details('raw wrapper', p1)
print("^"*20)
print ('Updating wrapper:')
print ('\tassign:', functools.WRAPPER_ASSIGNMENTS)
print ('\tupdate:', functools.WRAPPER_UPDATES)
print("*"*20)

functools.update_wrapper(p1, myfunc)
show_details('updated wrapper', p1)
```

    myfunc1:
    	object: <function myfunc1 at 0x7f4dc83b4ea0>
    	__name__:
    myfunc1
    	__doc__ None
    ~~~~~~~~~~~~~~~~~~~~
    myfunc:
    	object: <function myfunc at 0x7f4dcffedbf8>
    	__name__:
    myfunc
    	__doc__ 'Docstring for myfunc().'
    ++++++++++++++++++++
    raw wrapper:
    	object: functools.partial(<function myfunc at 0x7f4dcffedbf8>, b=4)
    	__name__:
    (no __name__)
    	__doc__ 'partial(func, *args, **keywords) - new function with partial application\n    of the given arguments and keywords.\n'
    ^^^^^^^^^^^^^^^^^^^^
    Updating wrapper:
    	assign: ('__module__', '__name__', '__qualname__', '__doc__', '__annotations__')
    	update: ('__dict__',)
    ********************
    updated wrapper:
    	object: functools.partial(<function myfunc at 0x7f4dcffedbf8>, b=4)
    	__name__:
    myfunc
    	__doc__ 'Docstring for myfunc().'

