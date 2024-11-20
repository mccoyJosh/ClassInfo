# Namespace

--------

First, a definition

### Namespace

> The set of all of a program's variables and their values

Throughout the course, we have talked briefly about how to properly name variables
and what not. To the computer, the names of the variables essentially mean nothing...
the computer technically (sometimes) is going to reassign their names any ways.
The real purpose of properly naming things correctly is for your and every other developer's sake.

What this section is going to do is explicitly define what is what in a piece of code:


Let's take this code for example:

### FILE: doctor.py

```python
replacements = {
    "I":"you",
    "me":"you",
    "my":"your",
    "we":"you",
    "us":"you",
    "mine":"yours"
}


def change_person(sentence):
    """ Replaces first-person pronouns with second-person pronouns. """
    words = sentence.split()
    reply_words = []
    for word in words:
        reply_words.append(replacements.get(word, word))
    return " ".join(reply_words)


```

## MODULE:
> This code is in the file doctor.py, therefore, the **module** is **doctor**.

Depending on where code is found in a module, it changes the name it is referred to as.

#### Module Variables
> In our case, _replacements_ and _change_person_ are our only module variables. These are 
> module variables as they are declared within the scope of the module, that is to say, the most
> outer scope in this file. These variables are given a value immediate when the program is run


#### Parameters
> The only parameter we have here is _sentence_ in the function _changePerson_. The parameter does not receive 
> a value until the function is called.


#### Temporary Variables
> The variables _words_, _replyWords_, and _word_ are the only temporary variables we have in this code.
> They are temporary as they are within the scope of the _change_person_ method. They receive their values 
> as soon as they are introduced into the code (but also only after the method they are in is called)


#### Method Names
> The names we see in this snippet of code are _split_, _append_, _get_, and _join_. These are only able to be called
> since the objects they are ascribed to exist. In our example, there are _string_ objects for the _split_ and _append_ 
> methods to run from, a _dictionary_ for the get method to be called from, and a _list_ for the append method to be 
> called from.


# Scope

Now we have already previously talked about scope:

```python
# All the print statements are within the scope of the example method

def example():
    print("One")
    print("Two")
    print("One")
    print("Two")
    print("One")
    print("Three")
    print('Four')

# This is not within the scope of the example method
val = 1 + 1 

def square(value):
    value = value ** 2
    if value < 0:
        return -1
    return value
```

Scope in python is described by the continuous _'tab level'_ at which you are at. 
In out previous example, the print statements were all tabbed over 1 time, which put them in the same scope.
Despite the square method also being at the same _'tab level'_, they do not share a scope with example since there
is a break in the _'tab level'_, and more specifically, a break which decreases the number of tabs.
In the square method, there is a break in the _'tab level'_ for the content of the if statement, BUT, it increases
the tab level and then return back to the initial _'tab level'_ for the final line ```return value```, which makes it all in the same scope.

Now, we have briefly talked about scope and what variables are available where. But here we are specifically talking about the lifetime of variables:

---------



# Lifetime

The **lifetime** of a variable is the period of time it exists on your computer.
When a variable is created, storage is allocated for it, when it goes out of existence, the storage is reclaimed by
the PVM.

Module variables, those found in the global scope, come to into existence when they are assigned in the program
and are removed when the program is over.

Temporary variables, found inside a function, 
are only around for as long as the function it is found in is still running

---------

We can see that in action here

Despite the variable being made before the method had begun, the x is considered within the module's (or global) scope,
which is accessible from anywhere and 'alive' during the 'f' function
```python
x = 5

def f():
    print(x)
```

An important exception for scope is how temp variables work (the variables made inside a function's scope).
For example:
```python
def f():
    x = 10

f()

print(x)
```

This code will not run.
Since x is being assigned within the scope of the method, 'x' is considered a temp variable for f() and f() alone.
Trying to use it outside the scope of the method will result in an error as it is 'dead'

Even for an example like this:
```python
x = 5

def f():
    x = 10

f()

print(x)
```
Despite x being originally initialized outside the function f(), x within the f() is still assigning a value
to the 'x' within the scope, which then becomes its own object. To help better highlight this, lets look at 
a similar example using list:

```python
x = [1, 2, 3]

def f():
    x = [0, 0, 0]
    x.append(999)

f()

print(x)
```

Here, despite initializing x in the global scope, reassigning a value to x within the f() function has made the
x.append(999) apply to the x list within the function, and not x list found outside the function.

Removing the assigning of x to a new list will make the .append() apply to the x in the modular scope.


```python
x = [1, 2, 3]

def f():
    x.append(999)

f()

print(x)
```


Strangely enough, this code here simply does not work:
```python
x = [1, 2, 3]

def f():
    x.append(999)
    x = [0, 0, 0]

f()

print(x)
```

This is because python will first figure out what the method is doing, and then run it, right. 
So, when it reads the def, it does run the x.append(999), but instead knows hey, there is an x on the
modular scope so this code is fine, then sees the x = [0, 0, 0] and tells itself, alright, for f() we are
going to have a variable be assigned to 'x', and decides that this is going to reference a temp variable for f(). 
NOW, once the code is actually run with the line with only ```f()```, it tries to do x.append(999), but it knows that x 
should only refer to temp variables within the f() function, and it hasn't encountered any, producing an error
explaining that x has no value.
