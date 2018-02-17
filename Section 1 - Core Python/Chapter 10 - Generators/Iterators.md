
# Iterators

Python iterator objects are required to support two methods while following the iterator protocol.

- `__iter__` returns the iterator object itself. This is used in for and in statements.

- `__next__` method returns the next value from the iterator. If there is no more items to return then it should raise StopIteration exception.
