
# property 
-----
Python has a great concept called property, which makes the life of an object oriented programmer much simpler. Before defining and going into details of what a property in Python is, let us first build an intuition on why it would be needed in the first place.


```python
CONST = 10 # some constant
class Weather_balloon():
    temp = 222
    
    def convert_temp_to_f(self):
        return self.temp * CONST
    
w = Weather_balloon()
w.temp = 122
print(w.convert_temp_to_f())
```

    1220



```python
class Circle():
    area = None
    radius = None

    def __init__(self, radius):
        self.radius = radius
        self.area = 3.14*radius*radius
        
c = Circle(10)
print(c.radius)

print(c.area)
c.area=222

print(c.radius)
print(c.area)
```

    10
    314.0
    10
    222



```python
class Circle():
    _area = None
    _radius = None
    
    def __init__(self, radius):
        self.set_radius(radius)
        
    def get_area(self):
        return self._area
    
    def get_radius(self):
        return self._radius
    
    def set_radius(self, radius):
        self._radius = radius
        self._area = 3.14*radius*radius

    radius = property(get_radius, set_radius)
        
c = Circle(10)
print(c.radius)
print(c._area)

c.radius=222
print(c.radius)
print(c._area)
```

    10
    314.0
    222
    154751.76



```python
import math

class Circle():
    _area = None
    _radius = None
    
    def __init__(self, radius):
        self.set_radius(radius)
        
    def get_radius(self):
        return self._radius
    
    def set_radius(self, radius):
        self._radius = radius
        self._area = 3.14*radius*radius

    radius = property(get_radius, set_radius)
    
    @property
    def area(self):
        return self._area
    
    @area.setter
    def area(self, area):
        self._area = area
        self._radius = math.sqrt(self._area)/3.14
        
        
c = Circle(10)
print(c.radius)
print(c.area)

print("---")
c.radius=222

print(c.radius)
print(c.area)

c.area=154751

print(c.radius)
print(c.area)
```

    10
    314.0
    ---
    222
    154751.76
    125.28154021658304
    154751



```python
class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
```


```python
man = Celsius()
# set temperature
man.temperature = 37

# get temperature
print(man.temperature)


# get degrees Fahrenheit
print(man.to_fahrenheit())
##### print(Celsius.temperature)
```

    37
    98.60000000000001



```python
##############
### Riddle ###
##############
class MyClass(): 
    x = 0
    y = 100

a = MyClass()
b = MyClass()

a.x = 2
print(id(a.y), id(b.y))
print(id(a.x), id(b.x))
print(b.x)

MyClass.x = 4
print(a.x)
print(b.x)

MyClass.x = 7
print(a.x)
print(b.x)
print("~~~~~~")
b.x = MyClass.y
MyClass.x = 4
print(b.x)
```

    1722795568 1722795568
    1722792432 1722792368
    0
    ~~~~~~
    100


## Class with Getter and Setter


```python
class Celsius:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # new update
    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value
```

We can see above that new methods get_temperature() and set_temperature() were defined and furthermore, temperature was replaced with \_temperature. An underscore (\_) at the beginning is used to denote private variables in Python.

## Python Way - Property
----
The pythonic way to deal with the above problem is to use property. Here is how we could have achieved it.


```python
class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature, set_temperature)
```


```python
man = Celsius()
# set temperature
man.temperature = 137

# get temperature
print(man.temperature)

# get degrees Fahrenheit
print(man.to_fahrenheit())
##### print(Celsius.temperature)
```

    Setting value
    Getting value
    137
    278.6


## Deep in Property


```python
### Method 1
temperature = property(get_temperature, set_temperature)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-17-586c28105eea> in <module>()
          1 ### Method 1
    ----> 2 temperature = property(get_temperature, set_temperature)
          3 


    NameError: name 'get_temperature' is not defined



```python
### Method 2
# make empty property
temperature = property()
# assign getter
temperature = temperature.getter(get_temperature)
# assign setter
temperature = temperature.setter(set_temperature)
```


```python
### Method 3
class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

        

celc = Celsius()
celc.temperature = 100
print(celc.temperature)
# del(celc.temperature) # Need to explicitly define a deleter
# print(celc.temperature)

```

    Setting value
    Getting value
    100


Another example to 


```python
### Method 3
class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value
        
    @temperature.deleter
    def temperature(self):
        print("deleting the property")
        del(self._temperature)
        

celc = Celsius()
celc.temperature = 100
print(celc.temperature)
del(celc.temperature)
print(celc.temperature) # This property is no longer valid thus will error out

```

    Setting value
    Getting value
    100
    deleting the property
    Getting value



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-15-7c6f209207cd> in <module>()
         29 print(celc.temperature)
         30 del(celc.temperature)
    ---> 31 print(celc.temperature) # This property is no longer valid thus will error out
    

    <ipython-input-15-7c6f209207cd> in temperature(self)
         10     def temperature(self):
         11         print("Getting value")
    ---> 12         return self._temperature
         13 
         14     @temperature.setter


    AttributeError: 'Celsius' object has no attribute '_temperature'

