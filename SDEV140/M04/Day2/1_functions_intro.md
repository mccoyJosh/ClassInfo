# Function Intro


So, we have made quite a bit of code up to this point,
but, it has all just been written out in the file without worries as to
where what code is written!

THIS ENDS NOW (hopefully) because we are talking about functions (aka, methods when they are in a class/object)



-----------------

# FUNCTIONS


In very general terms, the purpose of functions is to allow us as developers
to write specific scripts which can be later utilized in whatever code we are writing

Essentially, we can split up our code in a more simplified and reusable fashion


GENERAL FUNCTION:
```
def <function_name>(<parameter_1>, ..., <parameter_n>):
    <body>
```

The way a function works is by first defining the
action or process it does, then calling it where we need to use it
To call a function is easy, it looks like this:
```
<function_name>(<parameter(s)>)
```


-------

# Why use functions?

- A function is just a chunk of code which can be called (and thus ran)
- Once a function is made, it can be called anywhere in ones code, including in other functions
- Functions get data via parameters passed into them. When a function is called, the parameters are evaluated before they are 'copied' into the variables in the function
- Functions can return values (which can be done using the return keyword). It may return at one or more

It is entirely possible to code any program without using functions
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

# Abstraction (which improves readablity)

The point of a function is to simplify or hide code.

***Abstraction*** is a simplified view of a task or data structure
that ignores complex data.

Functions gives us the ability to abstract our code.
We can hide specific functionalities within functions, which, abstracts it.
Once we properly create a function, we can call it without worry about
the implementation of it everytime, just getting the result we'd expect from it.




# Division of Labor i.e. *Modular Development*

Ideally, functions should split up the work of the program into
single coherent tasks.

But how should we go about splitting up the work?


# Avoid writing redundant code


### WE CAN SEE ALL THESE ASPECTS IN THIS EXAMPLE HERE:


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


-------



Now we have seen the use of functions before. The print statement is literally a function!
But, let us quickly make our own:

Let's say we need some code that squares a given number for us
Making a square function would look like this:

```python
def square(x):
    return x * x
```

And calling this square function (and printing out the result)
would look like this:

```python
def square(x):
    return x * x


print(square(5))
```
Now let's take a look at specifically what is happening here.
First off, the method starts off with the def keyword;
this tells python that the next is going to be a method name

The method name in this case is 'square'. From here on out,
you are able to call this function and expect the result defined within.




DO NOT try to call the function on the lines before it is called!
It won't work! Python doesn't know the function exists (yet).
```python
# This bad

y()
def y():
    print('s')
```

```python
# This good
def y():
    print('s')


y()

```




Moving on from the function names, we have the contents within the
parentheses: the parameters.
The purpose of a parameter is to require
the caller of the function to provide a value
that the method can use.
In this case, the square method needs a number to square
There is no predefined value so the function will ERROR
if no parameter is given.


This code, for instance, would not work
No parameter is provided to square, so it will not work

```python
def square(x):
    return x * x


square()
```


This does work :)

```python
def square(x):
    return x * x


square(10)
```

This does not work either, as two parameters was provided

```python
def square(x):
    return x * x


square(10, 10)
```




Following the parameters is colon, and everything tabbed over
is considered inside the scope of the method (just like an if, for, while...)

```python
def square(x):
    return x * x
```


Now within the scope of the method, there CAN BE a return statement
The return statement not only tells the method to stop and go back from whence it came,
but it also is used to returns a value, as we are doing here


If we are to call the method, we can see the return statement in action

```python
def square(x):
    return x * x

val = square(10)
print(val)

```
We see that 'val' takes on the value that the square method returns


---------


You are not limited to only one return statement in a method either!
Some situations may require you to have multiple exits from a method, for instance, this:

```python
def absolute_value(x):
    if x < 0:
        return x * -1
    return x

```
You can also make methods which return different types, but, in nearly every circumstance, you won't
want to do this. Typically, a method should have an expected output, and having a method have an inconsistent
type can make it more confusing for developers

