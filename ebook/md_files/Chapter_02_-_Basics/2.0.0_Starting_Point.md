
# Starting Point
------------

In this section we will try to cover the starting point of python programming, which will help us understand the code. Lets start with few **Built-in Functions** without which you will not be able to understand this tutorial. We have seperate section for discussing them in details. 

## Basic functions

* `print`: It prints the provided data on standard output, which is in most cases is the console. It inserts spaces between expressions that are received as a parameter, and a newline character at the end, unless it receives a comma at the end of the parameter list.


```python
print("!!! स्वागतम् !!!")
print("!!! Welcome !!!")
print("!!! Willkommen !!!")
```

    !!! स्वागतम् !!!
    !!! Welcome !!!
    !!! Willkommen !!!


* `pass`: This function does nothing and acts only as a placeholder for the implementation in future.


```python
pass
```

* `id`: Return the “identity” of an object. This is an integer (or long integer) which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.

> **NOTE**: CPython implementation detail: This is the address of the object in memory.

* `input`: If the prompt argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that. When EOF is read, EOFError is raised


```python
name = input("Welcome to the funzone, Please provide your name: ")
```

    Welcome to the funzone, Please provide your name: Mayank Johri

