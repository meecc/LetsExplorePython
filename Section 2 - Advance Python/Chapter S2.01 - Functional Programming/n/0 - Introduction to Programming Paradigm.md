
# Introduction to Programming Paradigms
---

* **Imperative**: It uses statements that change a program's state. It focuses on describing how a program operates. It is useful in manipulating data structures and produces elegant & simple code.

    In computer science, imperative programming is a programming paradigm that uses statements that change a program's state. In much the same way that the imperative mood in natural languages expresses commands, an imperative program consists of commands for the computer to perform. Imperative programming focuses on describing how a program operates.

    The term is often used in contrast to **declarative programming**, which focuses on what the program should accomplish without specifying how the program should achieve the result.


* **Declarative**: 


* **Functional**: Every statement in functional programming is treated as mathematical equation. Also `state` or `mutable data` are avoided. Its main advantage are
    - that any side effects due to data are avoided,
    - good at parallel processing because there is no state, recursion and lambda calculus.


* **Object-oriented**: Relies on data fields that are treated as objects and manipulated only through prescribed methods. Python doesn’t fully support this coding form because it can’t implement features such as data hiding. However, this remains a useful coding style for complex applications because it supports encapsulation and polymorphism. This coding style also favors code reuse.


* **Procedural**: Tasks are treated as step-by-step iterations where common tasks are placed in functions that are called as needed. This coding style favors iteration, sequencing, selection, and modularization.

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

### Object-oriented

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

## References

- https://en.wikipedia.org/wiki/Imperative_programming
- https://en.wikipedia.org/wiki/Programming_paradigm
- https://docs.python.org/3/howto/functional.html
