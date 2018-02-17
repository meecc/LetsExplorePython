
**Hurdle 1: What will the output of the following program.**


```python
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print (a.f(), b.f())
print (a.g(), b.g())
```

    ('A', 'B')
    ('A', 'B')



```python
class Circle(object):
    color = "red"

class NewCircle(Circle):
    color = "blue"
    
nc = NewCircle
print(nc)
```

    <class '__main__.NewCircle'>



```python
print(nc.color)
```

    blue



```python
class Person:
    def __init__(self, id):
        self.id = id
 
sam = Person(100)
 
sam.__dict__['age'] = 49
print (sam.age + len(sam.__dict__))
```

    51



```python
class A:
    def __init__(self):
        self.calcI(30)
        print("i from A is", self.i)
 
    def calcI(self, i):
        self.i = 2 * i;
 
class B(A):
    def __init__(self):
        super().__init__()
        
    def calcI(self, i):
        self.i = 3 * i;
 
b = B()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-5-367e1b2b1488> in <module>()
         14         self.i = 3 * i;
         15 
    ---> 16 b = B()
    

    <ipython-input-5-367e1b2b1488> in __init__(self)
          9 class B(A):
         10     def __init__(self):
    ---> 11         super().__init__()
         12 
         13     def calcI(self, i):


    TypeError: super() takes at least 1 argument (0 given)

