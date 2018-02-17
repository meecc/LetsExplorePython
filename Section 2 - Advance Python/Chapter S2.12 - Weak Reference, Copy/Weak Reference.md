
# Misc Advance Topics
----


```python
lst1 = [1, 32, 3, 43]
lst2 = lst1
print(lst1, lst2)
```

    ([1, 32, 3, 43], [1, 32, 3, 43])



```python
lst2[3] = "TEST"
print(lst1, lst2)
print(id(lst1), id(lst2))
```

    ([1, 32, 3, 'TEST'], [1, 32, 3, 'TEST'])
    (140234224279208, 140234224279208)



```python
del(lst1)
```


```python
print(id(lst2))
```

    140234224279208



```python
del(lst2)
```


```python
print(id(lst2))
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-16-59e423e2a79d> in <module>()
    ----> 1 print(id(lst2))
    

    NameError: name 'lst2' is not defined


## Weak Reference: 
Non-permanent References to Objects

### What is Strong reference

When memory is referenced by a variable, its called strong reference. What that means is that untill all the strong references are removed from the memory location, it is not removed.


```python
a = 101
b = a
print(a, id(a))
print(b, id(b))
```

    (101, 6399912)
    (101, 6399912)



```python
del(a)
# print(a, id(a))
print(b, id(b))
```

    (101, 6399912)



```python
del(b)
# print(a, id(a))
# print(b, id(b))
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-9-62186b0eeb0a> in <module>()
    ----> 1 del(b)
          2 # print(a, id(a))
          3 # print(b, id(b))


    NameError: name 'b' is not defined



```python
import sys

class MayaHello:
    def __init__(self, lang):
        self.lang = lang
    
    def hello(self):
        if(self.lang == 'hi'):
            return "नमस्ते"
        elif(self.lang == 'de'):
            return "Hallo"
        else:
            return ("Hello")
    
    def __del__(self):
        print("self destruct initiated")
        del self.lang

a = MayaHello('hi')
print(a.hello())
sys.stdout.flush()
b = a 
print(b.hello()) 
sys.stdout.flush()
```

    self destruct initiated
    नमस्ते
    self destruct initiated
    नमस्ते



```python
print(a.hello())
```

    नमस्ते


### What are they

Weak references are used to refer to objects which are expensive in nature, but 

### When to Use 
As they are refered to an "expensive" object, but allow its memory to be reclaimed by the garbage collector if there are no other non-weak references.

Weak references to objects are managed through the ref class. To retrieve the original object, call the reference object.

** Reference URL's **
- https://stackoverflow.com/questions/2436302/when-to-use-weak-references-in-python
- https://stackoverflow.com/questions/1507566/how-and-when-to-appropriately-use-weakref-in-python


The typical use for weak references is if A has a reference to B and B has a reference to A. Without a proper cycle-detecting garbage collector, those two objects would never get GC'd even if there are no references to either from the "outside". However if one of the references is "weak", the objects will get properly GC'd.

However, Python does have a cycle-detecting garbage collector (since 2.0!), so that doesn't count :)

Another use for weak references is for caches. It's mentioned in the weakref documentation:

A primary use for weak references is to implement caches or mappings holding large objects, where it’s desired that a large object not be kept alive solely because it appears in a cache or mapping.
If the GC decides to destroy one of those objects, and you need it, you can just recalculate / refetch the data.

As a more transparent alternative to weakref.ref, we can use weakref.proxy. This call requires a strong reference to an object as its first argument and returns a weak reference proxy. The proxy behaves just like a strong reference, but throws an exception when used after the target is dead:


```python
obj = ExpensiveObject()
b = weakref.proxy(obj)
del(obj)
# print('obj:', obj)
print('ref proxy:', b) # Pointing to None Type
```

    (Deleting <__main__.ExpensiveObject instance at 0x7f40e6ffa1b8>)
    ('ref proxy:', <weakproxy at 0x7f40e6f79310 to NoneType at 0x7f41010c3e40>)


### Reference Callbacks

The ref constructor accepts an optional callback function that is invoked when the referenced object is deleted.




```python
import weakref


class ExpensiveObject:

    def __del__(self):
        print('(Deleting {})'.format(self))


def callback(reference):
    """Invoked when referenced object is deleted"""
    print('callback({!r})'.format(reference))


obj = ExpensiveObject()
r = weakref.ref(obj, callback)

print('obj:', obj)
print('ref:', r)
print('r():', r())

print('deleting obj')
del obj
print('r():', r())
```

    ('obj:', <__main__.ExpensiveObject instance at 0x7f8ac835a488>)
    ('ref:', <weakref at 0x7f8ac83567e0; to 'instance' at 0x7f8ac835a488>)
    ('r():', <__main__.ExpensiveObject instance at 0x7f8ac835a488>)
    deleting obj
    callback(<weakref at 0x7f8ac83567e0; dead>)
    (Deleting <__main__.ExpensiveObject instance at 0x7f8ac835a488>)
    ('r():', None)


References:
    - https://mindtrove.info/python-weak-references/
