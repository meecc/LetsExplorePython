
# Generators
----

The functions generally follow the conventional process flow, return values ​​and quit. Generators work similarly, but remember the state of the processing between calls, staying in memory and returning the next item expected when activated.

The generators have several advantages over conventional functions:

+ *Lazy Evaluation*: generators are only processed when it is really needed, saving processing resources. 
+ They reduce the need to create lists.
+ They allow to work with unlimited sequences of elements.

Generators are usually called through a *for* loop. The  syntax is similar to the traditional function, just the *yield* instruction substitutes *return*. In each new iteraction, *yield* returns the next value.

Exemple:


```python
def gen_pares():
    """
    Generates even numbers from 0 to 20
    """
    i = 0

    while i <= 20:
        yield i
        print("dada")
        i += 2

# Shows each number and goes to the next
for n in gen_pares():
    print ("> ", n)
    
```

    >  0
    dada
    >  2
    dada
    >  4
    dada
    >  6
    dada
    >  8
    dada
    >  10
    dada
    >  12
    dada
    >  14
    dada
    >  16
    dada
    >  18
    dada
    >  20
    dada



```python
def gen_pares():
    """
    Generates even numbers from 0 to 20
    """
    i = 0
    yield i
    print("dada")
    i += 2
    yield i

# Shows each number and goes to the next
for n in gen_pares():
    print ("> ", n) 
```

    >  0
    dada
    >  2



```python
a = list(gen_pares())
print(a)
```

    dada


Another example:


```python
import os

# Finds files recursively
def find(path='.'):
    for item in os.listdir(path):
        fn = os.path.normpath(os.path.join(path, item))

        if os.path.isdir(fn):
            for f in find(fn):
                yield f
        else:
            yield fn

# At each interaction, the generator yeld a new file name
for fn in find(r"/home/mayank/code/mj/raas/test/"):
    print (fn)
```

    /home/mayank/code/mj/raas/test/bb7567d7-8611-4416-a569-09b1d7972970-testsuite.xml
    /home/mayank/code/mj/raas/test/templates/login.html



```python
import time
import sys

def fib():
   a, b = 0, 1
   while True:
      yield b
      d = a + b
      if d > 20:
        break
      a, b = b, d 


iter = fib()

try:
    for i in iter:
        print( i),
        time.sleep(1)
        sys.stdout.flush()
    print("...Done...")
except KeyboardInterrupt: 
   print( "Calculation stopped")
```

    1
    1
    2
    3
    5
    8
    13
    ...Done...

