# Higher-Order Functions:

There comes a time when you need to apply the same operation to a list of items.

For instance, let's say we have just read a file, and have a list of values which are 
all strings, and we need to convert them to integers.
Now, you can go about this how you have surely done up to this point: making a loop and doing the operation on them.
For the sake of our example, here is what we would normally do:

```python
nums = ['1', '588', '399', '900', '123', '6', '4', '7', '11', '6']

def convert_to_int(num_str):
    return int(num_str)


for i, num in enumerate(nums):
    nums[i] = convert_to_int(num)

print(nums)
```

This works, but, there is a better way!

## HIGHER-ORDER FUNCTION

Now to understand HIGHER ORDER FUNCTIONS, we kinda need to talk about how python treats functions:

# Functions are First-Class Data Objects
Python recognizes functions as first-class data objects. This essentially means that they are treated like variables.
After you run some code defining a function with 'def', it acts as a variable, meaning you can pass it into other
functions as parameters, be returned from other functions, store them in a list or any other data structure, or whatever
else you would want to do.

We can even see it's type by using the type() function on it. ALSO, it has some methods we can call from
it that are built into the function type of object
```python
def f():
    return 10

print(type(f))


print(f.__name__)
```

And this stuff applies to all functions, so if maybe you just want to print out the documentation of
the log function from the math module, you can but getting that variable from it:
```python
import math

print(math.log.__doc__)
```


What this means is that you can use functions in more ways than you may expect:

For instance here, where we place two functions in lists and call the functions as indices from the list
```python
def make_positive(num):
    if num < 0:
        return num * -1
    return num

def make_negative(num):
    return -1 * make_positive(num)

func_list = [make_positive, make_negative]


print(func_list[0](-10))

print(func_list[1](90))
```


Or here where just ascribe it to a variable, essentially making an **_alias_** for it:
```python
def make_positive(num):
    if num < 0:
        return num * -1
    return num

k = make_positive

print(k(-10))
```

----

## Mapping 

With that in mind, we can now get into the first way of using higher-order functions: MAPPING.

Mapping is taking a function and applying it to every value in a sequence, i.e. it MAPS the function to each value.

Mapping can help solve the problem we were dealing with at the start of this discussion:

Here, we can see how we can map the function convert_to_int to the nums list (which removes the need for the loop)
```python
nums = ['1', '588', '399', '900', '123', '6', '4', '7', '11', '6']

def convert_to_int(num_str):
    return int(num_str)

nums = list(map(convert_to_int, nums))

print(nums)
```

What we see happening here is a few things:
- First, we do ```map(convert_to_int, nums)```, which does apply the function to the entire nums list, but 
  doesn't actually change the nums list... it just returns a map object of the changes made
- So, we then convert the map object to a list using list()
- Finally, we reassign the list back to num with nums = ...

This has successfully changed all the values in the list!

Now, there are other uses of higher-order-functions:

## Filtering
Filtering involves taking a list, and 'filtering out' the items that don't fit some criteria.

What this means for us is that we can create a function which returns true or false given an input, and
we can use it to filter out the value which result in false from a list.

For example:
```python
def odd(n):
  return n % 2 == 1

l = [1, 100, 101, 200, 201, 300, 301, 400, 401]

l = list(filter(odd, l))

print(l)
```

Here we are doing a very similar thing as to the map function. We first apply the filter method given the odd function and
l list, and then it returns a filter object, which then needs to be converted to a list,

## Reducing

Reducing involves taking a list of items and applying a single function which takes two values and returns a single value
This is handy for when you need to add all the values of a list together, or combine them in another way. 

Here is an example of reducing a list by addition (adding up the whole list) and multiplication (multiplying every
value together): 

```python
from functools import reduce

def add(x, y): return x + y

def mul(x, y): return x * y

l = [1, 2, 3, 4]

print(reduce(add, l))

print(reduce(mul, l))
```


----


# Using lambda to Create Anonymous Functions

Sometimes going about and creating a whole function to do something as simple as ```def add(x, y): return x + y```
is unnecessary, like, you just need to add two numbers together, and you might not want to make a whole function when you
just need to give it to a reduce method. 

This is where lambda functions come in.

A **lambda** is what is known as an **_anonymous function_**. It has no name, and it created to be used by something like
a map, filter, or reduce type object (or wherever else you may need a small function implemented).
It is not ascribed a name, but it can take parameters and return evaluate a single expression.

```
General Format:
lambda <arg-1>, <arg-2>, ..., <arg-n>: <expression>
```
When an anonymous function is used, its expression is evaluated and then its value is returned.

With a lambda function, we can more properly implement the add and mul reduce statements from before:

```python
from functools import reduce

l = [1, 2, 3, 4]

# Adds the two numbers provided
print(reduce(lambda x, y: x + y, l))

# Multiplies the two numbers provided
print(reduce(lambda x, y: x * y, l))
```

What this means is that we can heavily simplify our summation method discussed Monday:
```python
from functools import reduce

def summation(lower, upper):
    if lower > upper:
        return 0
    return reduce(lambda x, y: x + y, range(lower, upper +  1))

print(summation(0, 10))
```

## Creating Jump Tables

If you have some sort of program which changes needs to perform multiple different fucntions depending on some input,
maybe consider making a jump table where it JUMPS to whatever command you need (using a dictionary), which just
returns the function to be run.

```python

l = list(range(100))

jumpTable = {
  "1": l.reverse,
  "2": lambda : print(l),
  "3": l.sort,
}

def runCommand(command):
    jumpTable[command]()

inp = input("Please enter option: ")

while inp != '0':
  runCommand(inp)
  inp = input("Please enter option: ")
```

