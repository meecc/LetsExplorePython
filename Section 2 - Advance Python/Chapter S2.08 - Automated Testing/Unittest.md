
# Unittest

unittest is the batteries-included test module in the Python standard library. Its API will be familiar to anyone who has used any of the JUnit/nUnit/CppUnit series of tools.

The unittest library is inspired by the JUnit library. It can be used to create a comprehensive suite of tests. It is used within the Python project for testing. It's documentation is available at http://docs.python.org/3/library/unittest.html.




```python
# import unittest
# help(unittest)
```

## What is assert ?


```python
# Run Examples from command line 
import unittest

def multiply(a, b):
    """
    >>> multiply(4, 3)
    12
    >>> multiply('a', 3)
    'aaa'
    """
    return a * b
    
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual(multiply(3, 4), 12)
 
    def test_strings_a_3(self):
        self.assertEqual(multiply('a', 3), 'aaa')
        
    def test_string_a_b(self):
        self.assertFalse(multiply('a', 'b'))
```

## Asserts 

| Method                    | Checks that          |    meaning            |
|---------------------------|----------------------|-----------------------|
| assertEqual(a, b)         | a == b               |                       |
| assertNotEqual(a, b)      | a != b               |                       |
| assertTrue(x)             | bool(x) is True      |                       |
| assertFalse(x)            | bool(x) is False     |                       |
| assertIs(a, b)            | a is b               | Test that first and second evaluate to the same object.                      |
| assertIsNot(a, b)         | a is not b           |Test that first and second or don’t evaluate to the same object.                      |
| assertIsNotNone(x)        | x is not None        |                        |
| assertIsNone(x)           | x is None            |                       |
| assertIn(a, b)            | a in b               |                       |
| assertNotIn(a, b)         | a not in b           |                       |
| assertIsInstance(a, b)    | isinstance(a, b)     |                       |
| assertNotIsInstance(a, b) | not isinstance(a, b) |                       |


```python
a = d = 10
b = [12]
c = [10]
from unittest import TestCase
tc = unittest.TestCase('__init__')
```

### assertEqual


```python
print(tc.assertEqual(a, a))
```


```python
print(tc.assertEqual(a,b))
```


```python
print(tc.assertEqual(a,c))
```


```python
print(tc.assertEqual(a,d))
```

### assertTrue


```python
print(tc.assertTrue(a == a))
```


```python
print(tc.assertTrue(a < b))
```


```python
print(tc.assertTrue(a == c))
```


```python
print(tc.assertTrue(a,d))
```

### assertFalse


```python
print(tc.assertFalse(a == a))
```


```python
print(tc.assertFalse(a > b))
```


```python
print(tc.assertFalse(a == c))
```


```python
print(tc.assertFalse(a,d))
```

### assertIs


```python
print(tc.assertIs(a, a))
```

    None



```python
print(tc.assertIs(a,b))
```


```python
print(tc.assertIs(a,c))
```


```python
print(tc.assertIs(a,d))
```

### assertIsNot


```python
print(tc.assertIsNot(a, a))
```


```python
print(tc.assertIsNot(a,b))
```


```python
print(tc.assertIsNot(a,c))
```


```python
print(tc.assertIsNot(a,d))
```

### assertIsNone


```python
print(tc.assertIsNone(a/a))
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-4-75a3157d62fe> in <module>()
    ----> 1 print(tc.assertIsNone(a/a))
    

    /usr/lib64/python2.7/unittest/case.pyc in assertIsNone(self, obj, msg)
        952         if obj is not None:
        953             standardMsg = '%s is not None' % (safe_repr(obj),)
    --> 954             self.fail(self._formatMessage(msg, standardMsg))
        955 
        956     def assertIsNotNone(self, obj, msg=None):


    /usr/lib64/python2.7/unittest/case.pyc in fail(self, msg)
        408     def fail(self, msg=None):
        409         """Fail immediately, with the given message."""
    --> 410         raise self.failureException(msg)
        411 
        412     def assertFalse(self, expr, msg=None):


    AssertionError: 1 is not None


### assertIsNotNone


```python
print(tc.assertIsNotNone(a))
```

    None


### assertIn


```python
print(tc.assertIn(a, a))
```

### assertNotIn


```python
print(tc.assertNotIn(a, a))
```

### assertIsInstance


```python
print(tc.assertIsInstance(tc, object))
```

    None



```python
print(tc.assertIsInstance(a,b))
```


```python
print(tc.assertIsInstance(a,c))
```


```python
print(tc.assertIsInstance(a,d))
```

### assertNotIsInstance


```python
print(tc.assertNotIsInstance(tc, object))
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-10-3f38e7913ee1> in <module>()
    ----> 1 print(tc.assertNotIsInstance(tc, object))
    

    c:\apps\miniconda3\lib\unittest\case.py in assertNotIsInstance(self, obj, cls, msg)
       1241         if isinstance(obj, cls):
       1242             standardMsg = '%s is an instance of %r' % (safe_repr(obj), cls)
    -> 1243             self.fail(self._formatMessage(msg, standardMsg))
       1244 
       1245     def assertRaisesRegex(self, expected_exception, expected_regex,


    c:\apps\miniconda3\lib\unittest\case.py in fail(self, msg)
        664     def fail(self, msg=None):
        665         """Fail immediately, with the given message."""
    --> 666         raise self.failureException(msg)
        667 
        668     def assertFalse(self, expr, msg=None):


    AssertionError: <unittest.case.TestCase testMethod=__init__> is an instance of <class 'object'>



```python
class A:
    pass
class B:
    pass
class C(A):
    pass
```


```python
a = A
b = B
c = C
```


```python
print(tc.assertNotIsInstance(a, A))
```

    None



```python
print(tc.assertNotIsInstance(a,B))
print(type(b), type(a))
```

    None
    <class 'type'> <class 'type'>


## Test execution from command line

The unittest module can be called from command line to run tests from `modules`, `classes` or even individual `test methods` as shown below

```
python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method
```

## Programatically select the test cases


```python
suite = unittest.TestLoader().loadTestsFromModule(TestUM())
print(dir(suite))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestUMSubtraction))
unittest.TextTestRunner().run(suite)
```

or, use the following method


```python
def suite():
    tests = ['TestUM', 'TestUMSubtraction']

    return unittest.TestSuite(map(WidgetTestCase, tests))
```

## Skipping test cases  


```python
class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass
```


```python
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertEqual( multiply(3,4), 12)
 
    def test_strings_a_3(self):
        self.assertEqual( multiply('a',3), 'aaa')
        
    def test_string_a_b(self):
        try:
            self.assertFalse(multiply('a','b'))
        except Exception as e:
            return False
        
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")
        
    def skipUnlessHasattr(obj, attr):
        if hasattr(obj, attr):
            return lambda func: func
        return unittest.skip("{!r} doesn't have {!r}".format(obj, attr))
```


```python
suite = unittest.TestLoader().loadTestsFromModule(TestUM())
print(dir(suite))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestUMSubtraction))
unittest.TextTestRunner().run(suite)
```

# References


