
# Functions as First-Class citizens

In functional programming, functions can be treated as objects. That is, they can be
- Assigned to a variable
- Passed as arguments to a function
- Returned from a functions

Lets look at few example to understand what that means.

Before we can play with functions, lets check how python handles the variables and data. For that we have taken a variable `a` and assigned it value 10. 


```python
a = 10
```

Now, lets check what happens if we pass it to functions `id` and `dir` in order to know more about them


```python
print(id(a))
print(dir(a))
```

    140400728229376
    ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']


In the above example, value `10` is behaving like an object, with multiple attributes exposed to the world.

Now lets do the same to a function and validate if that also behaves the same.

In the below example, we are creating a function `test_function` and then passed it to functions `id` and `dir` similar to what we did with the variable `a`.


```python
def test_function():
    """Test Function.
    
    This is just a test function.
    """
    pass


print(id(test_function))
print(dir(test_function))
```

    140400547816856
    ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']


We saw, that function also behaved the same way as an data, It also had a memory location identified for it and exposes various attributes to the world. Lets check few of them 


```python
print(test_function.__dir__())
print(test_function.__doc__)
print(test_function.__code__)
print(test_function.__class__)
```

    ['__repr__', '__call__', '__get__', '__new__', '__closure__', '__doc__', '__globals__', '__module__', '__code__', '__defaults__', '__kwdefaults__', '__annotations__', '__dict__', '__name__', '__qualname__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
    Test Function.
        
        This is just a test function.
        
    <code object test_function at 0x7fb188722db0, file "<ipython-input-3-9c7783901235>", line 1>
    <class 'function'>


## Pure function

One of the main feature of functional programming is `pure functions`. Lets find out what is `pure function`.

As per definition, pure function is a function which has no side effects and for the same input returns same output every time and is not dependent on any other information. As we have already discussed about them in previous chapter, we are going to skip it.

## higher-order function

Python also supports higher-order functions, meaning that functions can 
- accept other functions as arguments and 
- return functions to the caller

What that means is we can construct complex functions from existing functions and customize existing functions as per our needs. 

### Functions accept other functions as argument

Lets take example of simple example, 


```python
def done(val, func):
    val = val * 2
    return func(val)
    
def square(val):
    return val**2

def increment(val):
    return val + 1
```

In the above example, we have three functions, `done`, `square` and `increment`. 
- `done` takes two argument, `val` and `func`
- `square` & `increment` takes one val argument each

Since, both `square` & `increment` take one argument, they both can be passed to `done` and in both the cases the behaviour of `done` will change depending upon the `behaviour` of passed function.

Lets try it out.


```python
print(done(10, square))
```

    400


the reason we got `400` is due to the fact that square returns `square` of the number passed to it. In our case we passed `10` to done, which increased it to `20` before passing it to `square` function and inturn received square of `20` which equals to `400`.


```python
print(done(10, increment))
```

    21


the reason we got `21` is due to the fact that `increment` returns one move value than the number passed to it. In our case we passed `10` to `done`, which increased it to `20` before passing it to `increment` function and inturn received `21` from `increment`.

### Nested Functions

Python allows function(s) to be defined within the scope of another function. In this type of setting the inner function is only in scope inside the outer function, thus inner functions are returned (without executing) or passed into another function for more processing.

In the below example, a new instance of the function `inner()` is created on each call to `outer()`. That is because it is defined during the execution of `outer()`. The creation of the second instance has no impact on the first.

So, we have two functions, `outer` and `inner`. `outer` function returns the instance of `inner` function and inner function performs some operations on the values provided and returns them.


```python
def outer(a):
    """
    Outer function 
    """
    y = 0
    
    def inner(x):
        """
        inner function
        """
        y = x*x*a
        return(y)
    print(a)
    
    return inner

my_out = outer(10)
```

    10


In the above example, `my_out` contains the address of the instance of `inner` function when value of `a` is `102`. Lets check that out by just printing `my_out`


```python
print(my_out)
```

    <function outer.<locals>.inner at 0x7fb18866abf8>


Now, lets perform some operations on it by passing values to `my_out`.


```python
for i in range(5):
    print(my_out(i))
```

    0
    10
    40
    90
    160


In above for `loop` execution, value of `a` has remained constant and value of `x` has changed as shown in the below calculations. 


```python
0 * 0 * 10 == 0
```




    True




```python
1 * 1 * 10 == 10
```




    True




```python
2 * 2 * 10 == 40
```




    True




```python
3  * 3 * 10 == 90
```




    True




```python
4 * 4 * 10 == 160
```




    True



**Note** in all the above exeuction, we have used the same instance of outer. Now lets create another instance of outer and try the above code. 

Also note, that we have returned the address of inner functions instance and not executed the inner function while returning. The returned inner function gets executed later in the code.


```python
my_out_2 = outer(2)
```

    2



```python
for i in range(5):
    print(my_out_2(i))
```

    0
    2
    8
    18
    32


Now, we have two instances of `outer` with different values of `a` thus returns they both return different values for same set of code (except where we updated the value of `a`).

Lets take another example, and see what happens when we have identifiers with same name in differnet scopes


```python
x = 0

def outer():
    x = 1
    def inner():
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)

```

    inner: 2
    outer: 1
    global: 0


#### Problem with `local` and `global`

Lets take the above example, we have two functions, `outer` & `inner`. We also have `x` variable which is present as `global` and also present in both the functions.

If we want to access `x` of `outer` function from `inner` function than `global` keyword not help. Fortunately, Python provides a keyword `nonlocal` which allows `inner` functions to access variables to `outer` functions as shown in below example. 

The details of nonlocal are details in https://www.python.org/dev/peps/pep-3104/


```python
x = 0
def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
        print("inner:",x, "id:", id(x))

    inner()
    print("outer:",x, "id:", id(x))

outer()
print("global:",x, "id:", id(x))
```

    inner: 2 id: 140400728229120
    outer: 2 id: 140400728229120
    global: 0 id: 140400728229056



```python
def outer(a):
    """
    Outer function 
    """
    PI = 3.1415
    
    def inner(x):
        """
        inner function
        """
        nonlocal PI
        print(PI)
        y = x*PI*a 
        return("y =" + str(y))
    
    print(a)
    return inner
```


```python
ten = outer(10)
second = outer(20)
print("*"*20)
print(ten)
print(ten(10))
print("*"*20)
print(second)
print(second(10))
```

    10
    20
    ********************
    <function outer.<locals>.inner at 0x7fb18867a598>
    3.1415
    y =314.15000000000003
    ********************
    <function outer.<locals>.inner at 0x7fb188621d90>
    3.1415
    y =628.3000000000001


## Inner / Nested Functions - When to use 

### Encapsulation

You use inner functions to protect them from anything happening outside of the function, meaning that they are hidden from the global scope.


```python
# Encapsulation

def increment(current):
    def inner_increment(x):  # hidden from outer code
        return x + 1
    next_number = inner_increment(current)
    return [current, next_number]

print(increment(10))
```

    [10, 11]


> NOTE: We can not access directly the inner function as shown below


```python
try:
    increment.inner_increment(109)
except Exception  as e:
    print(e)
```

    'function' object has no attribute 'inner_increment'


### Following DRY (Don't Repeat Yourself)

This type can be used if you have a section of code base in function is repeated in numerous places. For example, you might write a function which processes a file, and you want to accept either an open file object or a file name:


```python
# Keepin’ it DRY
import os

def process(file_name):

    if isinstance(file_name, str):
        with open(file_name, 'r') as f:
            for line in f.readlines():
                print(line)
    else:
        for line in file_name:
            print(line)
        
process(["test", "test3", "t33"])
process(os.path.join("files", "process_me.txt"))
```

    test
    test3
    t33
    Hello
    
    Guten Tag
    
    Junge
    
    
    



```python
# Keepin’ it DRY
import os

def process(data):
    def do_stuff(file_process):
        for line in file_process:
            print(line)

    if isinstance(data, str):
        with open(data, 'r') as f:
            do_stuff(f)
    else:
        do_stuff(data)
        
process(["test", "test3", "t33"])
process(os.path.join("files", "process_me.txt"))
```

    test
    test3
    t33
    Hello
    
    Guten Tag
    
    Junge
    
    
    


or have similar logic which can be replaced by a function, such as mathematical functions, or code base which can be clubed by using some parameters.  


```python
def square(n):
    return n**2

def cube(n):
    return n**3

print(square(2))
```

    4



```python
def sqr(a, b):
    return a**b
```

> ??? why code


```python
def test():
    print("TEST TEST TEST")
    
    def yes(name):
        print("Ja, ", name)
        return True
    return yes

d = test()
print("*" * 14)
a = d("Murthy")
print("*" * 14)
print(a)
```

    TEST TEST TEST
    **************
    Ja,  Murthy
    **************
    True



```python
def power(exp):
    def subfunc(a):
        return a**exp
    return subfunc

square = power(2)
hexa = power(6)

print(square)
print(hexa)
print(square(5))  # 5**2
print()
print(hexa(3))  # 3**6
print(power(6)(3))
# subfunc(3) where exp = 6
# SQuare 

# exp -> 2 
# Square(5) 
# a -> 5 
# 5**2
# 25
```

    <function power.<locals>.subfunc at 0x7fb18867a268>
    <function power.<locals>.subfunc at 0x7fb188621400>
    25
    
    729
    729



```python
def a1(m):
    x = m * 2

    def b(v, t=None):
        if t:
            print(x, m, t)
            return v + t
        else:
            print(x, m, v)
            return v + x
    return b
n = a1(2)
print(n(3))
print(n(3, 10))
```

    4 2 3
    7
    4 2 10
    13


Below code will not work as `f1` is not returning anything :). This is to show what can happen with one silly tab. Also it is one of the most common mistake. 


