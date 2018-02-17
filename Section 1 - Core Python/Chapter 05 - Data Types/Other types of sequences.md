
# Other types of sequences

Also in the *builtins*, Python provides:

+ *set*: mutable sequence univocal (without repetitions) unordered.
+ *frozenset*: immutable sequence univocal unordered.

Both types implement set operations, such as: union, intersection e difference.

Example:


```python
test = (1, 2, 3, "Aasdf", [1, 3, 5])
print(test)
test[-1][1]= "test"  
print(test)
test[-1].append("testing")
print(test)
test[-1] = ""
print(test)
```

    (1, 2, 3, 'Aasdf', [1, 3, 5])
    (1, 2, 3, 'Aasdf', [1, 'test', 5])
    (1, 2, 3, 'Aasdf', [1, 'test', 5, 'testing'])



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-1-76c72575bd4b> in <module>()
          5 test[-1].append("testing")
          6 print(test)
    ----> 7 test[-1] = ""
          8 print(test)


    TypeError: 'tuple' object does not support item assignment



```python
s1 = (1,2,3)
# print(s1)
# print(len(s1))
# print(s1.append(4))
s2 = ([1,2], 4)
print(s2)

# s2[0][1] = [5]
x = s2[0]
x[1] = [5]
x.append(5)
print(type(x))
s2[0].append(5)
# s2[0] = [6]
print(s2)
```

    ([1, 2], 4)
    <class 'list'>
    ([1, [5], 5, 5], 4)



```python
s = ((1,2),(21,22),(31,31),(41,42))
print(s)
print(s[0][1])
print(s[1][1])
print(s[1][0])
print(s[0])
```

    ((1, 2), (21, 22), (31, 31), (41, 42))
    2
    22
    21
    (1, 2)



```python
# Data sets
s1 = set(range(3))
s2 = set(range(10, 7, -1))
s3 = set(range(2, 10, 2))
s4 = [8, 9]

# Shows the data
print ('s1:', s1, '\ns2:', s2, '\ns3:', s3)

# Union
s1s2 = s1.union(s2)
print ('Union of s1 and s2:', s1s2)
s2s1 = s2.union(s1)
print ('Union of s2 and s1:', s2s1)

# Difference
print ('Difference with s3:', s1s2.difference(s3))

# Intersectiono
print ('Intersection with s3:', s1s2.intersection(s3))

# Tests if a set includes the other
if s1.issuperset([1, 2]):
    print ('s1 includes 1 and 2')

# Tests if there is no common elements
if s1.isdisjoint(s2):
    print ('s1 and s2 have no common elements')

# Tests if a set includes the other
if s2.issuperset(s4):
    print ('s2 includes all items from s4')
else:
    print("s2 does not include all items from s4")

# Tests if there is no common elements
if s2.isdisjoint(s3):
    print ('s2 and s3 have no common elements')
else:
    print("s2 and s3 have common elements")
```

    s1: {0, 1, 2} 
    s2: {8, 9, 10} 
    s3: {8, 2, 4, 6}
    Union of s1 and s2: {0, 1, 2, 8, 9, 10}
    Union of s2 and s1: {0, 1, 2, 8, 9, 10}
    Difference with s3: {0, 1, 9, 10}
    Intersection with s3: {8, 2}
    s1 includes 1 and 2
    s1 and s2 have no common elements
    s2 includes all items from s4
    s2 and s3 have common elements


When one list is converted to a *set*, the repetitions are discarded.

In version 2.6, a *builtin* type for mutable characters list, called *bytearray* is also available.
