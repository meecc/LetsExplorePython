
# ABC
----
Abstract base classes are a form of interface checking more strict than individual hasattr() checks for particular methods. By defining an abstract base class, you can define a common API for a set of subclasses. This capability is especially useful in situations where a third-party is going to provide implementations, such as with plugins to an application, but can also aid you when working on a large team or with a large code-base where keeping all classes in your head at the same time is difficult or not possible.

## How ABCs Work



```python
from abc import ABCMeta, abstractmethod


class Mammal(metaclass=ABCMeta):
## version 2.x ##     __metaclass__=ABCMeta
    
    @abstractmethod
    def eyes(self, val):
        pass

#     @abstractmethod
#     def hand(self):
#         pass
    
    def hair(self):
        print("hair")
    
    def neocortex(self):
        """a part of the cerebral cortex concerned with sight and hearing in mammals, 
        regarded as the most recently evolved part of the cortex."""
        print("neocortex")
    
class Human(Mammal):
    def eyes(self, val):
        print("human eyes")

print ('Subclass:', issubclass(Human, Mammal))
print ('Instance:', isinstance(Human(), Mammal))
c = Human()
print ('Instance:', isinstance(c, Mammal))
c.eyes("red")
```

    Subclass: True
    Instance: True
    Instance: True
    human eyes



```python
print(dir(c))
```

    ['__abstractmethods__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_abc_cache', '_abc_negative_cache', '_abc_negative_cache_version', '_abc_registry', 'eyes', 'hair', 'neocortex']



```python
m = Mammal()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-4-a74334e04a70> in <module>()
    ----> 1 m = Mammal()
    

    TypeError: Can't instantiate abstract class Mammal with abstract methods eyes



```python
class fish(Mammal):
    pass
```


```python
myfish = fish()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-8-738008bbe17b> in <module>()
    ----> 1 myfish = fish()
    

    TypeError: Can't instantiate abstract class fish with abstract methods eyes


** NOTE ** 

* **issubclass**: Return true if class is a subclass (direct, indirect or virtual) of classinfo. A class is considered a subclass of itself. classinfo may be a tuple of class objects, in which case every entry in classinfo will be checked. In any other case, a TypeError exception is raised.

* **isinstance**: Return true if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof. Also return true if classinfo is a type object (new-style class) and object is an object of that type or of a (direct, indirect or virtual) subclass thereof. If object is not a class instance or an object of the given type, the function always returns false. If classinfo is a tuple of class or type objects (or recursively, other such tuples), return true if object is an instance of any of the classes or types. If classinfo is not a class, type, or tuple of classes, types, and such tuples, a TypeError exception is raised.

## Registering the child class


```python
from abc import ABCMeta, abstractmethod


class Mammal(metaclass=ABCMeta):
    
    @abstractmethod
    def eyes(self, val):
        raise NotImplementedError()

    def hair(self):
        print("hair")
    
    def neocortex(self):
        """a part of the cerebral cortex concerned with sight and hearing in mammals, 
        regarded as the most recently evolved part of the cortex."""
        print("neocortex")
    
class Human:
    def eyes(self, val):
        print("human eyes: ", val)

Mammal.register(Human)
print ('Subclass:', issubclass(Human, Mammal))
c = Human()
print ('Instance:', isinstance(c, Mammal))
c.eyes("Hazel")
```

    Subclass: True
    Instance: True
    human eyes:  Hazel


## Implementation Through Subclassing
----


```python
from abc import ABCMeta, abstractmethod


class Mammal(metaclass=ABCMeta):
## version 2.x ##     __metaclass__=ABCMeta
    
    @abstractmethod
    def eyes(self, val):
        raise NotImplementedError()

#     @abstractmethod
#     def hand(self):
#         raise NotImplementedError()
    
    def hair(self):
        print("hair")
    
    def neocortex(self):
        """a part of the cerebral cortex concerned with sight and hearing in mammals, 
        regarded as the most recently evolved part of the cortex."""
        print("neocortex")
    
class Human(Mammal):
    def eyes(self, val):
        print("human eyes")

print ('Subclass:', issubclass(Human, Mammal))
print ('Instance:', isinstance(Human(), Mammal))
c = Human()
print ('Instance:', isinstance(c, Mammal))
c.eyes("Gray")
```

    Subclass: True
    Instance: True
    Instance: True
    human eyes


### Abstract Method Continued


```python
from abc import ABCMeta, abstractmethod


class Mammal(metaclass=ABCMeta):
## version 2.x ##     __metaclass__=ABCMeta
    
    @abstractmethod
    def eyes(self,color):
        print("Eyes color : " + color)

    def hair(self):
        print("hair")
    
    def neocortex(self):
        """a part of the cerebral cortex concerned with sight and hearing in mammals, 
        regarded as the most recently evolved part of the cortex."""
        print("neocortex")
    
class Human(Mammal):
    def eyes(self, val):
        super(Human, self).eyes(val)
        print("human eyes")

print ('Subclass:', issubclass(Human, Mammal))
print ('Instance:', isinstance(Human(), Mammal))
c = Human()
print ('Instance:', isinstance(c, Mammal))
c.eyes("Green")
```

    Subclass: True
    Instance: True
    Instance: True
    Eyes color : Green
    human eyes


## Abstract Properties
----
If your API specification includes attributes in addition to methods, you can require the attributes in concrete classes by defining them with @abstractproperty


```python
from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    
    @abc.abstractproperty
    def value(self):
        return 'Should never get here'


class Implementation(Base):
    @property
    def value(self):
        return 'concrete property'

if __name__ == '__main__':
#     try:
#         b = Base()
#         print ('Base.value:', b.value)
#     except Exception as err:
#         print ('ERROR:', str(err))

    i = Implementation()
    print ('Implementation.value:', i.value)
```

    Implementation.value: concrete property



```python
import abc

class Base(metaclass=abc.ABCMeta):
    
    @abc.abstractproperty
    def value(self):
        return 'Should never see this'
    
    @value.setter
    def value(self, newvalue):
        return


class Implementation(Base):
    
    _value = 'Default value'
    
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, newvalue):
        self._value = newvalue


i = Implementation()
print ('Implementation.value:', i.value)

i.value = 'New value'
print ('Changed value:', i.value)
```

    Implementation.value: Default value
    Changed value: New value


#### NOTE #####
For Python 2, that means assigning it to the __metaclass__ attribute on the class:
```python
class CVIterator(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.n = None # the value of n is obtained in the fit method
```
In Python 3, you'd use the metaclass=... syntax when defining the class:
```python
class CVIterator(metaclass=ABCMeta):
    def __init__(self):
        self.n = None # the value of n is obtained in the fit method
```

### The __metaclass__ attribute

The __metaclass__ attribute was introduced to give the programmer some control over the semantics of the class statement