```python
def f1(a):
    def f2(b):
        return f2
        def f3(c):
            return f3
            def f4(d):
                return f4
                def f5(e):
                    return f5
try:
    print (f1(1)(2)(3)(4)(5)) 
except Exception as e:
    print(e)
```

    'NoneType' object is not callable


The correct code is below


```python
def f1(a):
    def f2(b):
        def f3(c):
            def f4(d):
                def f5(e):
                    print(e)
                return f5
            return f4
        return f3
    return f2
        
f1(1)(2)(3)(4)(5)
```

    5


#### Closures & Factory Functions <sup>1</sup>

They are techniques for implementing lexically scoped name binding with first-class functions. It is a record, storing a function together with an environment. a mapping associating each free variable of the function (variables that are used locally, but defined in an enclosing scope) with the value or reference to which the name was bound when the closure was created.

A closure—unlike a plain function—allows the function to access those captured variables through the closure's copies of their values or references, even when the function is invoked outside their scope.


```python
def f(x):
    def g(y):
        return x + y
    return g

def h(x):
    return lambda y: x + y

a = f(1)
b = h(1)
print(a, b)
print(a(5), b(5))
print(f(1)(5), h(1)(5))
```

    <function f.<locals>.g at 0x7fb18868bea0> <function h.<locals>.<lambda> at 0x7fb18868b378>
    6 6
    6 6


