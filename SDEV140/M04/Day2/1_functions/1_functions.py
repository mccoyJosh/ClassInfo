
# So, we have made quite a bit of code up to this point,
# but, it has all just been written out in the file without worries as to
# where what code is written!

# THIS ENDS NOW (hopefully) because we are talking about functions (aka, methods)

# FUNCTIONS

# Now I know some of you all have already used functions, but we are
# unfortunately only going to be talking about how to make them, and we will get more
# into their specific uses next week

# In very general terms, the purpose of functions is to allow us as developers
# to write specific scripts which can be later utilized in whatever code we are writing

# Essentially, we can split up our code in a more simplified and reusable fashion

"""
GENERAL FUNCTION:

def <function_name>(<parameter_1>, ..., <parameter_n>):
    <body>
"""

# The way a function works is by first defining the
# action or process it does, then calling it where we need to use it
# To call a function is easy, it looks like this:
"""
<function_name>(<parameter(s)>)
"""

# Now we have seen the use of functions before. The print statement is literally a function!
# But, let us quickly make our own:

# Let's say we need some code that squares a given number for us
# Making a square function would look like this:


def square(x):
    return x * x


# And calling this square function (and printing out the result)
# would look like this:
print(square(5))

# Now let's take a look at specifically what is happening here.
# First off, the method starts off with the def keyword;
# this tells python that the next is going to be a method name

# The method name in this case is 'square'. From here on out,
# you are able to call this function and expect the result defined within.
# DO NOT try to call the function on the lines before it is called!
# It won't work! Python doesn't know the function exists (yet).

# This bad
"""
y()
def y():
    print('s')
"""

# This good
def y():
    print('s')


y()


# Moving on from the function names, we have the contents within the
# parentheses: the parameters.
# The purpose of a parameter is to require
# the caller of the function to provide a value
# that the method can use.
# In this case, the square method needs a number to square
# There is no predefined value so the function will ERROR
# if no parameter is given.


# This code, for instance, would not work
# No parameter is provided to square, so it will not work
"""
square() 
"""

# This does work :)
square(10)

# This does not work either, as two parameters was provided
"""
square(10, 10)
"""


# Following the parameters is colon, and everything tabbed over
# is considered inside the scope of the method (just like an if, for, while...)


def square(x):
    return x * x

# Now within the scope of the method, there CAN BE a return statement
# The return statement not only tells the method to stop and go back from whence it came,
# but it also is used to returns a value, as we are doing here


# If we are to call the method, we can see the return statement in action
val = square(10)
print(val)
# We see that 'val' takes on the value that the square method returns


# You are not limited to only one return statement in a method either!
# Some situations may require you to have multiple exits from a method, for instance, this:
def absolute_value(x):
    if x < 0:
        return x * -1
    return x


# You can also make methods which return different types, but, in nearly every circumstance, you won't
# want to do this. Typically, a method should have an expected output, and having a method have an inconsistent
# type can make it more confusing for developers
def absolute_value_but_bad(x):
    if x < 0:
        return "It is a negative number"
    return x


# Some methods have no return statements as well
def determine_if_even(val):
    if val % 2 == 0:
        print('The value is even')
    else:
        print('The value is odd')


# When you have no return statement, it will return on the last line of the function
# So, for instance, this method is equivalent to the one before
def determine_if_even_return(val):
    if val % 2 == 0:
        print('The value is even')
    else:
        print('The value is odd')
    return


# By default, if no return value is provided, python will have the method return nothing, as in
# the nothing type, None
print(determine_if_even(5))


# BOOLEAN FUNCTIONS
# Some methods only return boolean values
# These methods are referred to as boolean functions
# here is one for example:
def odd(x):
    if x % 2 == 1:
        return True
    else:
        return False


# MAIN FUNCTION
# In lots of other languages, it is necessary to define a method called main to start the code
# Here is java for example:
"""
public class Example{
    public static void main(String[] args) {
        System.out.println("")
    }
}
"""
# This serves as the entry point into a program and tells java where to begin running the code
# This not necessarily the case for python, as python code will work without defining a main method


# But it is highly recommended to make a main method! You want to do it like this:

def main():
    print("do whatever you need to do")


if __name__ == "__main__":
    main()

# What is happening here is it first creates the main method, and then calls the main method at the end
# If it wasn't called, the code will not run

# Making a main method has a few benefits:
# First off, as long as you call the main method at the end of your code,
# you can organize your methods in whatever order you'd like.
# This works because main method is called at the end of the code which means
# all the code in the file should have been declared by that point.


# Here is an example from the book
def main():
    number = float(input("Enter a number: "))
    result = square(number)
    print('The square of', number, 'is', result)


def square(number):
    return number * number


if __name__ == '__main__':
    main()

# The reason we have __name__ == "__main__" is because
# python will ascribe a value to __name__ when python code is run
# and that name will be __main__ if the code begins in that file

# This prevents main methods which may exist in other imported files from
# being run. For instance, if someone wanted to use the code from
# THIS file, the main method won't be run because this file will
# be imported, so the __name__ won't be __main__

