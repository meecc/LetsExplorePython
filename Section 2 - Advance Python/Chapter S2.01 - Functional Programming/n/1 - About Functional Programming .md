
# Section 1 - About Functional Programming 
---




## What is Functional Programming

Functional programming is a programming paradigm that revolves around **pure functions**. 
A **pure function** is a function which can be represented as a mathematical expression. That means, no **side-effects** should be present, i.e. no I/O operations, no global state changes, no database interactions. 

<img src="files/PureFunction.png" width="500" alt="Pure Function Representation">

The output from a pure function is depended **ONLY** on its inputs. Thus, if a pure function is called with the same inputs a million times, you would get the same result every single time.


```python
# not so functional function
a = 0

def global_sum(x):
    global a
    x += a
    return x

print(global_sum(1))
print(a)
a = 11
print(global_sum(1))
print(a)
```

    1
    0
    12
    11



```python
# not so functional function
a = 0

def global_sum(x):
    global a
    return x + a

print(global_sum(x=1))
print(a)
a = 11
print(global_sum(x=1))
print(a)
```

    1
    0
    12
    11


In the above example, the output of the function `global_sum` changed due to the value of `a`, thus it is unfunctional function.


```python
# a better functional function
def better_sum(a, x):
    return a+x

num = better_sum(1, 1)
print(num)
num = better_sum(1, 3)
print(num)
num = better_sum(1, 1)
print(num)
```

    2
    4
    2


and in the above example `better_sum`, the function returns always the same value for the set of input and only provided input can have any impact on the output of the function.

  ## Characteristics of functional programming

- **Functions are first class (objects)**. So, data and functions are treated as same and have access to same operations(such as passing a function to another function).
- Recursion as primary control structure.
- There is a focus on LISt Processing and are often used with recursion on sub-lists as a substitute for loops.
- Avoid "side-effects". It excludes the almost ubiquitous pattern in imperative languages of assigning first one, then another value to the same variable to track the program state.
- Either discourages or outright disallows statements, and instead works with the evaluation of expressions (in other words, functions plus arguments). In the pure case, one program is one expression (plus supporting definitions).
- FP worries about what is to be computed rather than how it is to be computed.
- Much FP utilizes "higher order" functions (in other words, functions that operate on functions that operate on functions).

## Functions as First-Class citizens

In functional programming, functions can be treated as objects. That is, they can assigned to a variable, can be passed as arguments or even returned from other functions.


```python
a = 10
def test_function():
    pass
print(id(a), dir(a))
print(id(test_function), dir(test_function))
```

    1798467328 ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
    2309665771728 ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']


### The lambda

The simplest way to initialize a pure function in python is by using `lambda` keyword, which helps in defining the one-line function. Functions initialized with lambda can often called `anonymous functions`


```python
# Example lambda keyword

product_func = lambda x, y: x*y

print(product_func(10, 20))
print(product_func(10, 2))
```

    200
    20



```python
concat = lambda x, y: [x, y]

print(concat([1,2,3], 4))
```

    [[1, 2, 3], 4]


### Functions as Objects

Functions are first-class objects in Python, meaning they have attributes and can be referenced and assigned to variables.


```python
def square(x):
    """
    This returns the square of the requested number `x`
    """
    return x**2

print(square(10))
```

    100



```python
print(square(100))
```

    10000



```python
# Assignation to another variable
mySquare = square
print(mySquare(100))
print(square)
print(mySquare)
print(id(square))
print(id(mySquare))
```

    10000
    <function square at 0x00000219C2D6B268>
    <function square at 0x00000219C2D6B268>
    2309666288232
    2309666288232



```python
# attributes present
print("*"*30)
print(dir(square))
print("*"*30)
print(mySquare.__name__)
print("*"*30)
print(square.__code__)
print("*"*30)
print(square.__doc__)
```

    ******************************
    ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'd']
    ******************************
    square
    ******************************
    <code object square at 0x00000219C2D5AE40, file "<ipython-input-6-37fb4737804d>", line 1>
    ******************************
    
        This returns the square of the requested number `x`
        


### Adding attributes to a function


```python
square.d = 10
print(dir(square))
```

    ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'd']


### higher-order function

Python also supports higher-order functions, meaning that functions can accept other functions as arguments and return functions to the caller.


```python
print(square(square(square(2))))
```

    256



```python
product_func = lambda x, y: x*y

sum_func = lambda F, m: lambda x, y: F(x, y)+m

print(sum_func(product_func, 5)(2, 4)) 
```

    13



```python
print(sum_func)
```

    <function <lambda> at 0x7f1b2c089cf8>



```python
print(sum_func(product_func, 5))
```

    <function <lambda> at 0x7f1b2c089f50>



```python
print(sum_func(product_func, 5)(3, 5))
```

    20


`13=2*4+5
F -> product_func
m => 5
x -> 2
y -> 4
2*4+5 = 8+5 = 13`

