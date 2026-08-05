# Constants

# What are constants?

Constants, in a general sense, are values which do not change and are constant, obviously.
In terms of coding, this refers to values which do not change, which makes sense.

# Using them in the most basic sense: MAGIC NUMBER

Magic Numbers are simply constants which are "put" in a piece of code without any context by not being
tied to a variable.

If we look at a simple formula, for instance, calculating the circumference, we can see this in action:

### C = 2 * π * r

That being the circumference being equal to two times the constant PI times the radius.

We could make a piece of code which takes the RADIUS as input and finds this calculation:

```
input radius
calculate result = 2 * 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986 * radius
output result
```

This works BUT, magic numbers are unclear.
If you are given this piece of code, you can make a pretty good guess that this number is representing 
PI, but you technically can't definitively say. 

This instance of 3.14159... is a magic number.

Another issue with magic numbers is that you can't use it again. If for instance your piece of code 
finds both the circumference and it's area.

A circle's area can be found using

### A  = π * r^2

Again, if we use magic numbers, our code would look like this:

```
input radius

calculate circumference_result = 2 * 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986 * radius
calculate area_result = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986 * radius * radius

output circumference_result
output area_result
```

This is now wasting our time, since we are re-writing the same number twice!

So, magic numbers will
- waste our time rewriting the value
- introduce confusion

# Another example:

```
init_price = input
final_price = init_price * 0.30
output final_price
```

This 0.30 value is completely unknown to us here. Since this it not a mathematical formula.
This is the worst case scenario when seeing a magic number.

--------

# NAMED CONSTANT

Instead of just using _basically_ random numbers, we should ascribe names to these values.
So, we can use VARIABLES to create NAMED CONSTANTS.

We are making variables before, but we are making a rule for ourselves where we do not change the 
value of it so it can CONSTANTly represent a single value.

Thus, it is a constant.


So, we can fix our first program like this:
```
declare constatnt PI = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986

input radius

calculate circumference_result = 2 * PI * radius
calculate area_result = PI * radius * radius

output circumference_result
output area_result
```

We can fix our other program like this:

```
init_price = input
TIP_PERCENTAGE = 0.30
final_price = init_price * TIP_PERCENTAGE
output final_price
```

Now in both programs, we have an easily-referencable name for our constant and
the name describe what it is.

One last thing:
# CONSTANTS are always labeled as all-in-caps

Some programming languages also have built in ways to FORCE you
to make constants not change by making the variable a CONST or CONSTANT type.

C# example from:
https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/constants

```csharp
class Calendar1
{
    public const int Months = 12;
}
```