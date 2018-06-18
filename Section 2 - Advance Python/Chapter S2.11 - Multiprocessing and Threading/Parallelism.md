
## Introducing: Map

Map can be used to easily achieve parallelism and we have already covered it in functional programming. For those who have not read it; It is a function which maps another function over a sequence

It basically provides kind of parallelism by calling the requested function over all elements in a list/array or in other words, Map applies a function to all the items in the given list and returns a new list.

It takes a function and a collection of items as parameters and makes a new, empty collection, runs the function on each item in the original collection and inserts each return value into the new collection. It then returns the updated collection.

This is a simple map that takes a list of names and returns a list of the lengths of those names


```python
names =  ("Manish", "Aalok", "Mayank","Durga")

lst = tuple(map(len, names))
print(lst)

# This is a map that squares every number in the passed collection:
power = map(lambda x: x*x, lst)
print(list(power))
```

    (6, 5, 6, 5)
    [36, 25, 36, 25]


## Multiprocessing


```python
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool 

# Initialize the pool, uses 
pool = ThreadPool() 
```


```python
import multiprocessing
multiprocessing.cpu_count()
```




    4




```python
# Sets the pool size to 4, 
# Play around the value till you get the most optimised value
# in this case ThreadPool() is equivalent to ThreadPool(4)
pool = ThreadPool(4)
```


```python
from urllib.request import urlopen
from multiprocessing.dummy import Pool as ThreadPool 

urls = [
  'http://www.python.org', 
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
  'http://planet.python.org/',
  'https://wiki.python.org/moin/LocalUserGroups',
  'http://www.python.org/psf/',
  'http://docs.python.org/devguide/',
  'http://www.python.org/community/awards/'
  ]

# Make the Pool of workers
pool = ThreadPool(10) 
# Open the urls in their own threads
# and return the results
results = pool.map(urlopen, urls)
#close the pool and wait for the work to finish 
pool.close() 
pool.join() 
print(results)
```


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-1-d29bef5540ac> in <module>()
    ----> 1 from urllib.request import urlopen
          2 from multiprocessing.dummy import Pool as ThreadPool
          3 
          4 urls = [
          5   'http://www.python.org',


    ImportError: No module named request


### Communication between the processes

Running a computation in multiple processes requires some communication between these processes. One of the nice aspects of multiprocessing in Python is that most of the time you do not need to know how this communication is handled: it just works. However, it is useful to understand the basics of this mechanism in order to figure out how to solve two kinds of problems: unexpected errors, and bad performance.

Communication between processes takes the form of streams of bytes that travel through specific communication channels. To send an object from one process to another, Python has to convert it to a stream of bytes, and assemble the object back at the receiving end. Python's mechanism for doing these conversions was originally designed for storing objects in files and is implemented in the pickle module. Every argument that is passed to a Python function running in another process is pickled and then unpickled. The result of the function undergoes the same process on its way back.

There are two things you need to know about pickle in the context of multiprocessing. First, most objects can be pickled but some cannot. Second, pickling and unpickling take time and can sometimes add considerable overhead to your multiprocessing.

The objects that cannot be pickled come in two varieties: those for which pickling does not make sense, and those for which it has simply not been implemented. A good example for the first category is file objects. The second category contains mainly object types defined in extension modules whose authors didn't implement pickling. If you use an old release of NumPy, you may discover that its array-aware functions are not picklable, making it impossible to use such a function directly as a task in multiprocessing. For Python's built-in objects, there is one important restriction that is due to the implementation details of pickle: functions and classes can only be pickled if they are defined at the top level of a module. This means, for example, that if you define a function inside another function, you cannot pickle it and thus not pass it to a multiprocessing task.

The performance implications of pickling are rather obvious: you should try to pass as few arguments as possible to your tasks, and make sure you pass no more data than you really need to. For example, rather than passing a huge list and the index of the item that your taks is supposed to process, you should pass only that item.

### Key Points

- CPU multi-processing is a parallel programming technique that can harness the power of modern computers to help you perform more tasks more quickly.
- The Python multiprocessing library allows you to create a pool of workers to carry out tasks in parallel
- Tasks are easy to describe using Python functions
- Care needs to be taken when executing code in parallel environments to avoid strange program behavior and wrong computations
- You can combine results from individual tasks allowing each worker to share in the computational load
- It is important to use profiling before optimizing computer programs
- Metrics such as speedup and efficiency aid in evaluating the performance and utility of parallel programs

*** Original Document: https://philipwfowler.github.io/2015-01-13-oxford/intermediate/python/04-multiprocessing.html ***

## Threading Vs Parallelism

The threading module uses threads, the multiprocessing module uses processes. The difference is that threads run in the same memory space, while processes have separate memory. This makes it a bit harder to share objects between processes with multiprocessing. Since threads use the same memory, precautions have to be taken or two threads will write to the same memory at the same time. This is what the global interpreter lock is for.

Spawning processes is a bit slower than spawning threads. Once they are running, there is not much difference.

### Pros

| Threading                                                                      | Parallelism                                                                                                                                |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Lightweight - low memory footprint                                             | Separate memory space                                                                                                                      |
| Shared memory - makes access to state from another context easier              | Code is usually straightforward                                                                                                            |
| Allows you to easily make responsive UIs                                       | Takes advantage of multiple CPUs & cores                                                                                                   |
| cPython C extension modules that properly release the GIL will run in parallel | Avoids GIL limitations for cPython                                                                                                         |
| Great option for I/O-bound applications                                        | Eliminates most needs for synchronization primitives unless if you use shared memory (instead, it's more of a communication model for IPC) |
|                                                                                | Child processes are interruptible/killable                                                                                                 |
|                                                                                | Python multiprocessing module includes useful abstractions with an interface much like threading.Thread                                    |
|                                                                                | A must with cPython for CPU-bound processing                                                                                               |

### Cons

| Threading                                                                                                                                                                                            | Parallelism                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| cPython - subject to the GIL                                                                                                                                                                         | IPC a little more complicated with more overhead (communication model vs. shared memory/objects) |
| Not interruptible/killable                                                                                                                                                                           | Larger memory footprint                                                                          |
| If not following a command queue/message pump model (using the Queue module), then manual use of synchronization primitives become a necessity (decisions are needed for the granularity of locking) |                                                                                                  |
| Code is usually harder to understand and to get right - the potential for race conditions increases dramatically                                                                                     |                                                                                                  |