In the above example higher-order function that takes two inputs- A function `F(x)` and a multiplier `m`.

### Nested Functions

In Python, Function(s) can also be defined within the scope of another function. If this type of function definition is used the inner function is only in scope inside the outer function, so it is most often useful when the inner function is being returned (moving it to the outer scope) or when it is being passed into another function.

Notice that in the below example, a new instance of the function `inner()` is created on each call to `outer()`. That is because it is defined during the execution of `outer()`. The creation of the second instance has no impact on the first.


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

my_out = outer
```


```python
my_out(102)
```

    102





    <function __main__.outer.<locals>.inner>




```python
o = outer(10)
b = outer(20)
print("*"*20)
print(b)
print(o)
print("*"*20)
print(o(10))
print(b(10))
```

    10
    20
    ********************
    <function outer.<locals>.inner at 0x00000219C2D82158>
    <function outer.<locals>.inner at 0x00000219C2D6B510>
    ********************
    1000
    2000



```python
def outer():
    """
    Outer function 
    """
    if 'a' in locals():
        a +=10
    else:
        print("~"),
        a = 20
    def inner(x):
        """
        inner function
        """
        return(x*x*a)
    print(a)
    return inner

# oo = outer
# print(oo.__doc__)
o = outer()
print("*"*20)
print(o)
print(o(10))
print(o.__doc__)
```

    ~ 20
    ********************
    <function inner at 0x7f1b2c040758>
    2000
    
            inner function
            



```python
b = outer()
print(b)
print(b(30))
print(b.__doc__)
```

    ~ 20
    <function inner at 0x7f1b2c0405f0>
    18000
    
            inner function
            



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



```python
x = 0
def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)

# inner: 2
# outer: 2
# global: 0
```

    inner: 2
    outer: 2
    global: 0



```python
def outer(a):
    """
    Outer function 
    """
    y = 1
    def inner(x):
        """
        inner function
        """
        nonlocal y
        print(y)
        y = x*x*a 
        return("y =" + str(y))
    print(a)
    return inner

o = outer(10)
b = outer(20)
print("*"*20)
print(o)
print(o(10))
print("*"*20)
print(b)
print(b(10))
```


      File "<ipython-input-26-5cfd9ea35045>", line 10
        nonlocal y
                 ^
    SyntaxError: invalid syntax



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


> NOTE: We can not access directly the inner function


```python
increment.inner_increment(109)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-36-7551cfbae1c8> in <module>()
    ----> 1 increment.inner_increment(109)
    

    AttributeError: 'function' object has no attribute 'inner_increment'



```python
### NOT WORKING

def update(str_val):
    def updating(ori_str, key, value):
        token = "$"
        if key in ori_str:
            ori_str = ori_str.replace(token+key, value)
        return ori_str
    
    keyval = [{"test1": "val_test", "t1" : "val_1"}, {"test2": "val_test2", "t2" : "val_2"}]

    keyval1 = [{"test1": "val_test", "t1" : "val_1"}, {"test2": "val_test2", "t2" : "val_2"}]
    ori_str = "This is a $test1 and $test2, $t1 and $t2"
    
#     for k in keyval:
#         for key, value in k.items():
#             ori_str = updateing(ori_str, key, value)
    
    sdd = [ key, value [for key, value in k] for(k in keyval) ]
    
    print(ori_str)
    
update("D")
```


      File "<ipython-input-11-4c5edce7660a>", line 17
        sdd = [ key, value [for key, value in k] for(k in keyval) ]
                              ^
    SyntaxError: invalid syntax




```python
ld = [{'a': 10, 'b': 20}, {'p': 10, 'u': 100}]
[kv for d in ld for kv in d.items()]
```




    [('a', 10), ('b', 20), ('p', 10), ('u', 100)]




```python
ori_str = "This is a $test;1 and $test2, $t1 and $t2"
print(ori_str.replace("test1", "TEST1"))
print(ori_str)
```

    This is a $TEST1 and $test2, $t1 and $t2
    This is a $test1 and $test2, $t1 and $t2


### Following DRY (Don't Repeat Yourself)

This type can be used if you have a section of code base in function is repeated in numerous places. For example, you might write a function which processes a file, and you want to accept either an open file object or a file name:


```python
# Keepin’ it DRY

def process(file_name):
    def do_stuff(file_process):
        for line in file_process:
            print(line)

    if isinstance(file_name, str):
        with open(file_name, 'r') as f:
            do_stuff(f)
    else:
        do_stuff(file_name)
        
process(["test", "test3", "t33"])do_stuff(file_name)
        
process("test.txt")
```

    test
    test3
    t33



    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-51-6cab43fac967> in <module>()
         14 process(["test", "test3", "t33"])
         15 
    ---> 16 process("test.txt")
    

    <ipython-input-51-6cab43fac967> in process(file_name)
          7 
          8     if isinstance(file_name, str):
    ----> 9         with open(file_name, 'r') as f:
         10             do_stuff(f)
         11     else:


    FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'


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
    print("TESTTESTTEST")
    def yes(name):
        print("Ja, ", name)
        return True
    return yes

