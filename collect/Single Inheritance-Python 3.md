
> Its already discussed while learning classes and OOP's, hence skipping


```python
class Pen():
    def __init__(self, size, name):
        self.name = name
        self.size = size
    
    def set_name(self, name):
        self.name = name
```


```python
class BallPen(Pen):
    def __init__(self, size, name, color):
        self.color = color
        super().__init__(size, name)
    
    def set_color(self, color):
        self.color = color
```


```python
class InkPen(Pen):
    def __init__(self, size, name, cart_type):
        self.cart = cart_type
        super().__init__(size, name)
```


```python
pb = BallPen(10, "Renolds", "Green")
print(pb.name)
pb.set_name("cello")
print(pb.name)
print(dir(pb))
print(pb.__dict__)

```

    Renolds
    cello
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'color', 'name', 'set_color', 'set_name', 'size']
    {'color': 'Green', 'name': 'cello', 'size': 10}



```python
class grand_parent:
    def __init__(self, middle_name):
        self.__middle_name = middle_name
        
    def middle_name(self, middle_name):
        self.__middle_name = middle_name
        return self.__middle_name
```


```python
class parent(grand_parent):
    def __init__(self, middle_name, surname):
        self.__surname = surname
        super().__init__(middle_name)
    
    def middle_name(self):
        return self.middle_name
```


```python
class student(parent):
    def __init__(self, name, middle_name, surname):
        self.name = name
        super().__init__(middle_name, surname)
```


```python
mohan = student("Venkat", "kumar", "Mohan")
```


```python
print(mohan.middle_name)
```

    <bound method parent.middle_name of <__main__.student object at 0x000002413971CBA8>>



```python
print(mohan.middle_name("KUMAR"))
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-26-e9c69e945a76> in <module>()
    ----> 1 print(mohan.middle_name("KUMAR"))
    

    TypeError: middle_name() takes 1 positional argument but 2 were given



```python
# NOTE: python 2 has issues with Super , get it also documented here
```
