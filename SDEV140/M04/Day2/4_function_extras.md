# Extra Function Info

# Small functions:

You can create a function, if it is small, using a single line:

```python
def add(x, y): return x + y

def mul(x, y): return x * y
```

----

# Function Stubs

When we write code, it is often incremental, and we therefore
are doing **incremental development**.

This means we are not completing all the parts of
our code as we plan it out.

For instance, let's say we are making a calculator and one part needs tp
find the greatest common denominator between two numbers; we may 
want to PLAN to create a function to do this action, but don't want to invest the
time to go and make the whole thing.

Instead, we can just temporarily make a function stub where
we name the function, but only put "pass" inside it as we continue working
on everything else.

Normally, without any content in our function, it would NOT WORK and 
error out. Adding pass as the content avoids this.

Here is an example of the code for the thing discussed:

```python

def greatest_common_denominator(num1, num2):
    pass


```


----

# Parameter Definitions:

We have talked about providing default values to parameters before.
The proper name for said variables are **_optional arguement_** (or **_default arguments_** or **_keyword arguments_**).

The values which don't have default values are considered **_required arguments_**, since you NEED to give them a value, otherwise the function won't run

Here is an example:
```python
def f(x, y, z = 10):
    return x + y + z
```

Now, a rule which needs to be made clear is that the **_required arguments_** 
MUST come before the **_optional arguments_** in the method header, otherwise the method will not work.
We will see why exactly that is in a bit, but here is an example of what you CANNOT DO:
```python
def f(x, z = 10, y):
    return x + y + z
```


# Using parameters where you would like:

We have talked about functions and parameters and providing default values,
but we have not talked about how calling a function can be a bit wacky.


Let's say we have this code (the summation method we have used before):

```python
def summation(lower, upper, step = 1):
    result = 0
    while lower <= upper:
        result += lower
        lower += step
    return result
```

Now, obviously you know that you don't necessarily NEED to add the step value, since it
has a default value.

For example, this is valid code:
```
summation(1, 20)
```

But, what you can also do is call the parameters in a custom way!

The way you do this is by writing out the name of the parameter you want
to assign. In this case, we want to assign lower, upper and step, so we just use their names in the parameter area
of the method call!

```python
def summation(lower, upper, step = 1):
    result = 0
    while lower <= upper:
        result += lower
        lower += step
    return result

print(summation(lower = 0, upper = 20, step = 2)) # HERE
```

What we have worked with up to this point is what is referred to as a **positional argument** (the parameter argument
is based off of its position in the method call). 

What we are seeing here is a **keyword argument**, a parameter which we provide a keyword to explictly say which
parameter we are referring to.


Now what we have done is nothing crazy. It accomplishes exactly what we had done before but with more work,
so why would we want to do this>. Well, with the parameters written out this way, we can go about rearranging them
however we please

Maybe we want the first parameter to be step, that is possible
```
print(summation(step = 2, lower = 0, upper = 20))
```


Maybe we wanted to switch the places of upper and lower, that is also possible
```
print(summation(upper = 20, lower = 20))
```

What this allows us to do is to use the parameters functions in whatever way seems most logical to us.

----

Now, we are not forced into using only named parameters when one is explicitly named, for instance, this is allowed:

```python
def summation(lower, upper, step = 1):
    result = 0
    while lower <= upper:
        result += lower
        lower += step
    return result

print(summation(0, 20, step = 2)) 

# And this is allowed
print(summation(0, upper = 20, step = 2)) 

# And this is allowed
print(summation(0, step = 2, upper = 20)) 

```

---


### THIS IS NOT ALLOWED THOUGH!!!!
```python
def summation(lower, upper, step = 1):
    result = 0
    while lower <= upper:
        result += lower
        lower += step
    return result


print(summation(step = 2, 0, lower = 20))

```

You can't have any of the explicitly defined parameters before the ones determined by index

---

This also allows us to use only the default parameters we'd like.
For instance, if we added another parameter to summation to decide where to start our count off at 
(currently it starts at 0), it would look like this:

```python
def summation(lower, upper, step = 1, initial_value = 0):
    while lower <= upper:
        initial_value += lower
        lower += step
    return initial_value

# we can do this, like we have already shown
print(summation(lower = 0, upper = 20, step = 2, initial_value=10))


# BUT, if you maybe don't want to change step at all, you can just, not use it now.
print(summation(lower = 0, upper = 20, initial_value=10))


# And as we discussed, we don't need to even explicable define parameters as 
# long as they do appear where they would normally, so our method call can actually get smaller!
print(summation(0, 20, initial_value=10))

# Now, it will use the default value for step, but use our value for initial_value!

```

### THIS IS PARTIALLY WHAT WE'VE BEEN DOING WITH THE PRINT() METHOD UP TO THIS POINT

The print method header actually looks like this:
```
def print(*values: object, sep: str | None = " ", end: str | None = "\n", file: SupportsWrite[str] | None = None, flush: Literal[False] = False) ):
```

Most of the header contains parameters with default values.
So, whenever we have wanted to change the ending of the print to be something instead of the newline character,
it is because we are just explicitly telling python I want the end parameter to be whatever:

```python
print('Dog', end='not a new line')
```



### What about the * parameters! What does that mean!

This addition to a parameter means we can have a potentially infinite number of arguments
for said parameter and the function will take these as a list:

```python
def receives_many_arguments(*args):
    print(f"Received {len(args)} arguments")
    for item in args:
        print(item, end=' ')
    print()
    print('------------')

receives_many_arguments(1,2,3,4,5)

receives_many_arguments(1,2)
```

This is what the print function does, along with functions 
like **RANGE** (taps nose to indicate this is IMPORTANT).


This is why strings can take a potentially infinite number of arguments
```python
print('a', 'b', 'c')

print('one string')
```


