
## Comprehensions

Using comprehensions is often a way both to make code more compact and to shift our focus from the "how" to the "what". It is an expression that uses the same keywords as loop and conditional blocks, but inverts their order to focus on the data rather than on the procedure. 

Simply changing the form of expression can often make a surprisingly large difference in how we reason about code and how easy it is to understand. The ternary operator also performs a similar restructuring of our focus, using the same keywords in a different order.

###  List Comprehensions

A way to create a new list from existing list based on defined logic

#### Unconditional Compreshensions 


```python
# Original
doubled_numbers = []
for n in range(1,12,2):
    doubled_numbers.append(n*2)

print(doubled_numbers)
```

    [2, 6, 10, 14, 18, 22]



```python
#list compreshensions
doubled_numbers = [n * 2 for n in range(1,12,2)] # 1 ,3, 5, 7, 9, 11
print(doubled_numbers)
```

    [2, 6, 10, 14, 18, 22]


#### Conditional Compreshensions 


```python
doubled_odds = []

for n in range(1,12):
    if n % 2 == 1:
        doubled_odds.append(n * 2)
print(doubled_odds)
```


```python
doubled_odds = [n * 2 for n in range(1,12) if n% 2 == 1]

print(doubled_odds)
```

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


```python
# TO
numbers = range(2,10)

doubled_odds = [n * 2 for n in numbers if n % 2 == 1]

```

#### Nested `if` statements in `for` loop


```python
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]

lst = []
for v in l:
    if v == 0 :
        lst.append('Zero')
    else:
        if v % 2 == 0:
            lst.append('even')
        else:
            lst.append('odd')
            
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
def flatten_list_new(lst, result=None):
    """Flattens a nested list
        >>> flatten_list([ [1, 2, [3, 4] ], [5, 6], 7])
        [1, 2, 3, 4, 5, 6, 7]
    """
    if result is None:
        result = []
#     else:
#     result = [x if not isinstance(x, list) else flatten_list_new(x, list) for x in lst]
#     result = [ x  if not isinstance(x, list) else isinstance(x, list) for x in lst ]
#     result = [flatten_list_new(x, result) if isinstance(x, list) else x for x in lst ]
    for x in lst:
        if isinstance(x, list):
            flatten_list_new(x, result)
        else:
            result.append(x)

    return result
lst = [[1, 2, [3, [4]] ], [5, 6], 7]
  
print(flatten_list_new(lst))
```

    [1, 2, 3, 4, 5, 6, 7]



```python
newlist = []
input_list = [1,2, [2,[3]],3,[3,[[4],5]]]

def convertHetrogenousList(hetroList):
    newlist = []
    if type(hetroList) is int:
        newlist.append(hetroList)
    elif type(hetroList) is list:
        for items in hetroList:
            newlist.extend(convertHetrogenousList(items))
    return newlist

newlist = convertHetrogenousList(input_list)
print(newlist)
```

    [1, 2, 2, 3, 3, 3, 4, 5]



```python
### TODO Can we redirect the stdio.out to a list
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
lsts = [x for a in range(n) if a % 2 == 0 for x in range(a, 10)]

print(lsts)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 9, 4, 5, 6, 7, 8, 9, 6, 7, 8, 9, 8, 9]



```python
import os

