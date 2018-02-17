
# Decorators
---
## ONLY AFTER FP
A decorator is the name used for a software design pattern. Decorators dynamically alter the functionality of a function, method, or class without having to directly use subclasses or change the source code of the function being decorated.

Python decorator is a specific change to the Python syntax that allows us to more conveniently alter functions and methods (and possibly classes in a future version). This supports more readable applications of the DecoratorPattern but also other uses as well.


```python
# sandwich()
# test = bread(ingredients(Cheese))
# test()

# # bread_1 = ingredients(Cheese)
# # print(bread_1)
# # bread_1()
```


```python
def bread(test_funct):
    def hyderabad():
        print("</''''''\>")
        test_funct()
        print("<\______/>")
    return hyderabad

def ingredients(test_funct):
    def chennai():
        print("#tomatoes#")
        test_funct()
        print("~salad~")
    return chennai

def cheese(food="--Say Cheese--"):
    print(food)

```


```python
ch = bread(cheese)

inn = bread(ingredients(cheese))

ch()
print("^"*20)
inn()
```

    </''''''\>
    --Say Cheese--
    <\______/>
    ^^^^^^^^^^^^^^^^^^^^
    </''''''\>
    #tomatoes#
    --Say Cheese--
    ~salad~
    <\______/>



```python
@bread
@ingredients
def sandwich(food="--Say Cheese--"):
    print(food)

sandwich()
```

    </''''''\>
    #tomatoes#
    --Say Cheese--
    ~salad~
    <\______/>


> ***!!! Order Matters !!!*** 


```python
@ingredients
@bread
def sandwich(food="--Say Cheese--"):
    print(food)

sandwich()
```

    #tomatoes#
    </''''''\>
    --Say Cheese--
    <\______/>
    ~salad~



```python
@bread
@ingredients
def hotdog(food="Jam"):
    print(food)

hotdog()
```

    </''''''\>
    #tomatoes#
    Jam
    ~salad~
    <\______/>



```python
def Names(test_funct):
    def inner():
        print("{Hello}")
        print("\tA-Priya")
        print("\tManish Gupta")
        print("\tNeha", end="\n\t")
        test_funct()
        print("(/Hello}")
    return inner

@Names
def print_AShanti():
    print("A-Shanti")

print_AShanti()
```

    {Hello}
    	A-Priya
    	Manish Gupta
    	Neha
    	A-Shanti
    (/Hello}



```python
def names(test_funct):
    def inner():
        print("\t", name)
        test_funct()
    return inner()

def Hello(test_funct):
    def inner():
        print("{Hello}")
        print("\tA-Priya")
        print("\tManish Gupta")
        print("\tNeha", end="\n\t")
        test_funct()
        print("(/Hello}")
    return inner

@Hello
@names(name="Mayank")
def print_AShanti():
    print("A-Shanti")

print_AShanti()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-10-90733c8b1b9d> in <module>()
         16 
         17 @Hello
    ---> 18 @names(name="Mayank")
         19 def print_AShanti():
         20     print("A-Shanti")


    TypeError: names() got an unexpected keyword argument 'name'


## Bound methods
---

Unless you tell it not to, Python will create what is called a bound method when a function is an attribute of a class and you access it via an instance of a class. This may sound complicated but it does exactly what you want.


```python
class A(object):
    def method(*argv):
        return argv
a = A()
a.method

```




    <bound method A.method of <__main__.A object at 0x00000234D70DB8D0>>




```python
a.method('an arg')
```




    (<__main__.A at 0x234d70db8d0>, 'an arg')



### staticmethod()

A static method is a way of suppressing the creation of a bound method when accessing a function.


```python
class A(object):
    @staticmethod
    def method(*argv):
        return argv
a = A()
a.method
```




    <function __main__.A.method>



When we call a static method we don’t get any additional arguments.


```python
a.method('an arg')
```




    ('an arg',)



### classmethod

A class method is like a bound method except that the class of the instance is passed as an argument rather than the instance itself.


```python
class A(object):
    @classmethod
    def method(*argv):
        return argv
a = A()
a.method
```




    <bound method A.method of <class '__main__.A'>>




```python
a.method('an arg')
```




    (__main__.A, 'an arg')




```python
def test(strg):
    print("Name: ", strg)
    
def hello(func, name):
    print("Ja")
    func(name)
    
hello(test, "Mayank")
```

    Ja
    Name:  Mayank



```python
class B(object):
    @classmethod
    def method(*argv):
        return argv
```


```python
a = B()
a.method()
```




    (__main__.B,)


