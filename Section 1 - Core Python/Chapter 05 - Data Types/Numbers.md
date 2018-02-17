
## Numbers

Python provide following *builtins* numeric data types:

+ Integer (*int*): i = 26011950
+ Floating Point real (*float*): f = 1.2345
+ Complex (*complex*): c = 2 + 10j

The builtin function `int()` can be used to convert other types to integer, including base changes.

*Example*:


```python
# Converting real to integer
print ('int(3.14) =', int(3.14))
print ('int(3.64) =', int(3.64))
```

    int(3.14) = 3
    int(3.64) = 3



```python
# Converting integer to real
print ('float(5) =', float(5))
```

    float(5) = 5.0



```python
# Calculation between integer and real results in real
print ('5.0 / 2 + 3 = ', 5 / 2 + 3)
```

    5.0 / 2 + 3 =  5.5



```python
x = 3.5
y = 2.5
z = x + y
print(x, y, z)
print(type(x), y, type(z))
z = int(z)
print(x, y, z)
print(type(x), y, type(z))
```

    3.5 2.5 6.0
    <class 'float'> 2.5 <class 'float'>
    3.5 2.5 6
    <class 'float'> 2.5 <class 'int'>



```python
# Integers in other base
print ("int('20', 8) =", int('20', 8)) # base 8
print ("int('20', 16) =", int('20', 16)) # base 16
```

    int('20', 8) = 16
    int('20', 16) = 32



```python
# Operations with complex numbers
c = 3 + 4j
print ('c =', c)

print ('Real Part:', c.real)
print ('Imaginary Part:', c.imag)
print ('Conjugate:', c.conjugate())
```

    c = (3+4j)
    Real Part: 3.0
    Imaginary Part: 4.0
    Conjugate: (3-4j)


> NOTE: The real numbers can also be represented in scientific notation, for example: 1.2e22.

### Arithmetic Operations:

Python has a number of defined operators for handling numbers through arithmetic calculations, logic operations (that test whether a condition is true or false) or bitwise processing (where the numbers are processed in binary form).

#### Logical Operations:

+ Less than (<)
+ Greater than (>)
+ Less than or equal to (<=)
+ Greater than or equal to (>=)
+ Equal to (==)
+ Not equal to (!=)

##### Less than (<)


```python
x = 22
y = 4
if(x < y):
    print("X wins")
else:
    print("Y wins")
```

    Y wins



```python
x = 2
y = 4
if(x < y):
    print("X wins")
else:
    print("Y wins")
```

    X wins


##### Greater than (>)


```python
x = 2
y = 4
if(x > y):
    print("X wins")
else:
    print("Y wins")
```

    Y wins



```python
x = 14
y = 4
if(x > y):
    print("X wins")
else:
    print("Y wins")
```

    X wins


##### Less than or equal to (<=)


```python
x = 2
y = 4
if(x <= y):
    print("X wins")
else:
    print("Y wins")
```


```python
x = 2
y = 4
if(x <= y):
    print("X wins")
else:
    print("Y wins")
```


```python
x = 21
y = 4
if(x <= y):
    print("X wins")
else:
    print("Y wins")
```


```python
x = 4
y = 4
if(x <= y):
    print("X wins")
else:
    print("Y wins")
```

##### greater_than_or_equal_to


```python
x = 8
y = 4
if(x >= y):
    print("X wins")
else:
    print("Y wins")
```


```python
x = 4
y = 14
if(x <= y):
    print("X wins")
else:
    print("Y wins")
```


```python
x = 4
y = 4
if(x <= y):
    print("X wins")
else:
    print("Y wins")
```

##### Equal To


```python
x = 4
y = 4
if(x == y):
    print("X & Y are equal")
else:
    print("X & Y are different")
```

    X & Y are equal



```python
x = 41
y = 4
if(x == y):
    print("X & Y are equal")
else:
    print("X & Y are different")
```

    X & Y are different



```python
x = 2+1j
y = 3+1j
if(x == y):
    print("X & Y are equal")
else:
    print("X & Y are different")
```

    X & Y are different



```python
x = 21+1j
y = 21+1j
if(x == y):
    print("X & Y are equal")
else:
    print("X & Y are different")
```

    X & Y are equal



```python
x = 21+1j
y = 21+1j
if(x == y):
    print("X & Y are equal")
else:
    print("X & Y are different")
```

    X & Y are equal


##### Not Equal To


```python
x = 4
y = 4
if(x != y):
    print("X & Y are different")
else:
    print("X & Y are equal")
```

    X & Y are equal



```python
x = 41
y = 4
if(x != y):
    print("X & Y are different")
else:
    print("X & Y are equal")
```

    X & Y are different



```python
x = 2+1j
y = 3+1j
if(x != y):
    print("X & Y are different")
else:
    print("X & Y are equal")
```

    X & Y are different



```python
x = 21+1j
y = 21+1j
if(x != y):
    print("X & Y are different")
else:
    print("X & Y are equal")
```

    X & Y are equal


#### Bitwise Operations:

+ Left Shift (<<)
+ Right Shift (>>)
+ And (&)
+ Or (|)
+ Exclusive Or (^)
+ Inversion (~)

During the operations, numbers are converted appropriately (eg. `(1.5+4j) + 3` gives `4.5+4j`).

Besides operators, there are also some *builtin* features to handle numeric types: `abs()`, which returns the absolute value of the number, `oct()`, which converts to octal, `hex()`, which converts for hexadecimal, `pow()`, which raises a number by another and `round()`, which returns a real number with the specified rounding.




```python
x = 10 #-> 1010 
y = 11 #-> 1011
```


```
1011
"""
OR
0 0 | 0 
0 1 | 1
1 0 | 1
1 1 | 1
AND
0 0 | 0
0 1 | 0
1 0 | 0
1 1 | 1
"""
```


```python
print("x<<2 = ", x<<2)
print("x =", x)
print("x>>2 = ", x>>2)
print("x&y = ", x&y)
print("x|y = ", x|y)
print("x^y = ", x^y)
print("x =", x)
print("~x = ", ~x)
print("~y = ", ~y)
```

    x<<2 =  40
    x = 10
    x>>2 =  2
    x&y =  10
    x|y =  11
    x^y =  1
    x = 10
    ~x =  -11
    ~y =  -12



```python



```
