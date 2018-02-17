
## Boolean

### True, False and Null

In Python, the boolean type (*bool*) is special integer type (*int*) which can have only one of two values, i.e. *True* (value equal to 1) or *False* (value equal to 0).

The following values are considered false:

+ `False`.
+ `None` (null).
+ `0` (zero).
+ `''` (empty string).
+ `[]` (empty list).
+ `()` (empty tuple).
+ `{}` (emtpy dicionary).
+ Other structures with size equal zero.

All other objects out of that list are considered true.

The object *None*, which is of type *NoneType*, in Python represents the null and is evaluated as false by the interpreter.

Boolean Operators
--------------------
With logical operators it is possible to build more complex conditions to control conditional jumps and loops.

Boolean operators in Python are: *and*, *or* , *not* , *is* , *in*.

+ `and`: returns a true value if and only if it receives two expressions that are true.
+ `or` : returns a false value if and only if it receives two expressions that are false.
+ `not` : returns false if it receives a true expression and vice versa.
+ `is`: returns true if it receives two references to the same object false otherwise.
+ `in` : returns true if you receive an item and a list and the item occur one or more times in the list false otherwise.

The calculation of the resulting operation *and* is as follows: if the first expression is true, the result will be the second expression, otherwise it will be the first. 

As for the operator *or* if the first expression is false, the result will be the second expression, otherwise it will be the first. For other operators, the return will be of type bool (True or False).

Examples:


```python
print (0 and 3) # Shows 0
print (2 and 3 )# Shows 3

print (0 or 3) # Shows 3
print (2 or 3) # Shows 2

print (not 0) # Shows True
print (not 2) # Shows False
print (2 in (2, 3)) # Shows True
print (2 is 3) # Shows False
```

    0
    3
    3
    2
    True
    False
    True
    False


Besides boolean operators, there are the functions `all()`, which returns true when all of the items in the sequence passed as parameters are true, and `any()`, which returns true if any item is true.