d = test()
print("XSSSS")
print(d("Venky"))
```

    TESTTESTTEST
    XSSSS
    Ja,  Venky
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

print(square(5)) # 5**2
print()
print(hexa(3)) # 3**6
print(power(6)(3))
# subfunc(3) where exp = 6
# SQuare 

# exp -> 2 
# Square(5) 
# a -> 5 
# 5**2
# 25
```

    <function power.<locals>.subfunc at 0x00000219C2D6BB70>
    <function power.<locals>.subfunc at 0x00000219C2D6BEA0>
    25
    
    729
    729



```python
 Power(6)(3, x)
```


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
print (f1(1)(2)(3)(4)(5)) 
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-52-8b5968dce991> in <module>()
          8                 def f5(e):
          9                     return f5
    ---> 10 print (f1(1)(2)(3)(4)(5))
    

    TypeError: 'NoneType' object is not callable



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

    <function f.<locals>.g at 0x000001ECFA3A3268> <function h.<locals>.<lambda> at 0x000001ECFA3A3598>
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

### Comprehensions


Using comprehensions is often a way both to make code more compact and to shift our focus from the "how" to the "what". It is an expression that uses the same keywords as loop and conditional blocks, but inverts their order to focus on the data rather than on the procedure. 

Simply changing the form of expression can often make a surprisingly large difference in how we reason about code and how easy it is to understand. The ternary operator also performs a similar restructuring of our focus, using the same keywords in a different order.

####  List Comprehensions

A way to create a new list from existing list based on defined logic

* **Unconditional Compreshensions** 


```python
# Original
doubled_numbers = []
for n in range(1,6):
    doubled_numbers.append(n*2)

print(doubled_numbers)
```

    [2, 4, 6, 8, 10]



```python
#list compreshensions
doubled_numbers = [n * 2 for n in range(1,12,2)] # 1 ,3, 5, 7, 9, 11
print(doubled_numbers)
```

    [2, 6, 10, 14, 18, 22]


* **Conditional Compreshensions** 


```python
doubled_odds = []

for n in range(1,12):
    if n % 2 == 1:
        doubled_odds.append(n * 2)
print(doubled_odds)
```

    [2, 6, 10, 14, 18, 22]



```python
doubled_odds = [n * 2 for n in range(1,12) if n% 2 == 1]

print(doubled_odds)
```

    [2, 6, 10, 14, 18, 22]


** !!!! Tip !!!! ** 

* Copy the variable assignment for our new empty list (line 3)
* Copy the expression that we’ve been append-ing into this new list (line 6)
* Copy the for loop line, excluding the final `:` (line 4)
* Copy the if statement line, also without the `:` (line 5)



```python
# FROM
numbers = range(2,10)

doubled_odds = []
for n in numbers:
    if n % 2 == 1:
        doubled_odds.append(n * 2)
print(doubled_odds)
```

    [6, 10, 14, 18]



```python
# TO
numbers = range(2,10)

doubled_odds = [n * 2 for n in numbers if n % 2 == 1]

```

    [6, 10, 14, 18]


### Nested `if` statements in `for` loop


```python
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]

lst = []
for v in l:
    if v == 0 :
        lst.append ('Zero')
    else:
        if v % 2 == 0:
            lst.append  ('even')
        else:
            lst.append  ('odd')
            
print(lst)
```

    ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'Zero']



```python
lst = ["zero" if v == 0 else "even" if v%2 == 0 else "odd" for v in l]
print(lst)
```

    ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'zero']



```python
print(['yes' if v == 1 else 'no' if v == 2 else 'idle' for v in l])
```

    ['yes', 'no', 'idle', 'idle', 'idle', 'idle', 'idle', 'idle', 'idle', 'idle', 'idle']



```python
# def flatten_list_new(lst, result=None):
#     """Flattens a nested list
#         >>> flatten_list([ [1, 2, [3, 4] ], [5, 6], 7])
#         [1, 2, 3, 4, 5, 6, 7]
#     """
# #     if result is None:
# #         result = []
# #     else:
#     result = [x if not isinstance(x, list) else flatten_list_new(x, list) for x in lst]
# #     result = [ x  if not isinstance(x, list) else isinstance(x, list) for x in lst ]
# #     result = [x for x in a if not isinstance(x, list) else isinstance(x, list)]
# #     for x in a:
# #         if isinstance(x, list):
# #             flatten_list(x, result)
# #         else:
# #             result.append(x)

#     return result
# lst = [ [1, 2, [3, 4] ], [5, 6], 7]

# print(flatten_list_new(lst))
```


