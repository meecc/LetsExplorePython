

```python
x = "!!! Good Morning, Goten Tag !!!"
y = x
print(id(y),":", id(x))
print(dir(y))
print(type(y))
print(x.__doc__)
```

    436264817968 : 436264817968
    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
    <class 'str'>
    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str
    
    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.



```python
x = "!!! Good Morning, Goten Tag !!!"
y = x
print(id(y),":", id(x))
y = y + " Hello"
print(id(y), ":", id(x))
print(y)
print(x) 
```

    436264819328 : 436264819328
    436262611584 : 436264819328
    !!! Good Morning, Goten Tag !!! Hello
    !!! Good Morning, Goten Tag !!!



```python
print(y.replace("G", "g"))
print(id(y))
print(y)
```

    !!! good Morning, goten Tag !!! Hello
    436262611584
    !!! Good Morning, Goten Tag !!! Hello

