# Troubleshooting


### We just talked about debugging... how is this any different?

> **Troubleshooting**: a systematic process for finding and fixing a problems cause in a system

This definition is nearly identical to the one we just gave for debugging.
Really, the only difference is TECHNICALLY, debugging normally refers
to code, while troubleshooting refers to systems at large.

Along with this, the book defines some extra features about a *proper* 
troubleshooting set of techniques.

OTHERWISE THOUGH, both troubleshooting and debugging are often used interchangeable!

## Troubleshooting: Hypotheses and Tests

Common troubleshooting process:

1. Create a hypothesis (a hypothesis declares a possible cause of a problem)
2. Run a test (do something to validate or invalidate hypothesis declared)

Instead of this, new programmers often:
- make random changes and hope it works
- this one sounds kinda dumb, but ask for help too quickly. Hitting your head against a wall at least for a little hit is helpful in learning
- not make tests/not know how to conduct tests

Without a plan, you are going to frustrate yourself.

Python kinda makes this problem a little easier.

Since python runs line by line, most programs' bugs can be traced to a single line.



## Creating Hypotheses

A hypothesis is a statement which state a clause.

For instance, let's say your computer will not start.

This is our problem:

PROBLEM: Computer will not start

Our hypotheses are statements which state why this might be a cause,
for instance:

- the computer is not plugged in
- it is missing components
- existing components are broken
- the way you are turning it on is incorrect

These all can lead to the computer not starting

These would be hypotheses.

HERE are some NOT hypotheses

- maybe hit it with a baseball bat
- give up
- the sky is blue

All of these don't really answer our problem and every but "the sky is blue" are
action statements, not really causes.


## Logic of Troubleshooting

With existing hypotheses,
we can actually test to see if they are true. Each one of
those hypotheses can be tested; see if the computer is plugged in, see if the components are there.
You can test the statement.

Do be aware that sometimes a test can validate a claim, but a failed test sometimes can 
not invalidate a claim.

The example in the book is like this:

Problem: Light bulb won't turn on
Hypothesis: light bulb is broken
Test: shake light bulb

After this, there can be two options:
1. hear like broken light bits **THIS MEANS IT IS BROKEN**
2. do not hear anything THIS DOES NOT MEAN IT IS NOT BROKEN; MAYBE IT IS BROKEN IN ANOTHER WAY

So, sometimes, a test leads to no result; we must then move on!

## Knowledge

Sometimes, you hit a wall. You can test and test all day long, but the problem may lie in information you
simply do not know.

Like, if your car does not accelerate anymore; maybe you don't know enough about cars to
even being making hypotheses and tests. So, learning knowledge is how you would be begin fixing it.

This is the same thing for programming. 


-----


# Hierarchical Hypotheses

Sometimes, the only thing stopping your program is a single line.

When searching for the problem in your code, you can search for it in chunks.

Maybe you can test to see if one half of your code has the bug vs the other.

Once you know a certain half of the code has the bug, cut that portion in half and test for a bug.

Continuing this process of halving each section until you find the bug will eventually lead you 
to the bug.

This process of cutting a section in half until you find something is known as a **binary search**, which
applies here with searching for bugs, but also is used in searching for values in data structures!

