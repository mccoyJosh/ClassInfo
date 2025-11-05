# Why use functions?

This was briefly discussed in earlier classes, but
we are going to go more in depth today!

Some of this are reminders, but this is a recap any ways so:

- A function is just a chunk of code which can be called (and thus ran)
- Once a function is made, it can be called anywhere in ones code, including in other functions
- Functions get data via parameters passed into them. When a function is called, the parameters are evaluated before they are 'copied' into the variables in the function
- Functions can return values (which can be done using the return keyword). It may return at one or more

Now, again, it is entirely possible to code any program without using functions
but, it may quickly become extremely complex, hard to understand, and difficult to maintain.


For example, if you do some code which does some process, lets name this process 'x', and
you do 'x' in 3 different places in your code. This 'works', but let's
say you want to add something new to said process, or you figure out there's a bug
in process 'x'. Now, you need to go fix said process in 3 different places, which, is not only
annoying, but, it also can introduce more errors, as you can easily accidentally
not do the same code in all 3 places and now one place is messed up.

This all shows how functions eliminate redundancy. We simply don't need to write
the same code over and over, as we can just create it once and use it.


---

# Abstraction

The point of a function is to simplify or hide code.

***Abstraction*** is a simplified view of a task or data structure
that ignores complex data.

Functions gives us the ability to abstract our code. 
We can hide specific functionalities within functions, which, abstracts it.
Once we properly create a function, we can call it without worry about 
the implementation of it everytime, just getting the result we'd expect from it.

If we look at a summation function, we can see abstraction in action.

```python
def summation(lower, upper):
    result = 0
    while lower <= upper:
        result += lower
        lower += 1
    return result
```

Now, instead of worrying about how exactly one may find the summation
between two numbers, you can be rest assured that this method will do that action
for you!

Since this information was abstracted, the complexity of the code it hidden.
Hiding your code in functions, along with cleaning up your code in general, also
reduces the overall code you as a developer need to look at. 

For example, if we needed to calculate sum of the sum of two 
ranges of numbers WITHOUT using functions, it would look like:

```python
lower_1 = int(input("Please provide first range lower: "))
upper_1 = int(input("Please provide first range upper: "))
lower_2 = int(input("Please provide second range lower: "))
upper_2 = int(input("Please provide second range upper: "))


result_1 = 0
while lower_1 <= upper_1:
    result_1 += lower_1
    lower_1 += 1
    
result_2 = 0
while lower_1 <= upper_1:
    result_1 += lower_1
    lower_1 += 1

print(result_1 + result_2)
```

By just using the summation function, it can be reduced to this:

```python
def summation(lower, upper):
    result = 0
    while lower <= upper:
        result += lower
        lower += 1
    return result

lower_1 = int(input("Please provide first range lower: "))
upper_1 = int(input("Please provide first range upper: "))
lower_2 = int(input("Please provide second range lower: "))
upper_2 = int(input("Please provide second range upper: "))

print(summation(lower_1, upper_1) + summation(lower_2, upper_2))
```

This code is much friendlier to look at and a whole
lot more understandable.



# General Methods

An **algorithm** is a **_general method_** for solving a class of problems. 
The individual problems that make up a class of problems are known as a **_problem instance_**.

In our example code of the summation function, the summation function is a
_general method_ for solving the class of problems which consists of
finding the sum of values between a range. The _problem instances_ in this case
are the pair of numbers specifying the range upper and lower bounds of the summation

Properly designing a function allows it to solve more problems. Typically, 
making a function have more capability comes at the cost of making the function
call more complicated (i.e, adding more arguments/parameters that it needs)

But, if for instance, our summation method currently does its summation
with a step of 1 every time. This limits the use of the summation method, especially
in the circumstance where we may want a step other than 1. So, we can create
more functionality by adding a third parameter called 'step' which allows
the user to define the step function if they so choose.

```python
def summation(lower, upper, step):
    result = 0
    while lower <= upper:
        result += lower
        lower += step
    return result
```

Of course, this now can make calling the method more difficult for users, as they
need to remember to provide a step value, even though they may just want 1 as their step.
There is a way to go around this problem though, so that we can get the benefits
of adding more functionality to our function along with
making it easy to call it in the circumstance where we may not want to have to provide all details:
default parameters.


```python
def summation(lower, upper, step = 1):
    result = 0
    while lower <= upper:
        result += lower
        lower += step
    return result

# Works just fine :)
summation(1, 20)

summation(1, 20, 2)
```

We will get WAY more into default values later, but, here we can see that
by giving step the default value of 1, users can call the summation method
just as they had before (with only the lower and upper range), but if someone
needed to have the function increase at a different step value, they can provide one
without any issue.



# Division of Labor

Ideally, functions should split up the work of the program into 
single coherent tasks. 

But how should we go about splitting up the work?