both a and b are closures—or rather, variables with a closure as value—in both cases produced by returning a nested function with a free variable from an enclosing function, so that the free variable binds to the parameter x of the enclosing function. However, in the first case the nested function has a name, g, while in the second case the nested function is anonymous. The closures need not be assigned to a variable, and can be used directly, as in the last lines—the original name (if any) used in defining them is irrelevant. This usage may be deemed an "anonymous closure".

**1: Copied from** : "https://en.wikipedia.org/wiki/Closure_(computer_programming)"


```python
def make_adder(x):
    def add(y):
        return x + y
    return add

plus10 = make_adder(10)
print(plus10(12))  # make_adder(10).add(12)
print(make_adder(10)(12))
```

    22
    22


Closures can avoid the use of global values and provides some form of data hiding. It can also provide an object oriented solution to the problem.

When there are few methods (one method in most cases) to be implemented in a class, closures can provide an alternate and more elegant solutions. But when the number of attributes and methods get larger, better implement a class.


In functional programming, functions can be treated as objects. That is, they can assigned to a variable, can be passed as arguments or even returned from other functions.


```python
a = 10
def test_function():
    pass
print(id(a), dir(a))
print(id(test_function), dir(test_function))
```

    140400728229376 ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
    140400474504864 ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']


### The lambda

The lambda operator or lambda function is a way to create small anonymous functions, i.e. functions without a name. These functions are throw-away functions, i.e. they are just needed where they have been created. Lambda functions are mainly used in combination with the functions filter(), map() and reduce(). The lambda feature was added to Python due to the demand from Lisp programmers.

