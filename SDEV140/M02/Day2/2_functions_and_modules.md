# Functions:

-------

# General Functions:

We have Covered Print and Input Already, so, maybe just explain how they are functions as examples and move on.

Mostly focus on combining casting with input!

## Print

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


### Function Call

When we use a function, we refer to this act as "calling" is. So we
are calling the print function in the previous example. 

Think of it as calling a person to do something nearby, like "HEY you, can you grab that for me!"

###  Parameters aka Arguments

we can also see with print the idea of a parameter, that being the "thing" we give to it
in the case of print(), the parameter is the items we give it between its () (parenthesis)


```python
print("parameters :/")
```

Functions which take arguments do so to do some work with them.
Here, the function takes the strings to print to the screen.

In other cases, it may perform some mathematical operation, or many, many other things!

## Input

Another very important function is input()
This gives us the ability to ask the user of our program for some information

### Returns Value

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

# Modules Intro

So far, everything we have done has been baked into python.

Now when you download python, it includes lots of code...
more code than you really need most days.

If you used ALL the code provided to you by python, it would make running code run a lot slower, 
as everything needs to be interpreted and be constantly loaded in the interpreter while running.

Instead of this, we split up the entire code base of python into what is called "**modules**".

Modules are simply files with code on it.


### Check out import assets how to create you own files to import!

- things.py has code which we will import into the other files
- main.py shows the most basic import which gives us access to all the code in a file
- main_2.py shows how we can avoid using "things." before each instance by importing specific variables/things

We will show more of this importing of other files
when we get to functions

### Python itself gives us MANY modules which we can quickly get access to with an import

These are simply python files which came with the programming langauge which are just waiting to be used.

-----

# Math Module

The math module is one of these files.

Instead of holding variables for us to import like in our example, it contains functions which can perform a slew of 
actions for us.


Here are a number of them:

```python
import math

print(math.floor(1.5))

print(math.ceil(1.5))

print(math.gcd(75474, 3432))

print(math.fabs(-609))

print(math.pow(3,2))

print(math.sqrt(64))
```

Along with the functions, there are some variables it gives us access to:

```python
import math

math.e

math.pi
```

This does not even begin to discuss the many, many more things the math module contains,
like sine, cosine, and tangent



---------------

# Random Values

Another super helpful module is the random module.

This module provides... well... randomnesses.

This library has functions to give us the ability to create pseudorandom numbers.

### Pseudorandom-ness

So, computers are very "precise", and a computer which acts randomly is really a cause for concern
as it can't be trusted. Imagine a calculator which could sometimes just be wrong, randomly.

So, when working with random numbers, programming languages can't just magically generate it
and instead has to pull it at least INITIALLY from somewhere.

This beginning number to perhaps create additional random numbers from is called the **seed**.

Even games we play can often rely on seeds or pseudorandom values to function correctly.

The random library utilizes the current time to create this seed, as most of the
time, one cannot predetermine the time at which a program is run
which makes this work most of the time.

### Basic Random Number... random()

The random.random() function creates a floating point value between 0 (inclusive) and 1 (exclsusive).

```python
import random

print(random.random())
```

If we wanted to print a bunch of values randomly under 10, we would run some code
like this:

```python
import random

for i in range(10000000):
    val = random.random()
    print(int(val*10), end=" ")
```

Since 1 is exclusive, it will never actually equal 10 in this instance, just randomly select numbers from 0 to 9

## random.randrange()

We can also just get ranges of numbers more easily with a different function:

```python
import random

print(random.randrange(25))
```

This function is also exclusive, so this last example only prints out numbers between 0 and 24.

This function also allows you to give the starting range of the random values being made:


```python
import random

print(random.randrange(20, 25))
```

Now this will print out numbers ONLY between 20 and 24, so 20, 21, 22, 23 and 24.

## random.randint()

This function is NEARLY identical to the previous function, EXCEPT it is inclusive of both range values.
SO, the number you put will appear:


```python
import random

print(random.randint(20, 24))
```

This also randomly will print 20, 21, 22, 23, and 24


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
