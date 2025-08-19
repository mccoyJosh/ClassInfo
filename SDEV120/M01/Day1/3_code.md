# Simple Code

# Let's start looking at some basic logic!

In a very general sense, most problems can be outlined like such:

1. INPUT
2. PROCESSING
3. OUTPUT

Even with the recipe example, we can see this:

we input a few ingredients

process them (mixing, cooking, etc.)

output cake

Let us pretend for one moment where we want to write a program
to multiply any given number.
It would look something like this:

```
start
    input myNumber
    myAnswer = myNumber * 2
    output myAnswer
stop
```

This is a piece of psuedocode... we will talk about this in more detail in just a moment.
Simply put though, psuedocode is simple english to show
the steps in which code takes to perform a task.

(See the next 4_psuedocode_intro.md file for the rest of the explanation and formal definition)


## Variable

The word "myNumber" here is our first representation of a "variable" as it
is known in coding. It is very SIMILAR to variable known in mathematics, as in
they represent a value.

In mathematics, the value being represented by a variable is "unknown" and is used to help calculate
whatever we are working with. This is what we are doing here in this problem. Whatever
is inputted is put inside of this "myNumber" variable; this can then be used for whatever we need.

In this case, we just use it to multiply by 2.

In our example above, we represent a number with our variable, but in the world of computers, we
can represent almost anything as a variable, whether that be a word, a sentence, a complex object, or
a simple number.

The variable itself is REALLY just a spot on the computer that is ready to take any value. Because of this,
thr variable is also known as a "reference" to these objects.

### Formal Variable Definition

> _**Variable:**_ a named memory location whose contents can vary or differ over time.

## Input

In all programming languages, there is a way to get input. When first starting off, this is often 
a simple text based input on the command line. Inputs describe any way in which the program gets information.

Most of the time, it is a user giving the program information (like it is in this example here), but it can be other
things like sensors, websites, many, many other things.

User Input can also come through more than just the keyboard; there is the mouse, controlled mic.


## Output

Output is a response given to a user. The simplest output is typically text on a screen, as is assumed by our
little example. These outputs include many, many things, such as any visual representation on our screen, a sound from a 
speaker or headphone, or a vibration from some device that does that. Output is typically how we even know if a 
program is working. If we see no loading bar, or screen change, 
or noise, how would we know if a program or thing is actually running.



# Real Code Example (Python)

Here is this code actually in a real programming language. Don't worry about if 
this is over your head at the moment, but just know it works!

```python
aNumber = input()
aNumber = int(aNumber)
result = aNumber * 2
print(result)
```

