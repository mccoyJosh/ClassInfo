# Operators

Most operators do what you would expect for them to do...
so this sections is not to insane (and we have seen a few of them already).

We just need to make sure the ground rules are officially stated:

# Plus (addition) +:

The plus symbol denotes addition of two numbers, just like it always has.
So,

1 + 1 results in 2

# Minus (subtraction) -:

The minus symbol denotes subtraction so 

3 - 2 results in 1


# Division /:

So, for division, we denote it with a forward slash i.e. /

This works as you would expect as in, numbers divide and provide us the result:
6 / 3 = 2


# Multiplication *:

Multiplication works as expected aswell, i.e. it multiplies things.

4 * 5 = 20

# Assignment =:

When working with variables and code, the assignment (=) operator is used 
specifically to denote a value is being placed inside of the memory space of a variable.

So given the example:
```
num = 1 + 2
```

If this line of code executes, we would say that 'num' would be assigned the value of 3.


# Modulus % (remainder)

There is also the often used operator of modulus, which is 'basically' the remainder after
doing a division.

Example:
```
10 % 3  results in 1
```
If you do 10 / 3, you can evenly divide 3 into 10 3 times, which results in 9
The remainder would be 10 - 9, which is 1.


# Make sure you stay aware of the precedence of these operations:

This will work nearly identical to PEMDAS that we have always used, the only main difference
is that the assignment of variables comes AFTER the operations have been carried out.

Now, depending on your programming langauge, the precedence will change a bit, so BE AWARE.

What you can (nearly) always do is use parenthesis () to denote what should occur when, since they have
precedence overriding abilities.

There are also operators built into languages that might not be universal across other programming langauges, like 
exponent. In python, you can use an exponent with simply **, while this typically isn't a built-in operation in other
programming languages. They may also change what these operations are denoted by as well, so do be MINDFUL!

# Another thing to be mindful REALLY is the type of variable you are applying them to

Depending on the data types of your values which are using, these operators may exhibit some interesting behaviors.

Most of the time, if you attempt to use two different data types with an operator, it will straight up give you an error and will not work.

However, in many programming languages, it will often try to convert one of the two values to the same type
and do the operation as one would "expect".

For instance, if you try this in python:

```
value = 10 + true
```

you would probably suspect that it would not work.

However, this actually results in 'value' equaling 11.

This is because python will automatically convert 'true' to 1, as 
0 is used for 'false' and 1 is used for 'true' under the hood of the programming language, 
so rather than letting the code error out, it will automatically do the conversion for you.



Also, if you try something like this:

```
10 / 2
```

You might expect the result to be an even 5, but many programming languages will convert the result
to a floating point value, even if no floating point values were used within the operation.


# NOTE: alot of these things are just to be mindful whenever using a programming language, but
# for the sake of this class, as long as you are clear in what you are doing, there shouldn't 
# be TOO much of a concern!