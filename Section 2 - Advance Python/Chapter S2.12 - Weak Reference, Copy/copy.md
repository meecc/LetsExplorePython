
# Misc Advance Topics
----

## copy — Duplicate Objects

### Shallow Copies

The shallow copy created by copy() is a new container populated with references to the contents of the original object. When making a shallow copy of a list object, a new list is constructed and the elements of the original object are appended to it.


```python
import copy

class MyTry:
    def __init__(self):
        self.lst = [1,2,3,4,5]

a = MyTry()
dup = copy.copy(a) 
a.lst.append(6)
print(a.lst, dup.lst)
print(id(a), id(dup))
```

    ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6])
    (139639932453520, 139639932453448)



```python
import copy

class MyTry:
    def __init__(self):
        self.lst = [1,2,3,4,5]

a = MyTry()
dup = copy.copy(a) 
a.lst.append(6)
print(a.lst, dup.lst)
print(id(a), id(dup))
print(id(a.lst), id(dup.lst))

```

    ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6])
    (139639932453880, 139639932453736)
    (139639933132096, 139639933132096)


### Deep Copies

The deep copy created by deepcopy() is a new container populated with copies of the contents of the original object. To make a deep copy of a list, a new list is constructed, the elements of the original list are copied, and then those copies are appended to the new list.

Replacing the call to copy() with deepcopy() makes the difference in the output apparent.


```python
import copy

class MyTry:
    def __init__(self):
        self.lst = [1,2,3,4,5]

a = MyTry()
dup = copy.deepcopy(a) 
a.lst.append(6)
print(a.lst, dup.lst)
print(id(a), id(dup))
print(id(a.lst), id(dup.lst))
```

    ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5])
    (139639932454600, 139639932454456)
    (139639933132600, 139639932353208)



```python
lst = [1,2,3,4,5]
dup_lst = copy.deepcopy(lst)
print(id(lst), id(dup_lst))
```

    (139639932351552, 139639933171400)


## Customizing Copy Behavior

It is possible to control how copies are made using the __copy__() and __deepcopy__() special methods.

- __copy__() is called without any arguments and should return a shallow copy of the object.
- __deepcopy__() is called with a memo dictionary and should return a deep copy of the object. Any member attributes that need to be deep-copied should be passed to copy.deepcopy(), along with the memo dictionary, to control for recursion. (The memo dictionary is explained in more detail later.)
