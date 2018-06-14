
# Introduction to Programming Paradigms
---

In the initial days we had only one type of programming paradigms, **the paradigm of the developer :)**. We will write what we wants and how we wants, but as we matures and our problems increases in size & complexity from adding two numbers to soling the issues of the entire universe like chatting, sharing (photos, texts {our own or other's copy pasted 1000<sup>nd</sup> time}, videos, live streaming etc), we need to make sure our code 
- is easily understool by others
- is easily upgradable
- is easily modifyable
- execution is fast
- is aligned to the problem resolution 

As the domain of solution increased, so did the types of paradigms which can be used for resolution. Most common of paradigms are listed below.

* **Imperative**: Imperative uses `statements` which can change the state of program. It's focus is on describing how a program operates, same way in which the imperative mood in natural languages expresses commands. It consists of commands for the computer to perform.

    It is useful in manipulating data structures and produces elegant & simple code.
    
    The term is often used in contrast to **declarative programming**, which focuses on what the program should accomplish without specifying how the program should achieve the result.


```python
towns = ["Rio de Janeiro", "Bhopal", "Budd Lake", "New York", "São Paulo", "Curitib]a "]
count = 0
for city in towns:
    print(city)
    count = count + 1
print()
print("Total number of cities:", count)
```

    Rio de Janeiro
    Bhopal
    Budd Lake
    New York
    São Paulo
    Curitib]a 
    
    Total number of cities: 6


* **Functional**: Every statement in functional programming is treated as mathematical equation. Also `state` or `mutable data` are avoided. Its main advantage are
    - that any side effects due to data are avoided,
    - good at parallel processing because there is no state, recursion and lambda calculus.

* **Object-oriented**: Relies on data fields that are treated as objects and manipulated only through prescribed methods. Python doesn’t fully support this coding form because it can’t implement features such as data hiding. However, this remains a useful coding style for complex applications because it supports encapsulation and polymorphism. This coding style also favors code reuse.

* **Procedural**: Tasks are treated as step-by-step iterations where common tasks are placed in functions that are called as needed. This coding style favors iteration, sequencing, selection, and modularization. It is a type of **imperative programming** in which, programs are created using one or more `procedures` (also known as `subroutines` or `functions`).

## Examples


```python
L = [1, 2, 4 , 6, 5, 7, 3]
```

### Functional


```python
from functools import reduce 


def add(x, y):
    return x + y

sum = reduce(add, L)
print(sum)
```

    28


the above example is below implemented using `lambda`


```python
import functools


Sum = functools.reduce(lambda x, y: x + y, L)
print(Sum)
```

    28


### Imperative 


```python
sum = 0

for x in L:
    sum += x

print(sum)
```

    28


### Procedural


```python
def add(a, b):
    return a + b

sum = 0
for a in L:
    sum = add(sum, a)

print(sum)
```

    28


### Object-oriented


```python
class Saving(object):
    def __init__(self, list_data):
        self.total_savings = list_data
    
    def add(self):
        sum = 0
        for a in self.total_savings:
            sum += a
        return sum

s = Saving(L)
print(s.add())
```

    28


## Design Patterns

### Flyweight pattern

In computer programming, flyweight is a software design pattern. A flyweight is an object that minimizes memory usage by sharing as much data as possible with other similar objects; it is a way to use objects in large numbers when a simple repeated representation would use an unacceptable amount of memory. Often some parts of the object state can be shared, and it is common practice to hold them in external data structures and pass them to the objects temporarily when they are used.

A classic example usage of the flyweight pattern is the data structures for graphical representation of characters in a word processor. It might be desirable to have, for each character in a document, a glyph object containing its font outline, font metrics, and other formatting data, but this would amount to hundreds or thousands of bytes for each character. Instead, for every character there might be a reference to a flyweight glyph object shared by every instance of the same character in the document; only the position of each character (in the document and/or the page) would need to be stored internally.

**REFERENCE**: https://en.wikipedia.org/wiki/Flyweight_pattern


```python
# Instances of CheeseBrand will be the Flyweights
class CheeseBrand(object):
    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost
        self._immutable = True   # Disables future attributions

    def __setattr__(self, name, value):
        if getattr(self, '_immutable', False):  # Allow initial attribution
            raise RuntimeError('This object is immutable')
        else:
            super(CheeseBrand, self).__setattr__(name, value)
    

class CheeseShop(object):
    menu = {}  # Shared container to access the Flyweights
    
    def __init__(self):
        self.orders = {}  # per-instance container with private attributes

    def stock_cheese(self, brand, cost):
        cheese = CheeseBrand(brand, cost)
        self.menu[brand] = cheese   # Shared Flyweight

    def sell_cheese(self, brand, units):
        self.orders.setdefault(brand, 0)
        self.orders[brand] += units   # Instance attribute

    def total_units_sold(self):
        return sum(self.orders.values())
    
    def total_income(self):
        income = 0
        for brand, units in self.orders.items():
            income += self.menu[brand].cost * units
        return income


shop1 = CheeseShop()
shop2 = CheeseShop()

shop1.stock_cheese('white', 1.25)
shop1.stock_cheese('blue', 3.75)
# Now every CheeseShop have 'white' and 'blue' on the inventory
# The SAME 'white' and 'blue' CheeseBrand

shop1.sell_cheese('blue', 3)    # Both can sell
shop2.sell_cheese('blue', 8)    # But the units sold are stored per-instance

assert shop1.total_units_sold() == 3
assert shop1.total_income() == 3.75 * 3

assert shop2.total_units_sold() == 8
assert shop2.total_income() == 3.75 * 8
```

## Summary

As stated earlier, Programming paradigms are nothing to be afraid of. They arejust different approaches to solving problems like
- **Functional**: In it we ask "What values should be transform and how should they be transformed to resolve this problem?"
    - In it we care about values
- **Procedural**: In it we ask "What are the steps which needs to be performed to resolve this problem?"
    - we care about the process/steps
- **OOP**: In it we ask "Which objects need to interact and what messages are needed to be sent between them to resolve this problem?"
     - We care about the real world entities and their interactions.

## References

- https://en.wikipedia.org/wiki/Imperative_programming
- https://en.wikipedia.org/wiki/Programming_paradigm
- https://docs.python.org/3/howto/functional.html
- https://blog.newrelic.com/2015/04/01/python-programming-styles/
- https://stackoverflow.com/questions/47441017/is-it-bad-practice-to-mix-oop-and-procedural-programming-in-python-or-to-mix-pr