```python
lst = []
for a in range(10):
    if a % 2==0:
        for x in range(a, 10):
            lst.append(x)
print(lst)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 4, 5, 6, 7, 8, 9, 6, 7, 8, 9, 8, 9]



```python
n = 10
lsts = [x for a in range(10) if a % 2==0 for x in range(a, 10) ]
print(lsts)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 4, 5, 6, 7, 8, 9, 6, 7, 8, 9, 8, 9]



```python
n = 10
lsts = [x for a in range(10) 
            if a % 2==0 
                for x in range(a, 10) ]
print(lsts)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 4, 5, 6, 7, 8, 9, 6, 7, 8, 9, 8, 9]



```python
%%time
import os

files = []

for d in os.walk(r"E:\code\mj\lep\Section 1 - Core Python"):
    for f in d[2]:
        if f.endswith(".py"):
            files.append(os.path.join(d[0], f))

print(len(files))
```

    134
    Wall time: 49.2 ms



```python
%%time

import os

files = [os.path.join(d[0], f) 
            for d in os.walk(r"E:\code\mj\lep\Section 1 - Core Python")
                 for f in d[2] if f.endswith(".py")]

print(len(files))
```

    134
    Wall time: 48.3 ms



```python
%%time

import os

files = [os.path.join(d[0], f) 
            for d in os.walk(r"E:\code\mj\lep\Section 1 - Core Python")
                 for f in d[2]  if f.endswith(".py")]

print(len(files))
```

    134
    Wall time: 54.5 ms



```python
%%time
restFiles = []

for d in os.walk(r"C:\apps\PortableGit"):
    if "etc" in d[0]:
        for f in d[2]:
            if f.endswith(".exe"):
                restFiles.append(os.path.join(d[0], f))
print(len(restFiles))
```

    0
    Wall time: 582 µs



```python
%%time
restFiles = [os.path.join(d[0], f) 
                 for d in os.walk(r"C:\apps\PortableGit") 
                     if "etc" in d[0]
                         for f in d[2] 
                             if f.endswith(".exe")]
print(len(restFiles))
```

    0
    Wall time: 1.08 ms



```python
%%time

matrix = []
for row_idx in range(0, 3):
    itmList = []
    for item_idx in range(0, 3):
        if item_idx == row_idx:
            itmList.append(1)
        else:
            itmList.append(0)
    matrix.append(itmList)
print(matrix)
```

    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    Wall time: 0 ns



```python
matrix = [ [ 1 if item_idx == row_idx 
               else 0 for item_idx in range(0, 3)] 
          for row_idx in range(0, 3) ]
print(matrix)
```

    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]



```python
matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
        ]
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)
```

    [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]



```python
transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)
```

    [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]



```python
lst = [1,2,34,4,5]
print(lst)
lst.append(2)
print(lst)
```

    [1, 2, 34, 4, 5]
    [1, 2, 34, 4, 5, 2]



```python

lst.append(2)
print(lst)
l = set(lst)
print(l)
```

    [1, 2, 34, 4, 5, 2, 2, 2]
    {1, 2, 34, 4, 5}


### Set Comprehensions

Set comprehensions allow sets to be constructed using the same principles as list comprehensions, the only difference is that resulting sequence is a set and **"{}"** are used instead of **"[]"**.


```python
names = [ 'aaLok', 'Manish', 'aalOk', 'Manish', 'Gupta', 'Johri', 'Mayank' ]

new_names1 = [name[0].upper() + name[1:].lower() for name in names if len(name) > 1 ]
new_names = {name[0].upper() + name[1:].lower() for name in names if len(name) > 1 }
print(new_names1)
print(new_names)
```

    ['Aalok', 'Manish', 'Aalok', 'Manish', 'Gupta', 'Johri', 'Mayank']
    {'Aalok', 'Manish', 'Gupta', 'Mayank', 'Johri'}



```python
        done_urls.append(url)
    urls = set(urls)
    left_urls = list(urls.difference(done_urls))

```

### Dictionary Comprehensions


```python
original = {'a':10, 'b': 34, 'A': 7, 'Z':3, "z": 199}

mcase_frequency = { k.lower() : original.get(k.lower(), 0) + original.get(k.upper(), 0) for k in original.keys() }
print(mcase_frequency)
```

    {'a': 17, 'b': 34, 'z': 202}



```python
original = {'a':10, 'b': 34, 'A': 7, 'Z':3, "z": 199, 'c': 10}
flipped = {value: key for key, value in original.items()}
print(flipped)
```

    {3: 'Z', 10: 'c', 199: 'z', 34: 'b', 7: 'A'}



```python
original = {'a': 10, 'b': 34, 'A': 7, 'Z':3, "z": 199, 'c': 10}
newdict = {}
for key, value in original.items():
    if (value not in newdict):
        newdict[value] = key
