
# Multiple Inheritance
---
Multiple inheritance is possible in Python unlike other programming languages. A class can be derived from more than one base classes. The syntax for multiple inheritance is similar to single inheritance.


```python
class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass
```


```python
class Base1:
    def test(self):
        print("in Base1 -> test")

class Base2:
    def test(self):
        print("in Base2 -> test")

class MultiDerived(Base1, Base2):
    def test2(self):
        super().test()
        Base2.test(Base2)

class MultiDerived2(Base2, Base1):
    def test2(self):
        super().test()
        Base2.test(Base2)

print("Please check the result of test()")

# d = Base2()
# print(type(d))
md = MultiDerived()
md.test2()
md.test()
print("*"*10)
md2 = MultiDerived2()
md2.test2()
md2.test()

```

    Please check the result of test()
    in Base1 -> test
    in Base2 -> test
    in Base1 -> test
    **********
    in Base2 -> test
    in Base2 -> test
    in Base2 -> test


## Multilevel Inheritance
---
we can inherit to from a derived class also. This is called as multilevel inheritance. Multilevel inheritance can be of any depth in Python. An example with corresponding visualization is given below.


```python
class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Derived1):
    pass
```

In the multiple inheritance scenario, any specified attribute is searched first in the current class. If not found, the search continues into parent classes in depth-first, left-right fashion without searching same class twice


```python
class Base:
    def test(self):
        print("In Base test")
        
    def test_alone(self):
        print("In Base test: test_alone")

class Derived1(Base):
    def test(self):
        print("In Derived1 test")
        super().test()

    def test_alone(self, val):
        print("In Derived1 test: test_alone ", val)

#     def test_alone(self):
#         print("In Base test: test_alone")

class Derived2(Derived1):
    def test2(self):
        print("in Derived2 test2")
        
obj = Derived2()
obj.test()
obj.test2()
obj.test_alone()
Base.test(Base)
```

    In Derived1 test
    In Base test
    in Derived2 test2



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-5-94cf95e50635> in <module>()
         24 obj.test()
         25 obj.test2()
    ---> 26 obj.test_alone()
         27 Base.test(Base)


    TypeError: test_alone() missing 1 required positional argument: 'val'



```python
class Base:
    def test(self):
        print("In Base test")
        
    def test_alone(self):
        print("In Base test: test_alone")

class Derived1(Base):
    def test(self):
        print("In Derived1 test")
        super().test()

    def test_alone(self, val):
        print("In Derived1 test: test_alone ", val)

    def test_alone(self):
        print("In Base test: test_alone")

class Derived2(Derived1):
    def test2(self):
        print("in Derived2 test2")
        
obj = Derived2()
obj.test()
obj.test2()
obj.test_alone()
Base.test(Base)
```

    In Derived1 test
    In Base test
    in Derived2 test2
    In Base test: test_alone
    In Base test



```python
class Base():
    def test1(self):
        print("In Base test")

class Derived1(Base):
    def test(self):
        print("In Derived1 test")

class Derived3(Derived1):
    pass

d = Derived3()
d.test()
d.test1()
```

    In Base test



```python
class Base():
    def test(self):
        print("In Base test")

class Derived1(Base):
    def test(self):
        print("In Derived1 test", end=", ")
        return "Golu"

class Derived3(Derived1):
    pass

d = Derived3()
print(d.test())
```

    In Derived1 test, Golu



```python
#### Explicitly calling function

class Base:
    def test(self):
        print("In Base test")

class Derived1(Base):
    def test(self):
        print("In Derived1 test")

class Derived2(Derived1):
    pass

obj = Derived2
obj.test(obj)

Derived2.test(Derived2)
```

    In Derived1 test
    In Derived1 test



```python
#### Explicitly calling function

class Base:
    def test(self):
        print("In Base test")

class Derived1(Base):
    def test(self):
        print("In Derived1 test")
        print(type(self))

class Derived2(Derived1):
    pass

obj = Derived2
obj.test(obj)

Derived2.test(Derived2)
```

    In Derived1 test
    <class 'type'>
    In Derived1 test
    <class 'type'>



```python
#### Explicitly calling function

class Base:
    def test(self):
        print("In Base test")

class Derived1(Base):
    def test(self):
        print("In Derived1 test")
        print(type(self))

class Derived2(Derived1):
    pass


obj = Derived2()
obj.test()

Derived2.test(Derived2)
```

    In Derived1 test
    <class '__main__.Derived2'>
    In Derived1 test
    <class 'type'>

