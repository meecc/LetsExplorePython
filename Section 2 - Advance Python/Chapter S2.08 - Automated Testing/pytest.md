
# pytest

The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.



```python
# content of test_sample.py
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5
```

## Benefits 

- Allows for compact test suites
> The idioms that pytest first introduced brought a change in the Python community because they made it possible for test suites to be written in a very compact style, or at least far more compact than was ever possible before.
> Pytest basically introduced the concept that Python tests should be plain Python functions instead of forcing developers to include their tests inside large test classes.

- Minimal boilerplate
> Tests written with pytest need very little boilerplate code, which makes them easy to write and understand.

- Tests parametrization
> You can parametrize any test and cover all uses of a unit without code duplication.

- Very pretty and useful failure information
> Pytest rewrites your test so that it can store all intermediate values that can lead to failing assert and provides you with very pretty explanation about what has been asserted and what have failed.

- Fixtures are simple and easy to use
> A fixture is just a function that returns a value and to use a fixture you just have to add an argument to your test function. You can also use a fixture from another fixture in the same manner, so it's easy to make them modular.
You can also parametrize fixture and every test that uses it will run with all values of parameters, no test rewrite needed. If your test uses several fixtures, all parameters' combinations will be covered.

- Pdb just works
> Pytest `**automagically**` (and safely) disables output capturing when you're entering pdb, so you don't have to redirect debugger to other console or bear huge amount of unneeded output from other tests.

- Test discovery by file-path

- Over 150 plugins 
> more than 150 plugins to customise py.test such as pytest-BDD and pytest-konira for writing tests for Behaviour Driven Testing

## Issues 

- Compatibility Issues
> The fact that pytest uses it's own special routines to write tests means that you are trading convenience for compatibility. In other words, writing tests for pytest means that you are tying yourself to only pytest and the only way to use another testing framework is to rewrite most of the code.

## Salient Features

- Pytest Fixtures
- Introspect agent
- Test parametrization
- Pytest Markers (Custom and inbuilt)
- Plugins

## Usage 

pytest can be called using any of the below methods

```
python -m pytest test_file.py
py.test test_file.py
pytest test_folder 
pytest test_file.py
```

### Python Fixtures

Fixture is one of the most important concept in pytest. They have taken the concept of setup and teardown to next level by adding many customization such as 
- Function level selection
- Module based selection

Also, they can be used to provide baseline on which tests can be repeatedly executed reliably. 

- Fixtures have explicit names and are activated by declaring them in test functions, modules, classes or whole projects
- Fixtures are modular, and each fixture triggers a fixture function which can use other fixtures
- You can choose to parametrize fixtures and tests according to configuration and component options, or to re-use fixtures across class, module or whole test session scopes

Any method can be marked as fixture by adding `@pytest.fixture` gecorator to it.


```python
import pytest

@pytest.fixture()
def my_fixture():
    print ("This is a fixture")
    
def test_my_fixture(my_fixture):
    print ("I'm the test")

```


```python
#pyfixture_1.py
import pytest
import pytest

@pytest.fixture()
def my_fixture():
    print ("This is a fixture")
    
def test_my_fixture(my_fixture):
    print ("I'm the test")


@pytest.fixture
def tester(request):
    """Create tester object"""
    print(request.param)
    return MyTester(request.param)


class TestIt:
    @pytest.mark.parametrize('tester', [['var1', 'var2']], indirect=True)
    def test_tc1(self, tester):
       tester.dothis()
       assert 1
```

## Specifying tests / selecting tests

```
pytest test_mod.py   # run tests in module
pytest somepath      # run all tests below somepath
pytest -k stringexpr # only run tests with names that match the
                      # "string expression", e.g. "MyClass and not method"
                      # will select TestMyClass.test_something
                      # but not TestMyClass.test_method_simple
pytest test_mod.py::test_func  # only run tests that match the "node ID",
                                # e.g. "test_mod.py::test_func" will select
                                # only test_func in test_mod.py
pytest test_mod.py::TestClass::test_method  # run a single method in
                                             # a single class

```

## Running multiple tests

pytest will run all files in the current directory and its subdirectories of the form test_*.py or *_test.py. More generally, it follows standard test discovery rules.

> pytest somepath  

## Asserting that a certain exception is raised


```python
# content of test_sysexit.py
import pytest
def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
```

## Grouping multiple tests in a class


```python
class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')
```

## Good Integration Practices

### Conventions for Python test discovery

pytest implements the following standard test discovery:

- If no arguments are specified then collection starts from testpaths (if configured) or the current directory. Alternatively, command line arguments can be used in any combination of directories, file names or node ids.
- Recurse into directories, unless they match norecursedirs.
- In those directories, search for test_*.py or *_test.py files, imported by their test package name.
- From those files, collect test items:
    - test_ prefixed test functions or methods outside of class
    - test_ prefixed test functions or methods inside Test prefixed test classes (without an __init__ method)
    
For examples of how to customize your test discovery Changing standard (Python) test discovery.

Within Python modules, pytest also discovers tests using the standard unittest.TestCase subclassing technique.

### Choosing a test layout / import rules

pytest supports two common test layouts:

#### Tests outside application code

Putting tests into an extra directory outside your actual application code might be useful if you have many functional tests or for other reasons want to keep tests separate from actual application code (often a good idea):

```
setup.py
mypkg/
    __init__.py
    app.py
    view.py
tests/
    test_app.py
    test_view.py
    ...```

If you need to have test modules with the same name, you might add __init__.py files to your tests folder and subfolders, changing them to packages:
```
setup.py
mypkg/
    ...
tests/
    __init__.py
    foo/
        __init__.py
        test_view.py
    bar/
        __init__.py
        test_view.py```

In this situation, it is strongly suggested to use a src layout where application root package resides in a sub-directory of your root:
```
setup.py
src/
    mypkg/
        __init__.py
        app.py
        view.py
tests/
    __init__.py
    foo/
        __init__.py
        test_view.py
    bar/
        __init__.py
        test_view.py
```

#### Tests as part of application code

Inlining test directories into your application package is useful if you have direct relation between tests and application modules and want to distribute them along with your application:
```
setup.py
mypkg/
    __init__.py
    app.py
    view.py
    test/
        __init__.py
        test_app.py
        test_view.py
        ...
```


In this scheme, it is easy to your run tests using the --pyargs option:

```pytest --pyargs mypkg```

pytest will discover where mypkg is installed and collect tests from there.

Note that this layout also works in conjunction with the src layout mentioned in the previous section.

## Calling pytest from Python code

You can invoke pytest from Python code directly:


```python
pytest.main()
```

this acts as if you would call “pytest” from the command line. It will not raise SystemExit but return the exitcode instead. You can pass in options and arguments:


```python
pytest.main(['-x', 'mytestdir'])
```
