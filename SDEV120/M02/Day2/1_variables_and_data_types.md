# Variables (briefly)

So, we have already discussed and used variables; although, very briefly, as a reminder, they are 
ascribed names (or alias) for a spot in memory.

So:

```
example = 10
```

In this example, we are putting the value 10 inside of the ascribed place denoted by 'example'.

Now, whenever we reference 'example' it will have the value of 10. If we use example to make a calculation and then REASSIGN
example to the result, then we would be changing the value within that spot in memory.

Using the variable alone in a calculation WILL NOT change the value. Only if we re-assign it.

# Data Types

Within programming, the data we are storing and how we store it are very important problems we deal with on a near daily basis.

Due to computers only technically storing 1's and 0's (binary), we need to be pretty clear to it what types of data
it is working with, otherwise it doesn't know THIS specific set of 0's and 1's is supposed to represent a number
or a letter!

## Numeric

The most basic type which we have DEFINITELY already seen are the numeric ones, that is, 
data that represents numbers.

### Integer

Integers are the simplest. They are non-floating point values, or as the book denotes:
> numeric whole number values without decimal points

These are numbers like 1, 3, 10, -344, 201241.

Pretty basic stuff

### Floating point value

Floating point values are pretty simple as well. They are numbers with decimal point precision.
> numeric values that contain decimal points.

For instance: 4.5, -12415.675, or even 6.0

Even though 6.0 can be expressed as an integer without losing information (i.e. just as 6), 
if we tell the computer that a certain value IS a floating point and IS 6.0 exactly, then that is
how it will be STORED!

-----

## Non-numeric

So, in the book, it ascribes the definition to string as:
> String: "describes data that is nonnumeric."

This though is OVERLY broad, as there are many data types which are not explicit 
numeric values but are not STRINGS, as we will see.

### Booleans

Booleans are a very simple data types. All they describe is values being 'true' or 'false'.
This can be represented with a single bit, as in 0 is false and 1 is true

This is used within decision-making parts of code, for instance, an if statement will use
a boolean value to decide to run the contents of its code, or move on past it.

### Characters

Characters are simply letters and symbols. Anything you type on a keyboard 'really' is a character.
Even things like NUMBERS can be considered characters if the type is a character. This would be different 
of writing numbers to the screen (INTEGERS) and using numbers in calculations (INTEGERS/FLOATING-POINT-VALUES)

### Strings

Strings are simply lists/arrays of characters. Some languages will not have separate types
for characters and strings and just denote any type of character as 'string' (see Python, for instance).

### An potentially infinite number of custom data types


# Actually Storing Specific Data Types Within Variables

Within MANY, MANY programming language you HAVE to provide a new variable you are making with
a data type.

For instance, in both C++ and Java, creating a variable to store an integer looks like this:

```java
int VARIABLE_NAME = 10;
```

First comes the data type (int), then the variable's name (VARIABLE_NAME), then comes an equal sign to denote assignment (=),
and THEN you can actually put the value (10).

Other programming languages will identify the data type automatically without you needing to say what it is:

For instance, in python, you can just do this.
```python
VARIABLE_NAME = 10
```
By seeing that we are using 10, it will auto-detect that the variable itself will need
to be a integer type. This is not a interpreter language exclusive, as we can do that same thing in Golang (which is compiled):
```golang
VARIABLE_NAME := 10
```
Golang very much does give you the ability to manually define these data types though!

THE ENTIRE POINT OF THIS IS THAT the computer needs to know how much space to allocate for this specific data.

The easiest way to see this is with the different types of ways to express whole numbers in java:

## Whole Numbers In Java

In java, we can use a few different data types to express non-floating point values.
The main one, **integer**, has its limits within Java.

Integers in java are 32 bit values, so they can only express numbers in the range of:
-2,147,483,648 to 2,147,483,647
(1 bit is used to determine positive or negative).

For a lot of tasks, this number is fine. Although, there are absolutely situations where you would
need bigger numbers (for instance, the population of earth).

In that case, you could use the **long** data type. This is used to store 64 bit values.
This gives us a range of:
-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
(this is much bigger).

If you tried to store a number in the trillions, you would not be able to use an integer data type
as it would literally not have enough space to store it.

Obviously, there are even bigger numbers than this, so if you are within java and need to store a number larger or smaller than
-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807, you need to use the "BigInteger" data type. This value
is a custom type inside of java which allows us to store whatever size variable we need to.

This is done by using a list of integer values to store certain parts of the LARGER number.


SO, the data type will tell the computer how to interpret the bits. For instance, if we try to 
store a character inside an integer type variable, the computer will try its best, but it will
fail to properly do what you need to do.