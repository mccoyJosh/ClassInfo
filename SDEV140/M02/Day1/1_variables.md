# Variables
assigns a value to a identifiable name
typically in this fashion:
<variable name> = <expression>

example:

```python
variable = 1
```

the word variable can be used here on out to refer to the value of 1
anything you could have done with 1, you can do with variable

# ASSIGNMENT OPERATOR: =

When we make a variable, we utilize the assignment operator to do so.

This creates for us an **assignment statement**.


## TYPES
in other languages, you need to explicitly tell the code what type
of value you are using the variable for


python is smart, as in you only NEED to provide an expression, and it can assume the type of the variable
```python
var_1 = 10
print(type(var_1))

var_2 = "cat"
print(type(var_2))
```

if you know the type of variable you would like, you can tell python what a variable type is going to be:
string_variable: str
this doesn't prevent you to reassigning it to another type, but it cant help make your code readable


## NAMING (creating an **identifier i.e. name**)

When creating variables, there are few REQUIRED rules we must abide by:
- constists of letters (a-z, A-Z), underscores ( _ ), and numbers (0-9)
- needs to start with a letter or underscore
- IS CASE-SENSITIVE (cat is NOT the same variable as Cat)
- cannot be names after reserved words
  - List of those resverved words: https://initialcommit.com/blog/python-reserved-words


Some invalid names would be
- 42case
  - due to starting with number
- the cat
  - due to containing a space
- dog&cat
  - invalid character included (&)
- else
  - reserved keyword

Valid names include:
- abc123
- the_cat_and_dog
- missingName
- WoWeeEe12
- _hello
- Mister1Man2

You should make your variables named properly as to what they do

```python
val_1 = 10
val_2 = 10
val_3 = 10
```

DON'T NAME IT SOMETHING LIKE X
```python
x = val_1 + val_2 + val_3
```

If this variable is holding the sum, name it sum:

```python
sum = val_1 + val_2 + val_3

```

Name the variables based off of its purpose in the code

We will look at a few more ways to name stuff when we get to styling on WEDNESDAY




# How they are Stored


When we create a variable, the computer
will see
- what type of variable it is
- how many of this variable it needs space for

For now, until we get to some data types, we really just need to focus on the first part.

So, if we do ```value = 64```

The computer will recognize it as an integer.

Now, typically, the computer will know integers are 32-bits, and therefore will allocate 32 bits 
for a variable.

The name we give to the variable then becomes a reference to this position this values begins at in memory.

Again, since it knows the type of the value, it would know it only needs to read 32 bits after this initial reference point
to find the value it stored.

In this circumstance, our integer would be restricted to the size of a 32-bit value; if we wanted a larger value, we would need
to upgrade to something like a long value, which would be 64-bit. This is the case for programming languages like JAVA

THESE DAYS, python uses a special type of integer to allow for a variable range of sizes for it's integers, which means
we should not really be worried about hitting the upper limit of these data types. How it works is more complicated than we
really should concern ourselves here today!


# Objects

So, when we create these variables, we are telling the computer we want a certain type of variable,
and it allocates space for it, and we then have reference to that space.

For simple variables, this is about all. Although, we can and will begin creating our own TYPES of variables
in the future, so now is a good time to also begin understanding these TYPES OF VARIABLES as OBJECTS

> **Objects**: an instantiated type of variable

When I say "integer", you know what I am referring to. It is a whole number which can be positive, negative (or 0) and we
can do all sorts of things with, like add and subtract. This is how it is DEFINED. This information is
what the computer KNOWS to do with it.

And, we can find that declaration within the files of python!

Objects are when we make/use/**instantiate** these types.

Like here; this would be instantiating an **integer object**:

```python
number = 10
```

We will discuss object-oriented programming WAY later in this course, but this is the first time we really begin to see variables
be referred to in this manner!



# Garbage Collection

When a variable it no longer being used, the memory it took up previously will
automatically be given back to the system to use for other problems.

In other programming languages, this was something which needed to be done by 
the user manually.

Python, along with some other programming langauges, will detect when values go out of scope, and therefore not being used, and
therefore can be reallocated back to memory!

# Mutable VS Immutable

> Mutable: can change

> Immutable: cannot be changed 

We will see this in action later with lists/dictionaries/tuples/sets next week!





# Incrementing


With the creation of variables, we can use them to do many things.

One of the simplest use cases is "INCREMENTING" and its brother "DECREMENTING"

