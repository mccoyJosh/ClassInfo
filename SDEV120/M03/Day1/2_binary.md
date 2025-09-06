# Binary (BASE 2)

So, the fundamental numbering system for computing logic is the base 2 numbering system.
This is because in the real world, an easy way to story and manipulate data
is by have things be ON and OFF, that is, 1 and 0.

Now since Binary is a base 2 numbering system, this means that there is only 2 digits, that
being 0 and 1.

So, just like in the decimal system, every digit position increments by the base value.
For instance, once we reach TEN, we move from using a single digit to using two digits:
9 -> 10

Each digit is the BASE for a new 10.

Therefore, if we start counting up to 2 in binary, it would look like this:

0     <- 0
1     <- 1
10    <- 2

So, since there is a 2 in the second position, you get one '2'.

If we wanted to represent 3 in binary, we would need a 2 (which we already know how to make),
with a 1, which also know. SO, we can just combine them:

11    <- 3

# Binary Conversion

Now, we can count to 3, but, in a more general sense, how do we convert these values
to decimal values in a more general sense.

So, just like in the base 10 decimal system, we can use each position to represent 10, and
as we move LEFT, each position is multiplied by 10.

So, 520, we know the '5' represent 500 because it is in the third position, so it ACTUALLY represents
5 * 100. The '2' represents 20 because it is in the second position. Thus, we do 2 * 10 (which equals 20).

To know the value of any digit, we can use this formula: 10^(position - 1).

This is the same thing for binary.
The only thing we change is make the 10 a 2, since we are now in base 2.


![binaryToDecimal.png](assets/binaryToDecimal.png)


To get a better idea on doing these conversion, let's do a few more:

BINARY VALUES TO CONVERT TO DECIMAL:

1111

1001

1000 0000 0000 0001

1010 1010


### CONVERTING FROM DECIMAL TO BINARY

![decimalToBinary.png](assets/decimalToBinary.png)


DECIMAL VALUES TO CONVERT TO DECIMAL:

100

81

236



# Binary Math




# Why would we even do this:

So, within computers, we use things called transistors, which we will talk more about later, BUT,
they only have two options, OFF and ON. To store data, we can use a range of these, each one representing a 
0 as OFF and a 1 as ON and THESE allow use to represent EVERYTHING within computing. But, erm, what are these?
