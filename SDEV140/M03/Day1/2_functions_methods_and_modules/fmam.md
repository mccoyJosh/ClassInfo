# Functions, Methods and Modules

--------

(we have talked about modules and functions before)

--------

## Modules
> An independent program component that can contain variables, functions, and classes

## Functions
> A chunk of code that can be treated as a unit and called to perform a task


### Example:

```python
import math     # imports math MODULE


math.sqrt(121)  # uses sqrt FUNCTION from module

print() # print FUNCTION
```

------

## Methods
> Operations that are called by name and run on or associated with objects

-----

## Similarities between methods and functions

- chunks of codes to perform actions
- can take input values as parameters
- can return values

----- 

## KEY DIFFERENCE

Methods NEED an object to apply some work on

Functions work as is

------

# Methods, actually used:

Strings are a good example:

```python
example = "word"

example.upper() # This is the upper METHOD being called on the string object
```

If the object did not exist and contain the information about the 
string, the method would have nothing to work on.

For instance the print() method simply can be called without an object tied to it

Even in this example:
```python
import math     # imports math MODULE


math.sqrt(121)  # uses sqrt FUNCTION from module
```
math is a module and not an object, so when sqrt is "called" from it, it is still acting as a function, not a method

it is not like we tied any values to 'math'.

-----

```
GENERAL FORMAT:
<object>.<method name>(<arg-1>,...,<arg-n>)
```

------

You can also find all the methods for an object using dir()
```python
print(dir(str))
```


--------


# Big Example:

```python
import os

print(f"Working Directory: {os.getcwd()}")

filename = "file.txt"
file = open(filename, "w") # Creates file object
file.write("Hey I am the file just made") # Calls write method on object
file.close() # Calls close method

input("Waiting....")

print(f"File.txt exists: {os.path.exists(filename)}")

input("Waiting again....")

os.remove(filename) # FUNCTION being called from a MODULE

print(f"File.txt exists: {filename}")
```