print(newdict)
```

    {10: 'a', 34: 'b', 7: 'A', 3: 'Z', 199: 'z'}



```python
newdict = {value: key for key, value in original.items() if (value not in newdict)}
print(newdict)
```

    {10: 'c', 34: 'b', 7: 'A', 3: 'Z', 199: 'z'}



```python
x = {"a": 10, "b": 20, "c": 20}

print(x)
x["a"] = 100

print(x)
```

    {'a': 10, 'b': 20, 'c': 20}
    {'a': 100, 'b': 20, 'c': 20}


This map doesn’t take a named function. It takes an anonymous, inlined function defined with lambda. The parameters of the lambda are defined to the left of the colon. The function body is defined to the right of the colon. The result of running the function body is (implicitly) returned.

The unfunctional code below takes a list of real names and appends them with randomly assigned code names.


```python
import random

names_dict = {}
names = ["Mayank", "Manish", "Aalok", "Roshan Musheer"]
code_names = ['Mr. Normal', 'Mr. God', 'Mr. Cool', 'The Big Boss']

random.shuffle(code_names)

for i in range(len(names)):
    names_dict[names[i]] = code_names[i] 
        
print(names_dict)
```

    {'Mayank': 'Mr. Normal', 'Manish': 'Mr. God', 'Aalok': 'Mr. Cool', 'Roshan Musheer': 'The Big Boss'}



```python
random.shuffle(code_names)
new_dict = {names[i] : code_names[i] for i in range(len(names))}
print(new_dict)
```

    {'Mayank': 'Mr. Normal', 'Manish': 'The Big Boss', 'Aalok': 'Mr. God', 'Roshan Musheer': 'Mr. Cool'}



```python
import random

names_dict = {}
names = ["Mayank", "Manish", "Aalok", "Roshan Musheer"]
code_names = ['Mr. Normal', 'Mr. God', 'Mr. Cool', 'The Big Boss']

random.shuffle(code_names)
d = list(zip(names, code_names))
print(d)
names_dict = dict(d)

print(names_dict)
```

    [('Mayank', 'Mr. God'), ('Manish', 'Mr. Cool'), ('Aalok', 'The Big Boss'), ('Roshan Musheer', 'Mr. Normal')]
    {'Mayank': 'Mr. God', 'Manish': 'Mr. Cool', 'Aalok': 'The Big Boss', 'Roshan Musheer': 'Mr. Normal'}


### Generator Comprehension

They are simply a generator expression with a parenthesis "()" around it. Otherwise, the syntax and the way of working is like list comprehension, but a generator comprehension returns a generator instead of a list. 


```python
x = (x**2 for x in range(20))
print(x)
print(list(x))
```

    <generator object <genexpr> at 0x0000029F7563E2B0>
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]



```python
itm = 10
print(itm / 2)
```

    5.0


#### Summary

When struggling to write a comprehension, `don’t panic`. Start with a for loop first and copy-paste your way into a comprehension.

Any for loop that looks like this:


```python
def condition_based_on(itm):
    return itm % 2 == 0

old_things = range(2,20, 3)
new_things = []
for ITEM in old_things:
    if condition_based_on(ITEM):
        new_things.append(ITEM)
print(new_things)
```

    [2, 8, 14]


Can be rewritten into a list comprehension like this:


```python
new_things = [ITEM for ITEM in old_things if condition_based_on(ITEM)]
print(new_things)
```

    [2, 8, 14]


**NOTE**

If you can nudge a for loop until it looks like the ones above, you can rewrite it as a list comprehension.

### Recursion

In Functional programming iteration such as `while` or `for` statements are avoided. Also it does not have the provision of state-updates. 
In FP recursion is used to overcome iterations, since any iterative code can be converted to recursive code as shown in the below examples.


```python
def fib(n):
    # the first two values
    l = [1, 1]
    
    # Calculating the others
    for i in range(2, n + 1):
        l.append(l[i -1] + l[i - 2])
        
    return l[n]

# Show Fibonacci from 1 to 5
for i in [1, 2, 3, 4, 5]:
    print (i, '=>', fib(i))
```

    1 => 1
    2 => 2
    3 => 3
    4 => 5
    5 => 8



```python
def fib(n):
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return 1

# Show Fibonacci from 1 to 5
for i in range(1,6):
    print (i, '=>', fib(i))
```

    1 => 1
    2 => 2
    3 => 3
    4 => 5
    5 => 8


or, using `lambda`


```python
fibonacci = (lambda x, x_1=1, x_2=0:
         x_2 if x == 0
         else fibonacci(x - 1, x_1 + x_2, x_1))

print(fibonacci(10))
```

    55


### map, reduce and filter

These are three functions which facilitate a functional approach to programming. `map`, `reduce` and `filter` are three higher-order functions that appear in all pure functional languages including Python. They are often are used in functional code to make it more elegant.

#### Map


It basically provides kind of parallelism by calling the requested function over all elements in a list/array or in other words, 
Map applies a function to all the items in the given list and returns a new list.

It takes a function and a collection of items as parameters and makes a new, empty collection, runs the function on each item in the original collection and inserts each return value into the new collection. It then returns the updated collection.

This is a simple map that takes a list of names and returns a list of the lengths of those names:


```python
names = ["Manish Kumar", "Aalok", "Mayank Johri","Durgaprasad"]