```python
def absolute_value_but_bad(x):
    if x < 0:
        return "It is a negative number"
    return x
```

Some methods have no return statements as well

```python
def determine_if_even(val):
    if val % 2 == 0:
        print('The value is even')
    else:
        print('The value is odd')

print(determine_if_even(5))
```

By default, if no return value is provided, python will have the method return nothing, as in
the nothing type, None

When you have no return statement, it will return on the last line of the function
So, for instance, this method is equivalent to the one before

```python
def determine_if_even_return(val):
    if val % 2 == 0:
        print('The value is even')
    else:
        print('The value is odd')
    return

```









### BOOLEAN FUNCTIONS
Some methods only return boolean values
These methods are referred to as boolean functions
here is one for example:

```python
def odd(x):
    if x % 2 == 1:
        return True
    else:
        return False

```



# MAIN FUNCTION

In lots of other languages, it is necessary to define a method called main to start the code
Here is java for example:


```java
public class Example{
    public static void main(String[] args) {
        System.out.println("");
    }
}
```


This serves as the entry point into a program and tells java where to begin running the code
This not necessarily the case for python, as python code will work without defining a main method


But it is highly recommended to make a main method! You want to do it like this:

```python
def main():
    print("do whatever you need to do")


if __name__ == "__main__":
    main()
```

What is happening here is it first creates the main method, and then calls the main method at the end
If it wasn't called, the code will not run

Making a main method has a few benefits:
First off, as long as you call the main method at the end of your code,
you can organize your methods in whatever order you'd like.
This works because main method is called at the end of the code which means
all the code in the file should have been declared by that point.


Here is an example:

```python
def main():
    number = float(input("Enter a number: "))
    result = square(number)
    print('The square of', number, 'is', result)


def square(number):
    return number * number


if __name__ == '__main__':
    main()
```


The reason we have __name__ == "__main__" is because
python will ascribe a value to __name__ when python code is run
and that name will be __main__ if the code begins in that file

This prevents main methods which may exist in other imported files from
being run. For instance, if someone wanted to use the code from
THIS file, the main method won't be run because this file will
be imported, so the __name__ won't be __main__




-------------

# Importing and Exporting Functions


Now, python would be very annoying if we had to contain
All of our information in one file

But, we can split it up into many files
One way to do this is through importing and exporting methods

All this really refers to is the ability to use a method
that was created in another file


I believe we may have already utilized this as well!
Think of the math library for example:

```python
import math

print(math.factorial(10))

```

What is happening is that there is some standard python file named
math which contains the code to execute the functionality of these
functions which we are importing. So, despite these being defined
elsewhere, we can run their code

To import and export, the first step is to make the file
You want to have the methods you want exported in
Then, define your methods!
For example, take a look at the my_math.py file!
It is just a normal python file with some functions

Now, to import it, just use its name and put import before it:

```python
import my_math

print(my_math.add_one(10))
```



This code can be seen in the assets/example_1.py file.
This works because the file is in the same directory as

It is quite literally that easy :)






Now, when it gets a bit difficult is
when the file may not be in the same folder as the
one you are in!

For instance, if you were in the example.py file
Which is one directory out from the directory with my_math.py
You need to specifically tell python the path to the file


```python

import assets.my_math as mm

print(mm.add_one(10))

```



Also, you can tell python to import ... as X so that you can use
the name provided (X) as where you call the methods you want.
This saves time as you don't need to write assets.my_math everytime!



# Hierarchical Function Calls aka Nested Function Calls

So, we have seen this before, but we have not ascribed a name to
it.

Sometimes, you need to use two different function calls at the same time
to accomplish something.

When we use two function calls together, we nest one of them into the other one, 
creating a "NESTED FUNCTION" which is a "FUNCTION HIERARCHY"

We have seen this plenty of times with casting functions.

For example:

```python
val = int(input("Please type in a number: "))

print("Result of that number times 2: ", val * 2)
```

Here, we see the int() function nest the input() function!

