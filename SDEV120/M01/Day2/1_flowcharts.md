# Flow Charts

When planning code, psuedocode sometimes does not provide us
a good "visual" to look at, since it is just lines of words.

Flowcharts show the logic of a piece of code with symbols representing each step.
This gives us a nice picture to look at to EASILY visualize the code 
we are trying to understand.

So we are representing the same ideas, but with specific shapes... so let's just get into them!

-----

# input

to denote inputs with a flow chart, we can use a parallelogram.

![input.png](assets/input.png)

as we can see, the same 'code' we would use is still in the shape, 
but the shape helps us easily tell what the purpose of this portion is.

We are going to see this same format (the actual code being contained withing a
specific shape) over and over again!

# calculation

to denote any time of calculation, we use a rectangle

![calculation.png](assets/calculation.png)


# output

to denote output, we use the same shape as input, i.e., a parallelogram

![output.png](assets/output.png)

# decision

to denote a decision being made (for instance, with an if statement), we use a diamond:

![decision.png](assets/decision.png)

# module call

we have not discussed modules yet, but when we do, we will denote them as such:

## internal module call\

![internalModule.png](assets/internalModule.png)

## external module call

![externalModule.png](assets/externalModule.png)

# flowline

Use an arrow to connect these steps and to show the flow

# starting and stopping.

Now, just like psuedocode, we NEED to indicate that our code is starting and stopping.

We do this with a circle (or oval, if you want to be technical)!

Now we don't need to only use the words "start" and "end"...
any words to indicate such is fine, just as long as there are these
two circles denoting these points.

![start-stop.png](assets/start-stop.png)

-----

# Simple Example

Let's put these together and make the previously discussed program into a flow chart.
> input a single value and find and output the value multiplied by 2

![simple_flowchart.png](assets/simple_flowchart.png)

* erm pretend the last red parallelogram said "output" instead of "input"

# REITERATE: INPUT -> CALCULATION -> OUTPUT

# Perhaps make a mistake during one of these and turn around and be all like "erm did you catch that"

# Better example problem:
> Write an algorithm which will calculate the area of a rectangle, given its width and height.

# Another optional example:
> Write an algorithm which, given 2 input numbers, will print out which one is larger between them

# Yet another example problem:
> Write an algorithm to calculate the tax and tip for a meal, then output the tax and tip and the total amount you owe. Assume the tax to be 7% and it is a nice tip of 25% which is calculated to include the tax.
> For example, if you paid 100 dollars for your meal, tax would be 7 dollars and the tip would be 25% of 107 dollars which is 26.75 dollars. Your output would look like the following:

```
Tax:   $7
Tip:   $26.75
Total: $133.75
```

-----

# Where to draw these??

# [draw.io](https://www.drawio.com/)

A good tool for making these flowcharts is draw.io

# A few things to show off

Honestly, this resource is very easy to use, but we will briefly discuss
its basics:

- Get there
    - Either draw.io
    - or go through website and "start using"
- Make shapes
- Change Color
- Add Text
- Represent small piece of code
- Add description
- Save
- Export