The general syntax of a lambda function is quite simple:

`lambda argument_list: expression`

The argument list consists of a comma separated list of arguments and the expression is an arithmetic expression using these arguments. You can assign the function to a variable to give it a name.
The following example of a lambda function returns the sum of its two arguments: 

The simplest way to initialize a pure function in python is by using `lambda` keyword. It helps in defining an one-line function. 

Functions initialized with lambda are also called **anonymous functions**.


```python
# Example lambda keyword
product_func = lambda x, y: x * y

print(product_func(10, 20))
print(product_func(120, 2))
```

    200
    240


In the above example higher-order function that takes two inputs- A function `F(x)` and a multiplier `m`.


```python
concat = lambda x, y: [x, y]

print(concat([1, 2, 3], 4))
```

    [[1, 2, 3], 4]



```python
print(concat({}, (2, 4)))
```

    [{}, (2, 4)]



```python
product_func = lambda x, y: x * y

sum_func = lambda F, m: lambda x, y: F(x, y) + m
```


```python
### TODO: some expl.
```


```python
print(sum_func(product_func, 6)(2, 4)) 
```

    14


```python
14 = 2 * 4 + 6
F -> product_func
m => 6
x -> 2
y -> 4
2 * 4 + 6 = 8 + 6 = 14
```


```python
print(sum_func)
```

    <function <lambda> at 0x7fb18868be18>



```python
print(sum_func(product_func, 5))
```

    <function <lambda>.<locals>.<lambda> at 0x7fb188621840>



```python
print(sum_func(product_func, 5)(3, 5))
```

    20


#### Use of Lambda Function

We use lambda functions when we require a nameless function for a short period of time.

In Python, we generally use it as an argument to a higher-order function (a function that takes in other functions as arguments). Lambda functions are used along with built-in functions like filter(), map() etc.

### Functions as Objects

Functions are first-class objects in Python, meaning they have attributes and can be referenced and assigned to variables.


```python
def square(x):
    """
    This returns the square of the requested number `x`
    """
    return x**2

print(square(10))
print(square(100))
```

    100
    10000


In the above example, we created a function `square` and tested it against two values `10` and `100`. Now lets assign a variable to the above function and play with it.


```python
# Assignation to another variable
power = square
print(power(100))
print(square)
print(power)
print(id(square))
print(id(power))
```

    10000
    <function square at 0x7fb1886218c8>
    <function square at 0x7fb1886218c8>
    140400474069192
    140400474069192


In the above execution, we can see that both `power` and `square` are pointing to same function `square`.  


```python
# attributes present
print("*"*30)
print(power.__name__)
print("*"*30)
print(square.__code__)
print("*"*30)
print(square.__doc__)
```

    ******************************
    square
    ******************************
    <code object square at 0x7fb188669d20, file "<ipython-input-45-52e68a4a6d18>", line 1>
    ******************************
    
        This returns the square of the requested number `x`
        


we can see that functions also have attributes, we can see the list of attributes exposed by using the code with syntax `dir(<func_name>)`.


```python
print(dir(square))
```

    ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']


### Adding attributes to a function

We can also add attributes to a function. In the below example we are addting attribute `d` to the function


```python
square.d = 10
print(dir(square))
```

    ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'd']


In the above example higher-order function that takes two inputs- A function `F(x)` and a multiplier `m`.

### In-built Higher Order Functions

Python provides many functions which can also act as higher order functions. We are going to cover few of them in this section.

#### `max()`

Max returns the largest item in an iterable or the largest of two or more arguments.

If one positional argument is provided, iterable must be a non-empty iterable (such as a non-empty string, tuple or list). The largest item in the iterable is returned. If two or more positional arguments are provided, the largest of the positional arguments is returned.

The optional key argument specifies a one-argument ordering function like that used for list.sort(). The key argument, if supplied, must be in keyword form (for example, max(a,b,c,key=func)).

**Example**: Basic Example


```python
marks = [[1, 2], [2, 1], [2, 4], [3, 0], [3, 4], [3, 2]]
max(marks)
```




    [3, 4]




```python
marks = [1, 2, 4, 2, (5)]
max(marks)
```




    5




```python
try:
    marks = [1, 2, 4, 2, (5, 1)]
    max(marks)
except Exception as e:
    print(e)
```

    '>' not supported between instances of 'tuple' and 'int'