lst = []
for name in names:
    lst.append(len(name))
    
print(lst)
```

    [12, 5, 12, 11]



```python
names = ["Manish Kumar", "Aalok", "Mayank Johri","Durgaprasad"]

tmp = map(len, names)
print(tmp)
lst = tuple(tmp)

print(lst)
# This is a map that squares every number in the passed collection:
power = map(lambda x: x*x, lst)
print(power)
print(list(power))
```

    <map object at 0x00000246F5C6F160>
    (12, 5, 12, 11)
    <map object at 0x00000246F5C6F2B0>
    [144, 25, 144, 121]



```python
help(map)
```

    Help on class map in module builtins:
    
    class map(object)
     |  map(func, *iterables) --> map object
     |  
     |  Make an iterator that computes the function using arguments from
     |  each of the iterables.  Stops when the shortest iterable is exhausted.
     |  
     |  Methods defined here:
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __next__(self, /)
     |      Implement next(self).
     |  
     |  __reduce__(...)
     |      Return state information for pickling.
    



```python
list(map(pow,[2, 3, 4], [10, 11, 12]))
```




    [1024, 177147, 16777216]




```python
import random

names_dict = {}
names = ["Mayank", "Manish", "Aalok", "Roshan Musheer"]
code_names = ['Mr. Normal', 'Mr. God', 'Mr. Cool', 'The Big Boss']

for i in range(len(names)):
#     name = random.choice(code_names)
    while name in names_dict.values():
        name = random.choice(code_names)
    names_dict[names[i]] = name 
        
print(names_dict)
```

    {'Manish': 'The Big Boss', 'Aalok': 'Mr. Cool', 'Roshan Musheer': 'Mr. God', 'Mayank': 'Mr. Normal'}


This can be rewritten as a lamba:


```python
import random

names = ["Mayank", "Manish", "Aalok", "Roshan Musheer"]
code_names = ['Mr. Normal', 'Mr. God', 'Mr. Cool', 'The Big Boss']
random.shuffle(code_names)

a_dict = lambda: {k: v for k, v in zip(names, code_names)}
print(a_dict())
```

    {'Mayank': 'Mr. God', 'Manish': 'Mr. Cool', 'Aalok': 'Mr. Normal', 'Roshan Musheer': 'The Big Boss'}



```python
# Excercise -> Try the above one using map, if possible
```


```python
def dictMap(f, xs) :
    return dict((f(i), i) for i in xs)
lst = [1,2,4,6]
lst2 = [3,5, 7,9]
print(list(map(pow, lst, lst2)))

```

    [1, 32, 16384, 10077696]



```python
def fahrenheit(T):
    return ((float(9)/5)*T + 32)

temp = (36.5, 37, 37.5, 39)

F = map(fahrenheit, temp)
print(list(F))
```

    [97.7, 98.60000000000001, 99.5, 102.2]


#### Reduce

Reduce takes a function and a collection of items. It returns a value that is created by combining the items. This is a simple reduce. It returns the sum of all the items in the collection.


```python
from functools import reduce

product = reduce(lambda a, x: a * x, range(1, 6))

print(product) # (((1 * 2 )* 3 )* 4) * 5

product = reduce(lambda a, x: a * x, range(-1, 6))
print(product) 

## NOTE the 20 at the end 
print(reduce(lambda a, x: a + x, range(1, 6), 20)) #-> 10 + 1 + 2+ 
```

    120
    0
    35



```python

```




    15




```python
help(reduce)
```

    Help on built-in function reduce in module _functools:
    
    reduce(...)
        reduce(function, sequence[, initial]) -> value
        
        Apply a function of two arguments cumulatively to the items of a sequence,
        from left to right, so as to reduce the sequence to a single value.
        For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
        ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
        of the sequence in the calculation, and serves as a default when the
        sequence is empty.
    


In the above example, `x` is the current iterated item and `a` is the accumulator. 
It is the value returned by the execution of the lambda on the previous item. reduce() walks through the items. For each one, it runs the lambda on the current a and x and returns the result as the a of the next iteration.

What is a in the first iteration? There is no previous iteration result for it to pass along. reduce() uses the first item in the collection for a in the first iteration and starts iterating at the second item. That is, the first x is the second item.

This code counts how often the word 'the' appears in a list of strings:


```python
sentences = ['Copy the variable assignment for our new empty list'
             'Copy the expression that we’ve been append-ing into this new list'
             'Copy the for loop line, excluding the final'
             'Copy the if statement line, also without the']

