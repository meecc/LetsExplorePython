
## Lists

Lists are collections of heterogeneous objects, which can be of any type, including other lists.

Lists in the Python are mutable and can be changed at any time. Lists can be sliced ​​in the same way as *strings*, but as the lists are mutable, it is possible to make assignments to the list items.

**Syntax**:

```python
list = [a, b, ..., z]
```

Common operations with lists:


```python
fruits = ['Apple', 'Mango', 'Grapes', 'Jackfruit', 
          'Apple', 'Banana', 'Grapes', [1, "Orange"]]

# processing the entire list
for fruit in fruits:
     print(fruit,  end=", ")

#
print("*"*30)


fruits.insert(0, "kiwi")
# help(fruits.insert)
# Including
fruits.append('Camel')
print(fruits)
```

    Apple, Mango, Grapes, Jackfruit, Apple, Banana, Grapes, [1, 'Orange'], ******************************
    ['kiwi', 'Apple', 'Mango', 'Grapes', 'Jackfruit', 'Apple', 'Banana', 'Grapes', [1, 'Orange'], 'Camel']


## Removing


```python
## Removing the second instance of Grapes
x = 0
y = 0
for fruit in fruits:
    if x == 1 and fruit == 'Grapes':
#          del (fruits[y])
        fruits.pop(y)
    elif fruit == 'Grapes':
        x = 1
    y +=1
    
print(fruits)   
```

    ['kiwi', 'Apple', 'Mango', 'Grapes', 'Jackfruit', 'Apple', 'Banana', [1, 'Orange'], 'Camel']



```python
fruits.remove('Grapes')
```

## Appending


```python
print(fruits)
fruits.append("Grapes")
```

    ['kiwi', 'Apple', 'Mango', 'Jackfruit', 'Apple', 'Banana', [1, 'Orange'], 'Camel']


## Ordering 


```python
# These will work on only homogeneous list and will fail for heterogeneous
fruits.sort()
print(fruits)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-12-a40e7897b208> in <module>()
          1 # These will work on only homogeneous list and will fail for heterogeneous
    ----> 2 fruits.sort()
          3 print(fruits)


    TypeError: unorderable types: list() < str()


## Inverting


```python
fruits.reverse()
print(fruits)
```

    ['Apple', 'Apple', 'Banana', 'Jackfruit', 'Mango', 'kiwi', [1, 'Orange'], 'Camel', 'Grapes']



```python
# # # prints with number order
for i, prog in enumerate(fruits):
    print( i + 1, '=>', prog)
print(len(fruits))
# # prints from de second item
print (fruits[1:])
```

    1 => Apple
    2 => Apple
    3 => Banana
    4 => Jackfruit
    5 => Mango
    6 => kiwi
    7 => [1, 'Orange']
    8 => Camel
    9 => Grapes
    9
    ['Apple', 'Banana', 'Jackfruit', 'Mango', 'kiwi', [1, 'Orange'], 'Camel', 'Grapes']


The function `enumerate()` returns a tuple of two elements in each iteration: a sequence number and an item from the corresponding sequence.

The list has a `pop()` method that helps the implementation of queues and stacks:


```python
my_list = ['A', 'B', 'C']
for a, b in enumerate(my_list):
    print(a, b)

# for (int x=0; x<len(my_list); x++){
#     printf("")
# }
```

    0 A
    1 B
    2 C



```python
my_list = ['A', 'B', 'C']
print ('list:', my_list)

# # The empty list is evaluated as false
while my_list:
    # In queues, the first item is the first to go out
    # pop(0) removes and returns the first item 
    print ('Left', my_list.pop(0), ', remain', len(my_list), my_list)

my_list.append("G")
# # More items on the list
my_list += ['D', 'E', 'F']
print ('list:', my_list)

while my_list:
    # On stacks, the first item is the last to go out
    # pop() removes and retorns the last item
    print ('Left', my_list.pop(), ', remain', len(my_list), my_list)
```

    list: ['A', 'B', 'C']
    Left A , remain 2 ['B', 'C']
    Left B , remain 1 ['C']
    Left C , remain 0 []
    list: ['G', 'D', 'E', 'F']
    Left F , remain 3 ['G', 'D', 'E']
    Left E , remain 2 ['G', 'D']
    Left D , remain 1 ['G']
    Left G , remain 0 []



```python
l = ['D', 'E', 'F', "G", "H"]
print(l)
k = ('D', "E", "G", "H")
print(dir(l))
print("*"*8)
print(dir(k))

```

    ['D', 'E', 'F', 'G', 'H']
    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    ********
    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']


The sort (*sort*) and reversal (*reverse*) operations are performed in the list and do not create new lists.

Tuples
------
Similar to lists, but immutable: it's not possible to append, delete or make assignments to the items.

Syntax:

    my_tuple = (a, b, ..., z)

The parentheses are optional.

Feature: a tuple with only one element is represented as:

t1 = (1,)

The tuple elements can be referenced the same way as the elements of a list:

    first_element = tuple[0]

Lists can be converted into tuples:

    my_tuple = tuple(my_list)

And tuples can be converted into lists:

    my_list = list(my_tuple)

While tuple can contain mutable elements, these elements can not undergo assignment, as this would change the reference to the object.

Example (using the interactive mode):


```python
t = ([1, 2], 4)
print(t)
```

    ([1, 2], 4)



```python
print(" :: Error :: ")

t[0] = 3
print(t)

```

     :: Error :: 



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-35-001db6e2f049> in <module>()
          1 print(" :: Error :: ")
          2 
    ----> 3 t[0] = 3
          4 print(t)


    TypeError: 'tuple' object does not support item assignment



```python
t[0] = [1, 2, 3]
print(t)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-31-1160520bcf2f> in <module>()
    ----> 1 t[0] = [1, 2, 3]
          2 print(t)


    TypeError: 'tuple' object does not support item assignment



```python
t[0].append(3)
print(t)
```

    ([1, 2, 3, 3], 4)



```python
t[0][0] = [1, 2, 3]
print(t)
```

    ([[1, 2, 3], 2, 3, 3], 4)



```python
ta = (1, 2, 3, 4, 5)

for a in ta:
    print (a)
```

    1
    2
    3
    4
    5



```python
ta1 = [1, 2, 3, 4, 5]
for a in ta1:
    print(a)
```

    1
    2
    3
    4
    5


**NOTE**: Tuples are more efficient than conventional lists, as they consume less computing resources (memory) because they are simpler structures the same way *immutable* strings are in relation to *mutable* strings.

### Lists Versus Tuples

Tuples are used to collect an immutable ordered list of elements. This means that to a tuple (**limitation**):

- elements can't be added, thus There’s no append() or extend() method for tuples,
- elements can't be removed, thus Tuples have no remove() or pop() method,

So, if we have a constant set of values and only we will iterate through it than use a tuple instead of a list as It is faster & safer than working with lists, as the tuples contain “write-protect” data.
