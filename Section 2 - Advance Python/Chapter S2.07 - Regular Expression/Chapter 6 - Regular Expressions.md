
# Chapter 6 - Regular Expressions

Original URL: https://github.com/mikekestemont/ghent1516/blob/master/Chapter%206%20-%20Regular%20Expressions.ipynb

Regular expressions are another, powerful way of handling strings in Python. You can use them for all sorts of very common string operations, like searching words and replacing them in texts. In fact, regular expressions are often used across many programming languages and text editors. Because of that, you will often be able to reuse many of the things that you will learn about below. The functionality for using regular expressions in Python is included in the 're' package, which you should be able to import as usual: 


```python
import re
```

On many occasions, you will want to search a string in your scripts: e.g. does the following word appear in a text? Is the format of the following email address valid and does it contain an @-symbol and a least one dot? To carry out such operations, the first thing you need is a string to search:  


```python
s = "In principio erat verbum, et verbum erat apud Deum."
```

The next thing we define is the actual regular expression which we will use, or the string that we will use to search the sentence we defined above. We pass this string to the `compile()` function in the `re` package, which will allow fast searching later on. Note that we put an `r` in front of this string when we initialize it, which turns our string into a so-called 'raw string'. While this is not always necessary, it is a good idea to do this consistently when dealing with regular expressions.


```python
pattern = re.compile(r"verbum")
```

Next, we can call the `sub()` function from the `re` package on this pattern, in order to replace (or 'substitute') our pattern with another word, like this:


```python
text = pattern.sub("XXX", s)
print(text)
```

    In principio erat XXX, et XXX erat apud Deum.



```python
help(re.sub)
```

    Help on function sub in module re:
    
    sub(pattern, repl, string, count=0, flags=0)
        Return the string obtained by replacing the leftmost
        non-overlapping occurrences of the pattern in string by the
        replacement repl.  repl can be either a string or a callable;
        if a string, backslash escapes in it are processed.  If it is
        a callable, it's passed the match object and must return
        a replacement string to be used.
    



```python
text = re.sub("ABC", )
```

Note the order of the arguments passed to `sub()`: first, the word we would like to replace our pattern with, and secondly our original string. We can just as easily get back our original string:


```python
pattern2 = re.compile(r"XXX")
text = pattern2.sub("verbum", s)
print(text)
```

So far nothing special: we are simply replacing one word for another word. The smart ones among you will have noticed that we could have achieved the exact same result using the `replace()` function, which we came across in an earlier chapter. But now: say you would like to replace all vowels in a string. With regular expressions, this is a piece of cake:


```python
vowel_pattern = re.compile(r"a|e|o|u|i")
without_vowels = vowel_pattern.sub("X", s)
print(without_vowels)
```

Note how our pattern allows for a special syntax: the pipe symbol which we used allows to express that one character OR another one is fine for the regular expression to match. Oops: the capital letter at the beginning of the sentence hasn't been replaced because we only included lowercase vowels in our pattern definition. Let's add the uppercase vowels to the regex:   


```python
vowel_pattern = re.compile(r"a|A|e|E|o|O|u|U|i|I")
without_vowels = vowel_pattern.sub("X", s)
print(without_vowels)
```

There is in fact an easy way to match all lowercase and uppercase characters in a string, like this:


```python
ups = re.compile(r"[A-Z]")
lows = re.compile(r"[a-z]")
without_ups = ups.sub("X", s)
print(without_ups)
without_ups = lows.sub("X", s)
print(without_ups)
```

These specific patterns are called 'ranges': they will match any lowercase or uppercase letter. In fact, you can use such a range syntax using squared brackets, to replace the pipe syntax we used earlier. 


```python
vowel_pattern = re.compile(r"[aeoui]")
without_vowels = vowel_pattern.sub("M", s)
print(without_vowels)
```

    In prMncMpMM MrMt vMrbMm, Mt vMrbMm MrMt MpMd DMMm.


You can also look for more specific, as well as longer letter groups by arranging them with round brackets:


```python
p = re.compile(r"(ri)|(um)|(Th)")
print(vowel_pattern.sub("A", s))
```

    In prAncApAA ArAt vArbAm, At vArbAm ArAt ApAd DAAm.


There is also a syntax to match any character (except the newline):


```python
any_char = re.compile(r".")
print(any_char.sub("X", s))
```

If you would like your expression to match an actual dot, you have to escape it using a backslash:


```python
dot = re.compile(r"\.")
print(dot.sub("X", s))
```

By the way, there exist more characters that you might have to escape using a backslash. This is because they are part of the syntax that use to define regular expressions: if you don't escape them, Python will not know that you are looking for an literal match. Characters that you typically might want to escape include: ( + ? . * ^ $ ( ) [ ] { } | \ ) ,. For example:


```python
s = "In principio [erat] verbum, et verbum erat apud Deum."
brackets_wrong = re.compile(r"[|]")
print(brackets_wrong.sub("X", s))
brackets_right = re.compile(r"(\[)|(\])")
print(brackets_right.sub("X", s))
```

The syntax for regular expression includes a whole range of possibilities which we simply cannot all deal with it here. Because of that we will stick to a number of helpful examples. An interesting feature is that you can specify whether or not a character really has to occur. You can check whether the pattern occurs in a string using the `match()` function which will return `None` if it doesn't find the pattern in the string searched:


```python
pattern = re.compile(r"m{2,4}")
print(pattern.match(""))
print(pattern.match("m"))
print(pattern.match("mm"))
print(pattern.match("mmm"))
print(pattern.match("mmmm"))
print(pattern.match("mmmmm"))
print(pattern.match("mmmmmm"))
print(pattern.match("mmmmammm"))
```