count = 0
for sentence in sentences:
    count += sentence.count('the')

print(count)
```

    6



```python
help(reduce)
```

    Help on built-in function reduce in module _functools:
    
    reduce(...)
        reduce(function, sequence[, initial]) -> value
        
        Apply a function of two arguments cumulatively to the items of a sequence,
        from left to right, so as to reduce the sequence to a single value.
        For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
        ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
        of the sequence in the calculation, and serves as a default when the
        sequence is empty.
    



```python

```

    6



```python
# This is the same code written as a reduce:
from functools import reduce


def countme(x):
    return x.count('the')
    
sentences = ['Copy the variable assignment for our new empty list'
             'Copy the expression that we’ve been append-ing into this new list'
             'Copy the for loop line, excluding the final'
             'Copy the if statement line, also without the']

sam_count = reduce(lambda a, x: a + countme(x),
                   sentences, 0)
print(sam_count)
```

    6


**NOTE:**

How does this code come up with its initial a? The starting point for the number of incidences of 'Sam' cannot be 'Mary read a story to Sam and Isla.' The initial accumulator is specified with the third argument to reduce(). This allows the use of a value of a different type from the items in the collection.

#### Benefits map and reduce 

* they are often one-liners.
* the important parts of the iteration - the collection, the operation and the return value - are always in the same places in every map and reduce.
* the code in a loop may affect variables defined before it or code that runs after it. By convention, maps and reduces are functional.
* map and reduce are elemental operations. Every time a person reads a for loop, they have to work through the logic line by line. There are few structural regularities they can use to create a scaffolding on which to hang their understanding of the code. In contrast, map and reduce are at once building blocks that can be combined into complex algorithms, and elements that the code reader can instantly understand and abstract in their mind. “Ah, this code is transforming each item in this collection. It’s throwing some of the transformations away. It’s combining the remainder into a single output.”
* map and reduce have many friends that provide useful, tweaked versions of their basic behaviour. For example: filter, all, any and find.

### Filtering

The function `filter(function, list)` offers an elegant way to filter out all the elements of a list, for which the function function returns True.

The function `filter(f,l`) needs a function `f` as its first argument. `f` returns a Boolean value, i.e. either True or False. This function will be applied to every element of the list `l`. Only if f returns True will the element of the list be included in the result list. 


```python
fib = [0,1,1,2,3,5,8,13,21,34,55]

result = filter(lambda x: x % 2 != 0, fib)
print(list(result))
```

    [1, 1, 3, 5, 13, 21, 55]



```python
def get_odd(val):
    return val % 2 != 0

result = list(filter(get_odd, fib))
print(result)
```

    [1, 1, 3, 5, 13, 21, 55]



```python
result = filter(lambda x: x % 2 == 0, fib)
print(list(result))
```

    [0, 2, 8, 34]



```python
def get_even(val):
    return val % 2 == 0

result = list(filter(get_even, fib))
print(result)
```

    [0, 2, 8, 34]



```python
apis = [{'name': 'UpdateUser', 'type': 'POST', "body": "{'name': '$name'}"},
        {'name': 'addUser', 'type': 'POST', "body": "{name : '$name'}"},
        {'name': 'listUsers', 'type': 'GET'},
        {'name': 'listUsers', 'type': ''},
        {'name': 'listUsers_withNone', 'type': None},
        {'name': 'testWithoutType'}]
```


```python
posts = 0
for api in apis:
    if 'type' in api and api['type'] == 'POST':
        posts += 1

print(posts)
```


```python
posts = 0
c = []

c = list(filter(lambda x:'type' in x and x['type'] is not 'POST', apis))
print(c)
print(len(list(c)))
```

    [{'name': 'listUsers', 'type': 'GET'}, {'name': 'listUsers', 'type': ''}, {'name': 'listUsers_withNone', 'type': None}]
    3



```python
posts = 0
c = []

c = list(filter(lambda x:'type' in x and x['type'] is 'POST', apis))
print(c)
print(len(list(c)))
```

    [{'name': 'UpdateUser', 'type': 'POST', 'body': "{'name': '$name'}"}, {'name': 'addUser', 'type': 'POST', 'body': "{name : '$name'}"}]
    2



```python
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

heights = map(lambda x: x['height'],
              filter(lambda x: 'height' in x, people))
print(heights)

if len(heights) > 0:
    from operator import add
    average_height = reduce(add, heights) / len(heights)
    print(average_height)
```

    [160, 80]
    120


## functools
----

The functools module is for higher-order functions: functions that act on or return other functions. In general, any callable object can be treated as a function for the purposes of this module.

Common functions in functools are as follows

* partial
* reduce


### partial

functools.partial does the follows:

* Makes a new version of a function with one or more arguments already filled in.
* New version of a function documents itself.


```python
def power(base, exponent):
    return base ** exponent
```


```python
def square(base):
    return power(base, 2)

def cube(base):
    return power(base, 3)
```

Now lets see the magic of partial


```python
from functools import partial

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(2))
print(cube(2))

