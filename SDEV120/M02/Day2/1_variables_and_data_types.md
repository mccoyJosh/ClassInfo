# Variables (briefly)



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

Strings are simply lists/arrays of characters.

### An potentially infinite number of custom data types


# Actually Storing Specific Data Types Within Variables


## For instance, what if it is a LONG value instead of an INTEGER value