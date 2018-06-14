
## map, reduce and filter

These are three functions which facilitate a functional approach to programming. `map`, `reduce` and `filter` are three higher-order functions that appear in all pure functional languages including Python. They are often are used in functional code to make it more elegant.

### Map

It basically provides kind of parallelism by calling the requested function over all elements in a list/array or in other words, 
Map applies a function to all the items in the given list and returns a new list.

It takes a function and a collection of items as parameters and makes a new, empty collection, runs the function on each item in the original collection and inserts each return value into the new collection. It then returns the updated collection.

This is a simple map that takes a list of names and returns a list of the lengths of those names:


```python
names = [ "Manish", "Aalok", "Mayank","Durga"]
lst = []

for name in names:
    lst.append(len(name))
    
print(lst)
```

    [6, 5, 6, 5]



```python
names =  ("Manish", "Aalok", "Mayank","Durga")

tmp = map(len, names)
print(tmp)
lst = tuple(tmp)

print(lst)

# This is a map that squares every number in the passed collection:
power = map(lambda x: x * x, lst)
print(power)
# print(list(power))
```

    <map object at 0x7f4ef8130390>
    (6, 5, 6, 5)
    <map object at 0x7f4ef8130358>



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

    {'Mayank': 'Mr. Cool', 'Roshan Musheer': 'Mr. Normal', 'Aalok': 'The Big Boss', 'Manish': 'Mr. God'}



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


### Reduce

Reduce takes a function and a collection of items. It returns a value that is created by combining the items. This is a simple reduce. It returns the sum of all the items in the collection.


```python
from functools import reduce

product = reduce(lambda a, x: a * x, range(1, 6))

print(product) # (((1 * 2 )* 3 )* 4) * 5
print(reduce(lambda a, x: a + x, range(1, 6), 10)) #-> 10 + 1 + 2+ 
```

    120
    25



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
import random

colours = ["pink", "purple", "black", "yellow", "purple", "indego", "white", "peach"]

def foo(counter, i):
  colour = random.choice(colours)
  try:
    counter[colour] += 1
  except KeyError:
    counter[colour] = 1
  return counter

counts = reduce(foo, range(1, 50), {})
print(counts)
```

    {'white': 9, 'purple': 13, 'pink': 3, 'yellow': 3, 'black': 4, 'peach': 9, 'indego': 8}


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
print(result)
```

    [1, 1, 3, 5, 13, 21, 55]



```python
result = filter(lambda x: x % 2 == 0, fib)
print(list(result))
```

    [0, 2, 8, 34]



```python
apis = [{'name': 'UpdateUser', 'type': 'POST', "body": "{'name': '$name'}"},
    {'name': 'addUser', 'type': 'POST', "body": "{name : '$name'}"},
    {'name': 'listUsers', 'type': 'GET'}]
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

c = filter(lambda x:'type' in x and x['type'] == 'POST', apis)
print(c)
print(len(list(c)))
```

    [{'body': "{'name': '$name'}", 'type': 'POST', 'name': 'UpdateUser'}, {'body': "{name : '$name'}", 'type': 'POST', 'name': 'addUser'}]
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

