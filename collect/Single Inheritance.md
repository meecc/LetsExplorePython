
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
        super(Pen).__init__(size, name)
    
    def set_color(self, color):
        self.color = color
```


```python
class InkPen(Pen):
    def __init__(self, size, name, cart_type):
        self.cart = cart_type
        super(Pen).__init__(size, name)
```


```python
pb = BallPen(10, "Renolds", "Green")
print(pb.name)
pb.set_name("cello")
print(pb.name)
print(dir(pb))
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-5-8335b0d47e20> in <module>()
    ----> 1 pb = BallPen(10, "Renolds", "Green")
          2 print(pb.name)
          3 pb.set_name("cello")
          4 print(pb.name)
          5 print(dir(pb))


    <ipython-input-3-61166b76a72b> in __init__(self, size, name, color)
          2     def __init__(self, size, name, color):
          3         self.color = color
    ----> 4         super(Pen).__init__(size, name)
          5 
          6     def set_color(self, color):


    TypeError: super() argument 1 must be type, not int



```python
# NOTE: python 2 has issues with Super , get it also documented here
```
