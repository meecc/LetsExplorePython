
# Excercise - Functional Programming


**Q: ** Try rewriting the code below as a map. It takes a list of real names and replaces them with code names produced using a more robust strategy.


```python
names = ["Aalok", "Chandu", "Roshan", "Prashant", "Saurabh"]

for i in range(len(names)):
    names[i] = hash(names[i])
print(names)
```

    [325562298102183658, 4656825154473833237, 2960754142854623811, 7009005651111438855, 5563618558131281728]


** Ans**: 


```python
secret_names = map(hash, names)
print(secret_names)
```

    <map object at 0x7fafd5760ba8>


#### Write functions to do the follows

- `generate_matrix` which takes two arguments `m` and `n` and a `keyword` argument `default` which specifies the value for each position. It should use a nested list comprehension to generate a list of lists with the given dimensions. If default is provided, each position should have the given value, otherwise the matrix should be populated with zeroes.

- `initcap` that replicates the functionality of the string.title method, except better. Given a string, it should split the string on whitespace, capitalize each element of the resulting list and join them back into a string. Your implementation should use a list comprehension.

- `make_mapping` that takes two lists of equal length and returns a dictionary that maps the values in the first list to the values in the second. The function should also take an optional keyword argument called exclude, which expects a list. Values in the list passed as exclude should be omitted as keys in the resulting dictionary.

- `compress_keys` that takes a dictionary with string keys and returns a new dictionary with the vowels removed from the keys. For instance, the dictionary {"foo": 1, "bar": 2} should be transformed into {"f": 1, "br": 2}. The function should use a list comprehension nested inside a dict comprehension.

- `toUpper` that takes a list of names and returns a set of  with the case normalized to uppercase. For instance, the list ["mayank", "JohrI", "Tagore", "Arjun"] should be transformed into the set {"MAYANK", "JOHRI", "TAGORE", "ARJUN"}.
