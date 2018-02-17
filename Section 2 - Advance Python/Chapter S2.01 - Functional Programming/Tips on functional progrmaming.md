
# Tips on functional progrmaming
-----

This section contains tips on functional programming and ZERO theory. :). So enjoy. 


```python
# Original 
x = 20
if(x > 1):
    print("True: ", x)

# eleminating if
x  = 20
a = (x > 1 and ("True: " + str(x)))
print(a)
```

    ('True: ', 20)
    True: 20



```python
# Eleminating if else
x = 10
if (x > 1):
    print("true ", x)
else:
    print("false ", x)
```


```python
x  = -20
a = (x>1 and ("true" + str(x))) or ("false " + str(x))
print(a)
```

    false -20



```python
x  = 20
a = (x > 1 and ("true " + str(x))) or ("false " + str(x))
print(a)
```

    true 20



```python
AND
0 0 0 
0 1 0
1 0 0
1 1 1 

or
0 0 0 
0 1 1 
1 0 1
1 1 1
```


```python
# Eleminating if elif else
x = 0
if (x == 0):
    print("False")
elif (x == 1):
    print("True")
else:
    print("Not boolean")
    
print("*"*11)

a = (x == 0 and ("False")) or ((x == 1 and ("True")) or ("Not boolean")) 
print(a)
```

    False
    ***********
    False



```python
# Eliminating Sequential Statement
def double(x):
    return(x+x)

d = []
for x in range(20):
    d.append(double(x))
print(d)
    
# Using import map
print("*"*75)
d = list(map(double, range(20)))
print(d)
```

    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
    ***************************************************************************
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]



```python
# Eliminating While Statement
def double(x):
    return(x+x)
x = 1
d = []

while x < 20:
    d.append(double(x))
    x = x + 1
    
print(d)


##  while_FP = lambda: (<cond> and while_block()) or while_FP()
```

    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]