```python
try:
    marks = [1, 2, 4, 2, [5]]
    max(marks)
except Exception as e:
    print(e)
```

    '>' not supported between instances of 'list' and 'int'


Now lets take an excercise, below are the marks for students for 8 semesters, and we need to find what is the highest marks in 3rd semester.


```python
import random
student_count = 10000
max_marks = 100
min_marks = 0
semester = 8
marks = [[random.randint(min_marks, max_marks) for _ in range(semester)] for _ in range(student_count)]
```


```python
print(marks[:3])
```

    [[93, 26, 9, 84, 13, 52, 15, 9], [19, 99, 18, 0, 3, 86, 25, 89], [37, 79, 22, 9, 24, 14, 99, 48]]


we can achive it by using `itemgetter` from `operator` modules, which we have used in the past.


```python
import operator

print("Max number is each semester are as follows:")
for a in range(semester):
    print('\t', max(marks, key = operator.itemgetter(a))[a])
```

    Max number is each semester are as follows:
    	 100
    	 100
    	 100
    	 100
    	 100
    	 100
    	 100
    	 100


As we have passed `operator.itemgetter` function as key, we can pass some custom function as well.

Now lets assume a situation, were we have to calculate total marks, which are calculated as sum of 10% of first 6 semesters and 100% of 7th & 8th semester and we wants to find the highest mark obtained for the year 1994 batch.


```python
# %%timeit
def marks_sum_v1(marks_list):
    total = 0
    for a in range(5):
        total += marks_list[a] 
    total *= 0.1
    for a in range(6, 8):
        total += marks_list[a]
    return total

marks_sum_v1(max(marks, key = marks_sum_v1))
```




    239.4




```python
print('Maximum marks:\t', marks_sum_v1(max(marks, key = marks_sum_v1)))
```

    Maximum marks:	 239.4



```python
# %%timeit

def marks_sum_v2(marks_list):
    total = 0
    
    total = sum(marks_list[a] * 0.1 for a in range(5))
    total += sum([marks_list[a] for a in range(6, 8)])
    return total


marks_sum_v2(max(marks, key=marks_sum_v2))
```




    239.4




```python
# %%timeit

def marks_sum_v2(marks_list):
    total = sum((sum(marks_list[a] for a in range(6, 8)), 
                 sum(marks_list[a] * 0.1 for a in range(5))))
    return total

marks_sum_v2(max(marks, key=marks_sum_v2))
```




    239.4



Similarly we can also use lambda in key variable.

Lets, take another example, we are conducting games, where teams have to perform few tasks and after each task they are provided some points. The team with highest score wins. 

Its our job to write an script which will take the scores (which are stored as list of lists) and provided what is the maximum score. 

In our solution, we will use `lambda` function to get the total of scores


```python
scores = [[14, 19, 96, 91, 32, 65, 87, 27], [11, 37, 22, 93, 75, 11, 95, 95], 
         [14, 54, 92, 72, 13, 17, 44, 73], [17, 31, 82, 80, 40, 4, 11, 8], 
         [86, 83, 85, 93, 85, 42, 22, 87], [44, 61, 17, 87, 21, 35, 90, 10],
         [75, 27, 67, 88, 22, 84, 4, 51], [28, 25, 66, 22, 46, 56, 76, 47], 
         [24, 98, 16, 20, 92, 5, 40, 12]]

results = []
for a in scores:
    results.append(sum(a))

print(results)
print(max(results))
```

    [431, 439, 379, 273, 583, 365, 418, 366, 307]
    583



```python
sum(max(scores, key=lambda x: sum(x)))
```




    583



#### min()

Similer to `max`, `min` also provide the same functionality. thus is not covering in it in details except one example


```python
import random
student_count = 10000
max_marks = 100
min_marks = 0
semester = 8
marks = [[random.randint(min_marks, max_marks) for _ in range(semester)] for _ in range(student_count)]
```


```python
def marks_sum_v1(marks_list):
    total = 0
    for a in range(5):
        total += marks_list[a] 
    total *= 0.1
    for a in range(6, 8):
        total += marks_list[a] * 1
    return total

d = round(marks_sum_v1(min(marks, key = marks_sum_v1)),2)
print(d)
```

    16.4