With the curly brackets, you indicate that you are only interested in the letter 'm' if it occurs 2,3 or 4 times in a row in the string you search. Because `None` is returned if not a single match was found, you can use the outcome of `match()`in an if-statement. The following example shows how you can also use the curly brackets to match an exact number of occurences (in this case three a's).


```python
pattern = re.compile(r"a{5}")
if pattern.match("aaaaa"):
    print("Found it!")
else:
    print("Nope...")
# or:
if pattern.match("aa"):
    print("Found it!")
else:
    print("Nope...")
```

Using a plus sign you can indicate whether you want to match multiple occurrences of a character. A good example from the world of paper writing are double spaces, which can be hard to spot. In the code block below, we replace all multiple occurences of a whitespace character by a single whitespace character. Note that you can use the whitespace character just like any other character (you don't have to escape it). Multiple occurences of the whitespace character will be matched: it doesn't matter how many, as long as there is at least one:


```python
paper = "My thesis on  biology     contains a lot of  double spaces.   I will remove  them."
mult = re.compile(r" +")
print(mult.sub(" ", paper))
```

A similar piece of functionality is offered by the asterisk operator: here you can match multiple occurences of the same character in a row OR not a single one. Note the subtle difference with respect to the plus operator, which needs at least a single occurence of the character to match. Here we use the `search()` function which will search the entire string: the `match()` function which we used earlier will only look for matches at the very beginning of a string. Keep this in mind! The final pattern below yields a match, although there is not a single 'x' in the sentence. That is because the pattern with the asterisk says: "a single x, or no x at all". 


```python
s = "In English some letters occur multiple times in a row."
p1 = re.compile(r"t")
p2 = re.compile(r"t+")
p3 = re.compile(r"x")
p4 = re.compile(r"x*")
print(p1.search(s))
print(p2.search(s))
print(p3.search(s))
print(p4.search(s))
```

    <_sre.SRE_Match object; span=(18, 19), match='t'>
    <_sre.SRE_Match object; span=(18, 20), match='tt'>
    None
    <_sre.SRE_Match object; span=(0, 0), match=''>



```python
print(p2.search(s))
```

    <_sre.SRE_Match object; span=(18, 20), match='tt'>


Interestingly, you also use regular expression to search inside words. Can you explain why the following patterns (don't) match? 


```python
candidates = ["good", "god", "gud", "gd"]
p = re.compile(r"go+d")
for c in candidates:
    print(p.match(c))
```

Speaking of words: it might be interesting to know that you can use regular expressions for advanced string splitting. If you want to split a sentence across all whitespace characters for instance, you can use an espaced `\s`. This operator will match all whitespace characters, such as tabs, linebreaks, normal spaces etc. If you add a `+` sign, your pattern will match series of whitespace characters: 


```python
s = """This is a text  on three   lines
with  multiple instances of  
double spaces."""
whitespace = re.compile(r"\s+")
print(whitespace.split(s))
```

If you would have wanted to split on the linebreaks only (possible followed by e.g. spaces), you could have used the following pattern:


```python
s = """This is a text  on three   lines
with  multiple instances of  
double spaces."""
whitespace = re.compile(r"\s*\n\s*")
print(whitespace.split(s))
```

    ['This is a text  on three   lines', 'with  multiple instances of', 'double spaces.']


If we want to correct the double spaces, we could now do:    


```python
ds = re.compile(r" +")
for line in whitespace.split(s):
    print ds.sub(" ", line)
```

One final feature we should mention is the `[^...]` syntax: this will match any character that is NOT between the brackets. Remember the vowel_pattern above? Using the caret symbol we can quickly 'invert' this pattern, so that it will match all consonants:


```python
s = "these are vowels and consonants"
consonants = re.compile(r"[^aeuoi]")
print(consonants.sub("X", s))
```

Regular expressions are really useful, but they can get tricky as well as difficult to read, because of the many different options that exist. There is a whole range of special symbols which you can use to match nearly everything in a text, from word boundaries (\b) to digits (\d) etc. Don't learn these by heart but look up a good reference list online (like http://www.tutorialspoint.com/python/python_reg_expressions.htm). As usual Stackoverflow will prove really useful when you search for information online.

# Final Exercises Chapter 6

- Ex. 1 - Write Python code that loads data items from a file that has the format below. Use regular expresions to parse the lines and the data fields: take care of the multiple whitespace characters that might occur. Fill a dictionary using the two data fields. Use regular expressions as much as possible!

Example data:

color = red

number =7

name= joe

age =   9
...


- Ex. 2 - In the scientific community you will often find data online that has been stored in '.csv' format. Each data item in these files is represented on separate line. Write a function that takes a csv-filename as only input parameter and return a lists of lists, containing the data fields for each item.

Example data:

Mike, 28, scientist, Belgium

Lars, 49, research director, Luxemburg

Matt, 52, rockstar, US

Example output:
[["Mike","28","scientist","Belgium"],["Lars","49","research director","Luxemburg"], ...]

- Ex. 3 - Expand the previous excercise (don't throw away the original version!). Assume that the first line of your csv-file is not a real data-entry, but a so-called header-line that contains the names of the data fields stored in your csv-file. Now, have your function return a list of dictionaries: one for data item, containing for each item the value for each data field which you find.

Example data:
name, age, profession, country

Mike, 28, scientist, Belgium

Lars, 49, research director, Luxemburg

Matt, 52, rockstar, US
...
Example output:
[{"name": "Mike", "age": "28", "profession":"scientist", "country":"Belgium"}, {"name": "Lars", "age": "49", "profession":"research director", "country":"Luxemburg"]}, ...]

- Ex. 4 - Write a function that reads a random text file, splits the words across whitespace instances and returns a set containing all words that contain at least two characters. Use regular expressions where possible!

- Ex. 5 - Come up with a regular expression that matches time-of-day strings (such as 9:14 am or 11:20 pm).

- Ex. 6 - Write a function that can validate email addresses: a valid email address contains at least one dot, one (and only one!) at-symbol. It should not contain other punctuation symbols and it should end in a common extension like ".com", ".net" or ".org". Again, use regular expressions where possible! 
