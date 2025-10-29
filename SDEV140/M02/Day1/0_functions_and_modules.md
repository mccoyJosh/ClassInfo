# Functions:

-------

## General Functions:

We have Covered Print and Input Already, so, maybe just explain how they are functions as examples and move on.

Mostly focus on combining casting with input!

### Print

we have already seen a few functions up to this point
the print function is one example and a good place to start

```python
print("HEY")
```

From it we can notice a common thread throughout many functions:
its structure, that being, usually a word followed by ()

```python
print()
```

we can also see with print the idea of a parameter, that being the "thing" we give to it
in the case of print(), the parameter is the items we give it between its () (parenthesis)


```python
print("parameters :/")
```

### Input

Another very important function is input()
This gives us the ability to ask the user of our program for some information

Input is going to be out first example of a function that "returns" something
In its case, it returns a string of whatever the user typed

In this example, we capture that returning value in the variable 'name'
and use it to print out
```python
name = input("Hey, please type in your name: ")
print('Your name is "' + name + '"')

```

### Casting

Sometimes we need to get things other than strings from the user though,
in that case, we still use the input() method, BUT, we need to convert the values to our
needed format.

SO WE USING CASTING! int() and float(), for instance

(These are also functions btw)
```python
age = int(input("Hey, please type in your age: "))
print('If you were 10 years older, you would be: ', (age + 10))
```
If we did not convert the string to an integer, this would result in an error!


## Len (and Count Method)

There are more helpful functions that help show some returning values along with parameters
```python
len("dog") # returns an integer of the length of the string
'hhhh dog'.count('h') # returns an integer of the number of h's that appear in the string, BUT THIS IS TECHNICALLY A METHOD!!
```

------


# Math Module

## FIRST OFF, WHAT IS A MODULE???

```python
import math

print(math.floor(1.5))

print(math.ceil(1.5))

print(math.gcd(75474, 3432))

print(math.fabs(-609))
```


---------------

# Random Values




-------

# Pass

Sometimes, you don't want to do anything with your code
maybe there's a section of code you want to wait to do but need something
in the loop to run the code, or actually don't want to do anything in a section of code:
THEN USE, pass

```python
x = int(input('Enter a number: '))

if x == 0:
    pass  # does nothing
```

Now, you can work on the rest of the code and come back to this if statement