print(square(2, exponent=4))
print(cube(2, exponent=9))
```

    4
    8
    16
    512



```python
from functools import partial

def multiply(x,y):
        return x * y

# create a new function that multiplies by 2
db2 = partial(multiply,2)
print(db2(4))
db4 = partial(multiply, 4)
print(db4(3))
```

    8
    12



```python
from functools import partial
 
#----------------------------------------------------------------------
def add(x, y):
    """"""
    return x + y
 
#----------------------------------------------------------------------
def multiply(x, y):
    """"""
    return x * y
 
#----------------------------------------------------------------------
def run(func):
    """"""
    print (func())
 
#----------------------------------------------------------------------
def main():
    """"""
    a1 = partial(add, 1, 2)
    m1 = partial(multiply, 5, 8)
    run(a1)
    run(m1)
 
if __name__ == "__main__":
    main()
```

    3
    40



```python
def another_function(func):
    """
    A function that accepts another function
    """
 
    def wrapper():
        """
        A wrapping function
        """
        val = "The result of %s is %s" % (func(),
                                          eval(func())
                                          )
        return val
    return wrapper
 
#----------------------------------------------------------------------
@another_function
def a_function():
    """A pretty useless function"""
    return "1+1"
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    print (a_function.__name__)
    print (a_function.__doc__)
    print(a_function())
```

    wrapper
    
            A wrapping function
            
    The result of 1+1 is 2



```python
from functools import wraps
 
#----------------------------------------------------------------------
def another_function(func):
    """
    A function that accepts another function
    """
 
    @wraps(func)
    def wrapper():
        """
        A wrapping function
        """
        val = "The result of %s is %s" % (func(),
                                          eval(func())
                                          )
        return val
    return wrapper
 
#----------------------------------------------------------------------
@another_function
def a_function():
    """A pretty useless function"""
    return "1+1"
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    #a_function()
    print (a_function.__name__)
    print (a_function.__doc__)
    print(a_function())
```

    a_function
    A pretty useless function
    The result of 1+1 is 2


Here we import wraps from the functools module and use it as a decorator for the nested wrapper function inside of another_function to map the __name__ and __doc__ to the wrapper function

#### update_wrapper

The partial object does not have __name__ or __doc__ attributes by default, and without those attributes decorated functions are more difficult to debug. Using update_wrapper(), copies or adds attributes from the original function to the partial object.


```python
import functools


def myfunc1(a, b=2):
    print ('\tcalled myfunc1 with:', (a, b))
    return

def myfunc(a, b=2):
    """Docstring for myfunc()."""
    print ('\tcalled myfunc with:', (a, b))
    return

def show_details(name, f):
    """Show details of a callable object."""
    print ('%s:' % name)
    print ('\tobject:', f)
    print ('\t__name__:',) 
    try:
        print (f.__name__)
    except AttributeError:
        print ('(no __name__)')
    print ('\t__doc__', repr(f.__doc__))
    print
    return
show_details('myfunc1', myfunc1)
print("~"*20)
show_details('myfunc', myfunc)

p1 = functools.partial(myfunc, b=4)
print("+"*20)
show_details('raw wrapper', p1)
print("^"*20)
print ('Updating wrapper:')
print ('\tassign:', functools.WRAPPER_ASSIGNMENTS)
print ('\tupdate:', functools.WRAPPER_UPDATES)
print("*"*20)

functools.update_wrapper(p1, myfunc)
show_details('updated wrapper', p1)
```

    myfunc1:
    	object: <function myfunc1 at 0x000001ECFB445A60>
    	__name__:
    myfunc1
    	__doc__ None
    ~~~~~~~~~~~~~~~~~~~~
    myfunc:
    	object: <function myfunc at 0x000001ECFB445EA0>
    	__name__:
    myfunc
    	__doc__ 'Docstring for myfunc().'
    ++++++++++++++++++++
    raw wrapper:
    	object: functools.partial(<function myfunc at 0x000001ECFB445EA0>, b=4)
    	__name__:
    (no __name__)
    	__doc__ 'partial(func, *args, **keywords) - new function with partial application\n    of the given arguments and keywords.\n'
    ^^^^^^^^^^^^^^^^^^^^
    Updating wrapper:
    	assign: ('__module__', '__name__', '__qualname__', '__doc__', '__annotations__')
    	update: ('__dict__',)
    ********************
    updated wrapper:
    	object: functools.partial(<function myfunc at 0x000001ECFB445EA0>, b=4)
    	__name__:
    myfunc
    	__doc__ 'Docstring for myfunc().'


 


- Avoid state
- Immutable data
- First-class functions
- Higher-order functions
- Pure functions
- Recursion, tail recursion
- Iterators, sequences, lazy evaluation, pattern matching, monads, etc.