help(os.walk)
```

    Help on function walk in module os:
    
    walk(top, topdown=True, onerror=None, followlinks=False)
        Directory tree generator.
        
        For each directory in the directory tree rooted at top (including top
        itself, but excluding '.' and '..'), yields a 3-tuple
        
            dirpath, dirnames, filenames
        
        dirpath is a string, the path to the directory.  dirnames is a list of
        the names of the subdirectories in dirpath (excluding '.' and '..').
        filenames is a list of the names of the non-directory files in dirpath.
        Note that the names in the lists are just names, with no path components.
        To get a full path (which begins with top) to a file or directory in
        dirpath, do os.path.join(dirpath, name).
        
        If optional arg 'topdown' is true or not specified, the triple for a
        directory is generated before the triples for any of its subdirectories
        (directories are generated top down).  If topdown is false, the triple
        for a directory is generated after the triples for all of its
        subdirectories (directories are generated bottom up).
        
        When topdown is true, the caller can modify the dirnames list in-place
        (e.g., via del or slice assignment), and walk will only recurse into the
        subdirectories whose names remain in dirnames; this can be used to prune the
        search, or to impose a specific order of visiting.  Modifying dirnames when
        topdown is false is ineffective, since the directories in dirnames have
        already been generated by the time dirnames itself is generated. No matter
        the value of topdown, the list of subdirectories is retrieved before the
        tuples for the directory and its subdirectories are generated.
        
        By default errors from the os.scandir() call are ignored.  If
        optional arg 'onerror' is specified, it should be a function; it
        will be called with one argument, an OSError instance.  It can
        report the error to continue with the walk, or raise the exception
        to abort the walk.  Note that the filename is available as the
        filename attribute of the exception object.
        
        By default, os.walk does not follow symbolic links to subdirectories on
        systems that support them.  In order to get this functionality, set the
        optional argument 'followlinks' to true.
        
        Caution:  if you pass a relative pathname for top, don't change the
        current working directory between resumptions of walk.  walk never
        changes the current directory, and assumes that the client doesn't
        either.
        
        Example:
        
        import os
        from os.path import join, getsize
        for root, dirs, files in os.walk('python/Lib/email'):
            print(root, "consumes", end="")
            print(sum([getsize(join(root, name)) for name in files]), end="")
            print("bytes in", len(files), "non-directory files")
            if 'CVS' in dirs:
                dirs.remove('CVS')  # don't visit CVS directories
    



```python
# %%time
import os

file_list = []

for path, _, files in os.walk("/home/mayank/lep"):
    for f in files:
        if f.endswith(".py"):
            file_list.append(os.path.join(path, f))

print(len(file_list))
# print(file_list)
```

    514



```python
file_list = [os.path.join(path, f) for path, _, files in os.walk("/home/mayank/lep") for f in files if f.endswith(".py") ]
print(len(file_list))
```

    514



```python
%%time

import os

folder = "/home/mayank/lep"
file_list = [os.path.join(path, f) 
             for path, _, files in os.walk(folder) 
                 for f in files if f.endswith(".py") ]
print(len(file_list))
```

    514
    CPU times: user 33.8 ms, sys: 0 ns, total: 33.8 ms
    Wall time: 33.2 ms



```python
%%time
restFiles = []

for d in os.walk(r"C:\apps"):
    if "etc" in d[0]:
        for f in d[2]:
            if f.endswith(".txt"):
                restFiles.append(os.path.join(d[0], f))
print(len(restFiles))
```

    0
    Wall time: 977 µs



```python
%%time
restFiles = [os.path.join(d[0], f) 
                 for d in os.walk(r"C:\apps") 
                     if "etc" in d[0]
                         for f in d[2] 
                             if f.endswith(".txt")]
print(len(restFiles))
```

    0
    CPU times: user 320 µs, sys: 0 ns, total: 320 µs
    Wall time: 177 µs



```python
lst = [1, 2, [2, 3], 3, [3, [[4], 5]]]

lst = [1, 2, 2, 3, 3, 3, 4, 5]
```


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
    CPU times: user 116 µs, sys: 13 µs, total: 129 µs
    Wall time: 101 µs



```python
matrix = [[1 if item_idx == row_idx 
               else 0 for item_idx in range(0, 3)] 
                  for row_idx in range(0, 3) ]
print(matrix)
```

    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]



```python
lst = [1,2,34,4,5]
print(lst)
lst.append(2)
print(lst)
```


```python

lst.append(2)
print(lst)
l = set(lst)
print(l)
```

### Set Comprehensions

Set comprehensions allow sets to be constructed using the same principles as list comprehensions, the only difference is that resulting sequence is a set and **"{}"** are used instead of **"[]"**.


```python
names = [ 'aaLok', 'Manish', 'AalOK', 'Manish', 'Gupta', 'Johri', 'Mayank' ]

