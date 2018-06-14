
## Recursion

In Functional programming iteration such as `while` or `for` statements are avoided. Also it does not have the provision of state-updates. 
In FP recursion is used to overcome iterations, since any iterative code can be converted to recursive code as shown in the below examples.


```python
# Original code
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
# Updated code: Fist irreration
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



```python
# Updated code: Fist irreration
def fib(n):
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return 1

# Show Fibonacci from 1 to 5
for i in range(1,6):
    print (i, '=>', fib(i))
```

or, using `lambda`


```python
fibonacci = (lambda x, x_1=1, x_2=0:
         x_2 if x == 0
         else fibonacci(x - 1, x_1 + x_2, x_1))

print(fibonacci(10))
```

    55

