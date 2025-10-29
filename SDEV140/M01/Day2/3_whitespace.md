# Whitespace

When programming, it is going to be very apparent that whitespace, that is, the "space"
characters we use between pieces of text, is VERY important.

Whitespace is used by nearly EVERY programming langauge to separate tokens.
Tokens are the words and symbols we use to describe our code.

For instance:

print("Hello World")

This is (maybe) broken down into the tokens:

`print`

`(`

`"Hello World"`

`)`

With mapping all of these tokens out, the computer can determine what we are trying to tell it.

BUT, if we use whitespaces incorrectly to break up these tokens, it can either break the program entirely,
or do something that we would not expect.

For instance, in the last example, instead of

`print`

maybe we wrote

pr int

The computer may interpret this as two tokens now:

`pr`

`int`

It will now not know you are trying to print, and this will break.


# == / = Operators

We will get into operators in just a moment, but one such operator is

==

another operator is 

=


If we put a space between the two spaces of the first operator, all of a sudden we have two of the second operator, which
is presumably not what we want.


# Ugly Code

If we use unnecessary whitespace, it can also just make our code look ugly, even though it can still run...
for
instance:

```python
print                  (       "Hey dude"             )
```

Like this works, but is completely unnecessary.

We will talk more about common coding etiquette next week!


# JUST BE AWARE OF WHITESPACES AS WE MOVE ON!