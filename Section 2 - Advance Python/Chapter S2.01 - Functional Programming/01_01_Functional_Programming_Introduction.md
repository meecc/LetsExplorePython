
# Introduction to Functional Programming

## What is Functional Programming

Functional programming is a programming paradigm that revolves around **pure functions**. 

## Pure function

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

### Characteristics of functional programming

- Functions are first class (objects). So, data and functions are treated as same and have access to same operations(such as passing a function to another function).
- Recursion as primary control structure.
- There is a focus on LISt Processing and are often used with recursion on sub-lists as a substitute for loops.
- Avoid "side-effects". It excludes the almost ubiquitous pattern in imperative languages of assigning first one, then another value to the same variable to track the program state.
- Either discourages or outright disallows statements, and instead works with the evaluation of expressions (in other words, functions plus arguments). In the pure case, one program is one expression (plus supporting definitions).
- FP worries about what is to be computed rather than how it is to be computed.
- Much FP utilizes "higher order" functions (in other words, functions that operate on functions that operate on functions).
