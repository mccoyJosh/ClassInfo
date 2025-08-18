# Psuedocode Introduction

With an idea of "what" code looks like,
we can get into what we are doing here in this class,
pseudocode... and with it, learn about
completing some basic logical problems.

# Formal Definition:

> **_Pseudocode:_** an English-like representation of the logical steps it takes to solve a problem.


# Why?

Since this obviously is not interpreted by a computer, what does this benefit us?

- Allows us to plan REAL programs on computers
- Allows us to demonstrate an algorithm without actually writing it to talk and potentially fix it with others (which is kinda another way of planning but whatever)


# First Steps

Let us pretend for just a moment we need to solve a really difficult problem
with a computer:

> Double a given number

Let us make a psuedocode to solve this:

```
start
    input myNumber
    myAnswer = myNumber * 2
    output myAnswer
stop
```

Considering this is the same problem we were "solving" before, it is the same piece of code.
We can now talk about it specifically how it's psuedocode

# Loose Syntax

When writing psuedocode, there is often not going to be an exact or strict syntax to follow.

It is not a real programming language, so you are not going to be forced to make
a computer interpret it, instead you are writing it so a HUMAN can understand.

So psuedocode should be able to be read by humans and make logical sense above all else.

## ALTHOUGH, to maintain some order for the sake of this class, we will make sure we follows some basic rules

# start, stop

When beginning and ending psuedocode, make sure this is indicated with words like 'start' and 'stop';
you can use other words aswell like 'begin' and 'end'.

# input

When taking input, we need a word to indicate such. We can use the word "input", along with "get" or  "read".

You can also indicate that you are getting input in a different syntax than what was initially show:

```
get aNumber
```

is just as valid as something as:

```
aNumber = get
```

# Calculations

Currently, the calculation line is written as:

```
myAnswer = myNumber * 2
```

But these are valid as well:

```
calculate myAnswer = myNumber times 2
```

```
myAnswer is assigned myNumber doubled
```


# output

When outputting, just like "input", we can use many different words to describe "output", like

- display
- print
- write


# A few additional things the book desiress

## indention

The content (code) in your psuedocode needs to be indented compared to the "begin" and "end" of your code.
This helps it be clear what portion of the piece is the code:

```
start
--->input myNumber
--->myAnswer = myNumber * 2
--->output myAnswer
stop
```

## Program statements begin with lowercase letters

## No punctuation is used to end a statement

## Each statement represents 1 action

As we move on, we will see a few more things

## When using functions/modules, follow the name of the module with parentheses "()"

## When writing a function/module, end it with the word 'return'

### THE MAIN THING IS TO BE CONSISTENT

With all of these different ways of writing psuedocode, it is okay to use all of the above, BUT,
if you use different kinds of words for the same thing, it can cause confusion. To avoid this, 
I would pick one way of doing any one of these things and sticking to it (at least withing the same piece of
psuedocode).