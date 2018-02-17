
## String



*Strings* are Python *builtins* datatype for handling text. They are **immutable** thus you can **not add, remove or change** any character in a *string*. To perform these operations, Python needs to create a new *string*.

> Since Python 3, strings are by default unicode string.

Types:

+ Standard String: `s = 'Chandu\tNalluri'` # Chandu   Nalluri
+ Raw String: `a = r'Roshan\tMusheer'` # Roshan\tMusheer
+ Unicode String: `u = u'Björk'`

> The standard *string* can be converted to *unicode* by using the function `unicode()`.

String can be initialized using:

+ With single or double quotes ('', "").
+ On several consecutive lines, provided that it's between three single or double quotes (''' ''', """ """).
+ Without expansion characters (example: `s = r '\ n'`, where `s` will contain the characters `\` and `n`).




```python
a = r'Roshan\tMusheer'
print(a)
```

    Roshan\tMusheer



```python
path = "C:\new_data\technical_jargons"
print(path)
path = R"C:\new_data\technical_jargons"
print(path)
```

    C:
    ew_data	echnical_jargons
    C:\new_data\technical_jargons



```python
a = 'Roshan\tMusheer'
print(a)
```

    Roshan	Musheer


### String Operations:


```python
s = 'Camel'
s = 'The ' + s + ' ran away!'
# Concatenation
print(s)
st = 'The ' + s + ' ran away!'
print(st)
print(id(st))
print(id(s))

```

    The Camel ran away!
    The The Camel ran away! ran away!
    139651602524888
    139651602147488



```python
# Interpolation
"""
string interpolation (or variable interpolation, variable substitution, 
or variable expansion) is the process of evaluating a string literal 
containing one or more placeholders, yielding a result in which the 
placeholders are replaced with their corresponding values.
"""
print( 'Size of %s => %d' % (s, len(s)))
print(dir(s))
print( 'Size of %s => %d' % (s, s.__len__()))

def size(strdata):
    c = 0
    for a in strdata:
        c+=1
    return c

print(size("Anshu"))
```

    Size of Camel => 5
    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
    Size of Camel => 5
    5



```python
# String processed as a sequence
s = "Murthy "
for ch in s: print(ch , end=',') # This 
# print(help(print))
print("\b.")
print("~"*79)
```

    M,u,r,t,h,y, ,.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



```python
# Strings are objects
if s.startswith('M'): print(s.upper())

print(s.lower())
print("~"*79)

# what will happen? 
print(3*s) 

# print(dir(s))
```

       murthy 
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       Murthy    Murthy    Murthy 



```python
s = "   Murthy "
age = 5
print(s + str(age))
print(s.strip(), age)
# print(s + age)
```

       Murthy5
    Murthy 5



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-12-d14538833000> in <module>()
          3 print(s + str(age))
          4 print(s.strip(), age)
    ----> 5 print(s + age)
    

    TypeError: must be str, not int



```python
st = "    Mayank Johri    "
print(len(st))
s = st.strip()
print(len(s))
print(st.rstrip())
print(st.lstrip())
```

    20
    12
        Mayank Johri
    Mayank Johri    



```python
m = "Mohan Shah"
x = ["mon", "tues", "wed"]
y = ","
a = "On Leave"
print(y.join(x)) # -> mon,tues,wed
print(m.join(y)) 
print(a.join(y))
print(y.join(a)) 
print(a.join(m)) 
```

    mon,tues,wed
    ,
    ,
    O,n, ,L,e,a,v,e
    MOn LeaveoOn LeavehOn LeaveaOn LeavenOn Leave On LeaveSOn LeavehOn LeaveaOn Leaveh


The operator `%` is used for string interpolation. The interpolation is more efficient in use of memory than the conventional concatenation.

Symbols used in the interpolation:

+ %s: *string*.
+ %d: integer.
+ %o: octal.
+ %x: hexacimal.
+ %f: real.
+ %e: real exponential.
+ %%: percent sign.

Symbols can be used to display numbers in various formats.

*Example*:


```python
# Zeros left
print ('Now is %02d:%02d.' % (6, 30))

# Real (The number after the decimal point specifies how many decimal digits )
print ('Percent: %.1f%%, Exponencial:%.2e' % (5.333, 0.00314))

# Octal and hexadecimal
print ('Decimal: %d, Octal: %o, Hexadecimal: %x' % (10, 10, 10))
```

    Now is 06:30.
    Percent: 5.3%, Exponencial:3.14e-03
    Decimal: 10, Octal: 12, Hexadecimal: a


### format
In addition to interpolation operator `%`, the string method and function `format()` is available.

> The function `format()` can be used only to format one piece of data each time.

*Examples*:


```python
peoples = [('Mayank', 'friend', 'Manish'),
('Mayank', 'reportee', 'Roshan Musheer')]

# Parameters are identified by order
msg = '{0} is {1} of {2}'

for name, function, friend in peoples:
    print(msg.format(name, function, friend))

# Parameters are identified by name
msg = '{greeting}, it is {hour:02d}:{minute:02d}'

print(msg.format(greeting='Good Morning', hour=9, minute=30))
print(msg)
# Builtin function format()
print ('Pi =', format(3.14159, '.3e'))
print ('Pi =', format(3.14159, '.1e'))
```

    Mayank is friend of Manish
    Mayank is reportee of Roshan Musheer
    Good Morning, it is 09:30
    {greeting}, it is {hour:02d}:{minute:02d}
    Pi = 3.142e+00
    Pi = 3.1e+00


### `str` in-build module

Strings implement all of the common sequence operations, along with the additional methods described below.


```python
myStr = "maya Deploy, version: 0.0.3 "

print(myStr.capitalize())
print(myStr.center(60))
print(myStr.center(60, "*"))
print(myStr.center(10, "*"))

print(myStr.count('a'))
print(myStr.count('e'))

print(myStr.endswith('all'))

print(myStr.endswith('.0.3'))
print(myStr.endswith('.0.3 '))

print(myStr.find("g"))
print(myStr.find("e"))
```

    Maya deploy, version: 0.0.3 
                    maya Deploy, version: 0.0.3                 
    ****************maya Deploy, version: 0.0.3 ****************
    maya Deploy, version: 0.0.3 
    2
    2
    False
    False
    True
    -1
    6


> **Note**: The find() method should be used only if you need to know the position of sub. To check if sub is a substring or not, use the in operator:

checking: substring in main_string : returns true or false


```python
print("m" in myStr)
```

    True



```python
print("M" in myStr)
```

    False



```python
c = "one"
print(c.isalpha())
c = "1"
print(c.isalpha())
```

    True
    False



```python
superscripts = "\u00B2"
five = "\u0A6B"
#str.isdecimal() (Only Decimal Numbers)
print(five)
print(c.isdecimal())
print(five.isdecimal())
print("10 ->", "10".isdecimal())
print("10.001".isdecimal())

str = u"this 2009";  
print(str.isdecimal())

str = u"23443434";
print(str.isdecimal())
print(fractions.isdecimal())
```

    ੫
    True
    True
    10 -> True
    False
    False
    True
    False



```python
# str.isdigit() (Decimals, Subscripts, Superscripts)
fractions = "\u00BC"
print(fractions)
print(c.isdigit())
print(fractions.isdigit())
print(five.isdigit())

print("10".isdigit())
str = u"this 2009";  
print(str.isdigit())

str = u"23443.434";
print(str.isdigit())
```

    ¼
    True
    False
    True
    True
    False
    False



```python
print(superscripts)
print(superscripts.isdigit())
print(superscripts.isdecimal()) 
print(superscripts+superscripts)
print(fractions+fractions)
```

    ²
    True
    False
    ²²
    ¼¼



```python
# str.isnumeric() (Digits, Fractions, Subscripts, Superscripts, Roman Numerals, Currency Numerators)
print(fractions)
print(fractions.isnumeric())
print(five.isnumeric())
```

    ¼
    True
    True



```python
print(myStr.isalnum())
print("one".isalnum())
print("thirteen".isalnum())
```

    False
    True
    True


### String Module
-----

Various functions for dealing with text are implemented in the module *string*.


```python
import string

# the alphabet
print(dir(string))
a = string.ascii_letters
print(a)
# Shifting left the alphabet
b = a[1:] + a[0]
print(b)
print(b.__doc__)
print(string.digits)
print(string.hexdigits)
print(help(string.printable))
```

    ['ChainMap', 'Formatter', 'Template', '_TemplateMetaclass', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_re', '_string', 'ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'capwords', 'digits', 'hexdigits', 'octdigits', 'printable', 'punctuation', 'whitespace']
    abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZa
    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str
    
    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.
    0123456789
    0123456789abcdefABCDEF
    no Python documentation found for '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    
    None


#### Template

The module also implements a type called *Template*, which is a model *string* that can be filled through a dictionary. Identifiers are initialized by a dollar sign ($) and may be surrounded by curly braces, to avoid confusion.

Example:


```python
import string

# Creates a template string
st = string.Template('$warning occurred in $when $$what')

# Fills the model with a dictionary
s = st.substitute({'warning': 'Lack of electricity',
    'when': 'April 3, 2002'})

# Shows:
# Lack of electricity occurred in April 3, 2002
print(s)
```

    Lack of electricity occurred in April 3, 2002 $what



```python
# Unicode String 
u = u'Hüsker Dü'
# Convert to str
s = u.encode('latin1')
print (s, '=>', type(s))

# String str
s = 'Hüsker Dü'
# u = s.decode('latin1')

print (repr(u), '=>', type(u))
```

    b'H\xfcsker D\xfc' => <class 'bytes'>
    'Hüsker Dü' => <class 'str'>


To use both methods, it is necessary to pass as an argument the compliant coding. The most used are "latin1" "utf8".