new_names1 = [name[0].upper() + name[1:].lower() for name in names if len(name) > 1 ]
new_names = sorted({name[0].upper() + name[1:].lower() for name in names if len(name) > 1 })
print(new_names1)
print(new_names)
```

### Dictionary Comprehensions


```python
original = {'a':10, 'b': 34, 'A': 7, 'Z':3, "z": 199}
```

Now, lets consolidate the above dictionary in such a way that resultant dictionary will have only lower case keys and if both lower and upper case keys are found in the original dictionary than values of both the keys should be added.  


```python
mcase_freq = {}
for k in original.keys():
    mcase_freq[k.lower()] = original.get(k.lower(),0) + original.get(k.upper, 0)
print(mcase_freq)
```

    {'a': 10, 'b': 34, 'z': 199}



```python
mcase_frequency = { k.lower() : original.get(k.lower(), 0) + original.get(k.upper(), 0) for k in original.keys() }
print(mcase_frequency)
```

    {'a': 17, 'b': 34, 'z': 202}



```python
original = {'a':10, 'b': 34, 'A': 7, 'Z':3, "z": 199, 'c': 10}
flipped = {value: key for key, value in original.items()}
print(flipped)
```


```python
original = {'a':10, 'b': 34, 'A': 7, 'Z':3, "z": 199, 'c': 10}
newdict = {}
for key, value in original.items():
#     print(ori)
    if (value not in newdict):
        newdict[value] = key
print(newdict)
```


```python
newdict = {value: key for key, value in original.items() if (value not in newdict)}
print(newdict)
```


```python
x = {"a": 10, "b": 20, "c": 20}

print(x)
x["a"] = 100

print(x)
```

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

    {'Mayank': 'The Big Boss', 'Manish': 'Mr. God', 'Aalok': 'Mr. Normal', 'Roshan Musheer': 'Mr. Cool'}



```python
# Better implementation
import random

names_dict = {}
names = ["Mayank", "Manish", "Aalok", "Roshan Musheer"]
code_names = ['Mr. Normal', 'Mr. God', 'Mr. Cool', 'The Big Boss']

random.shuffle(code_names)

for i, _ in enumerate(names):
    names_dict[names[i]] = code_names[i] 
        
print(names_dict)
```

    {'Mayank': 'Mr. Cool', 'Manish': 'The Big Boss', 'Aalok': 'Mr. Normal', 'Roshan Musheer': 'Mr. God'}



```python
# best implementation
import random

names_dict = {}
names = ["Mayank", "Manish", "Aalok", "Roshan Musheer"]
code_names = ['Mr. Normal', 'Mr. God', 'Mr. Cool', 'The Big Boss']

random.shuffle(code_names)

names_dict = dict(zip(names, code_names))

print(names_dict)
```

    {'Mayank': 'The Big Boss', 'Manish': 'Mr. God', 'Aalok': 'Mr. Normal', 'Roshan Musheer': 'Mr. Cool'}



```python
ld = [{'a': 10, 'b': 20}, {'p': 10, 'u': 100}]
dict([kv for d in ld for kv in d.items()])
```

### Generator Comprehension

They are simply a generator expression with a parenthesis "()" around it. Otherwise, the syntax and the way of working is like list comprehension, but a generator comprehension returns a generator instead of a list. 


```python
%%timeit
x = (x**2 for x in range(20000))
# for a in x:
#     pass
```

    928 ns ± 12.4 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)



```python
%%timeit
x = [x**2 for x in range(20000)]
# for a in x:
#     pass
```

    8.15 ms ± 199 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)



```python
itm = 10
print(itm / 2)
```

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

Can be rewritten into a list comprehension like this:


```python
new_things = [ITEM for ITEM in old_things if condition_based_on(ITEM)]
print(new_things)
```

**NOTE**

If you can nudge a for loop until it looks like the ones above, you can rewrite it as a list comprehension.
