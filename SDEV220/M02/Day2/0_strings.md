# Strings (reminder)

Strings are simply  list of characters.
We have been using strings already up to this point.
They are simply characters surrounded by either " or '

Here is an example real quick:

```python
'A string!'
```
We have surely seen this plenty of times!

This is common across all (most) languages, 

# Multiline Strings

You can create multiline strings using either three single or three double quotes instead of a single character.

```python
here_is_a_huge_string = '''
Here
we have

a 

bunch of lines wooo
'''

```


# Converting to strings (using 'str()') and Concatenating Strings (with +)

We have already discussed this, but, if something is not a string type
and we need to convert it to a string, we can convert it using str()

```python
age = 200
message = "I am " + str(age) + " years old"

```
This example also shows off concatenating of a string

# Get Character with [] (LIKE MANY OTHER DATA STRUCTURES)

To get a single character from a string, you can use []'s after the string with the desired index.

This is very similar to many other data structures in python (think list).
This is because strings are 'essentially' data structures, just ones that
only hold characters.

Here, we are printing the letter 'r' from 'word':

```python
example_string = 'word'
print(example_string[2])
```

# Substrings (USING [:])

Using just a single value inside brackets results in 1 character, but using 
2 will get a range of characters.

We can use this to get substrings from strings.

Here, we get the substring 'dog' from the greater string:

```python
big_string = 'I am going to walk my dog today'
print(big_string[22:25])
```


# Functions    

- split()
  - creates list of strings by separating by separator string
  - ```python 
    string = "here,are,some,words"
    string.split(',') # this results in ["here", "are", "some", "words"] 
    ```
- join()   
  - creates a string from a list of strings and separates them by a given character
  - ```python 
    ex_list = ['Here', 'Are', 'Words']
    "!".join(ex_list) # this results in 'Here!Are!Words'
    ```
- replace()
  - replaces a substring with a new substring
  - ```python 
    string = "here,are,some,words"
    string.split(',') # this results in ["here", "are", "some", "words"] 
    ```
- strip()
  - removes whitespace from a string
  - ```python 
    string = 'mean people exist in this mean world'
    string.replace('mean', 'nice') # results in 'nice people exist in this nice world'
    ```
- startswith()
  - determines whether a string begins with a given substring or not
  - ```python 
    string = "here are some words"
    string.startswith('here') # results in True
    ```
- endswith()
  - determines whether a string ends with a given substring or not
  - ```python 
    string = "here are some words"
    string.endswith('words') # results in True
    ```
- upper()
  - makes string uppercase
  - ```python 
    string = "word"
    string.upper() # results in "WORD"
    ```
- lower()
  - makes string lowercase
  - ```python 
    string = "WORd"
    string.lower() # results in "word"
    ```

# Format Strings

There are a few ways to create formatted strings, including using the .format method, but here 
we are simply going to be showing off the f'' string!

Sometimes it is inconvenient to be converting everything to strings
and then append them to whatever you are working with, so
it may be more connivent if there was a way to simply convert your 
other types from within the string to be what you want and where you want:
thats where format strings come in handy!

f strings allow you to place your variables where you want in your string
and do additional formatting in the same place!

```python
name = "josh"
print(f'Here is my name {name}')
```

If you have something like a number, specifically a floating point in our example,
you can apply the many additional 'formattings' to it after the variable name

Here, we are using the formatting string to round up this floating point value's third decimal value:

```python
my_floating_point = 7.65656565656
print(f"Here is the number: {my_floating_point:.3f}")
```



