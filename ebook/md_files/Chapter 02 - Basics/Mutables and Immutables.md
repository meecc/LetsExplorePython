
# Mutables and Immutables

A general explanation from the "Data Model" chapter(http://docs.python.org/reference/datamodel.html#objects-values-and-types) in the Python Language Reference":

> "The value of some objects can change. Objects whose value can change are said to be mutable; objects whose value is unchangeable once they are created are called immutable.

> (The value of an immutable container object that contains a reference to a mutable object can change when the latter’s value is changed; however the container is still considered immutable, because the collection of objects it contains cannot be changed. So, immutability is not strictly the same as having an unchangeable value, it is more subtle.)

An object’s mutability is determined by its type; for instance, numbers, strings and tuples are immutable, while dictionaries and lists are mutable.

Common immutable type:

* numbers: int(), float(), complex()
* immutable sequences: str(), tuple(), frozenset(), bytes()

Common mutable type (almost everything else):

* mutable sequences: list(), bytearray()
* set type: set()
* mapping type: dict()
* classes, class instances
...


```python
ls = [1,2,4,5]

print(id(ls))
print(ls)
ls[2]=3
print(id(ls))
print(ls)
```

    140291830112200
    [1, 2, 4, 5]
    140291830112200
    [1, 2, 3, 5]


> Although, immutable elements can not be updated, but mutable elements inside immutables can update themself as shown in the example below.


```python
tp =(1,2,3,4,[2,2,2])
print(tp)
print(id(tp))
tp[4][2]=4
print(tp)
print(id(tp))
```

    (1, 2, 3, 4, [2, 2, 2])
    139845075278048
    (1, 2, 3, 4, [2, 2, 4])
    139845075278048



```python
print(dir(tp))
```

    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

