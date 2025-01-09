# Data Types

In python, the way the computer knows how to interact with different
types of values to other types of values, it needs to determine its TYPE.

If you have used python (or any other programming language), you should be familiar with many of these data types



## Booleans

Boolean values are the most simple. There are literally only two possibilities:

```python
True

False
```

Right now, without having discussed conditionals (which we will get to later), there not much
functionally for booleans, and also, typically, we do not just straight up use booleans like this (explicitly writing 'True' or 'False'). Most commonly, they are simply results from boolean expressions, like these:

```python
print(1 == 1)
print(1 < 1)
print(0 != 1)
```






## Integers


These are just numbers without decimal points. Just the whole numbers.
Anytime you need to count stuff up, add whole numbers, represent whole numbers, these are you guys.

These values can also be negative!

```python
1 + 1  # Adding two integers

2 * 3  # Multiplying two integers

912 - 12_12  # Subtracting two numbers (and using _ in integers is OKAY)
```







## Floating Point

These are numbers with decimal values. Anytime you need to describe values with accuracy
in real world scenarios or are doing scientific work requiring floating point values, then\
use floating point values, obviously.

```python
1.0 + 1.2 

0.21212121 * 0.1

2.0 / 3.0

7/2 # These two numbers are NOT floating point values, but this results in a floating point value of 3.5

```









## Characters (and Strings)

Characters are letters and symbols (and numbers). To make one, surround said letter or symbol with single quotes ' or double quotes "

There are some special characters we can describe using a backslash \, for instance, a new line '\n'

These are single characters:

```python

'a'

'?'

'9'

" "

"\n"
```


Strings are simply lists of these characters, so, we begin describing words and sentences using them.
We create them in python the same way we make characters: surround our sentence or word or whatever set of
characters with single or double quotes (' or ")

Here are some strings:

```python
"here is a string"

'here is another string, but this time, using single quotes, which also mean I can use normal "double quotes" in it'

```







------

# Converting between types (*CASTING*)

Sometimes, you need to convert certain values to a different type than what they initially are.

For instance, you may have a integer you need to become a float, or a string
of a number you need to be converted to a integer. 

To do a conversion, you simply call the type you want as a function with the value you want
converted. 

`desired_type(value)`

Here is an example of converting a string of 1 to an integer and then adding it with another integer

```python
print( int('1') + 10 )
```



# How python knows what type a value is?

In other languages, it is explicitly defined, but not here, so what is going on....


Python is known as a **dynamically typed language**. This means that the interpreter itself will determine the type of a value for you.

```python
x = 10 # Python automatically reads the 10 and knows to make x a variable of integer type
```

Other languages, like Java, are know as **statically typed languages**. This is where you have to explicitly tell your computer what type of value you are working with.

For instance:
```java
class main{
    public static void main(String[] args) {
        int x = 10; // We need to explicitly tell the computer that hey, this is in fact an 'int', otherwise it will not work
    }
}
```


