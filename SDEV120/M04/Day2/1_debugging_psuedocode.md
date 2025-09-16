# So monday, we discussed fixing flowchart problems, but we did not look at psuedocode problems

So, here we are.

Some of these have logical issue; some of these have structure issues.
Let's take a look and see how we should properly be walking through these.


# How to debug

Debugging psuedocode/written code is very similar to fixing flowcharts.

We should simply walk through each step of the code, and hand-do the code.

What we are going to do here though is to be thorough.

> NOW, IN THE UPCOMING ASSIGNMENTS, YOU ARE EXPECTED TO FIND THE BUGS IN
> THE CODE AND FIX THEM AND TURN THEM IN. You do not have to outline EVERYTHING like
> we are doing here. BUT, if you want good practice in doin so, go ahead. When code is difficult,
> you may find yourself doing just this to fix it. IT IS A GOOD SKILL TO HAVE, but you
> probably won't need to do this is debug small problems!

- go step by step
- keep track of all variables
- record results from calculations (for instance, in a boolean expression)

If you get through the entire piece of code, and it works with your expect inputs, then you "SHOULD" be good.

----------

# Basic Debugging Problems


## Example 1

```
// Program to read a file full of numbers and find each
// value squared. As it squares these values, it adds the squared results
// to a total. It stops reading if all the numbers have been read (EOF) or if the total would exceed
// 250 with the next value
//
// Pretend inputs:
// 10 5 5 10 4 3
// We find this code does not work (it should stop at the 4, it stops sooner)
start
    num value
    num squaredValue
    num total = 0
    
    value = read file for input
    
    while not EOF and (total + value) * value <= 250 then
        squaredValue = value * value
        output squaredValue 
        total = total + squaredValue
        
        value = read file for input
    endwhile
    
end
```

If we walk through this problem, we find that it stops too soon.

WALK THROUGH IT

We find there is a logical error in the while loop's conditional.
It should be doing total + (value*value) instead of (total + value) * value. This causing
the program to end sooner than expected.

## Example 2

```
// This program takes grades inputted by a student.
// It will assume all assignments are worth the same weight,
// and each is scored on a basis of 100 points. It will calculate for the student
// minimum grade they need to get an 'A' in the class on the next assignment, if it
// is possible
//
// It should continue accepting inputs until 999 is entered. (This score should not be possible)
//
start
    float runningTotal = 0
    int count = 0
    float currentAverage 
    // Initiall set to 90 (for A) but just as easily be changed to 80, 70, etc.
    float desiredAverage = 90
    float currentScore
    float neededScore
    
    
    output "Please input first grade: "
    input currentScore
    if currentScore is not 999 then
        runningTotal = runningTotal + currentScore 
        count = count + 1
        output "Please input next grade: "
        input currentScore
    endif
    
    currentAverage = runningTotal / count
    output "Current Average is: ", currentAverage
    
    neededScore = (desiredAverage * ( count+ 1 )) - runningTotal
    output "To get a grade of ", desiredAverage, "points, you need to get a ", neededScore, " or greater!" 
end
```

Here, we see that it expects a loop and not an if statement!


## Example 3 

```
// The program will calculate the perimeter of a shape given
// - the number of side
// - the length of each side
// The program works for non-equalateral shapes; that is to say,
// the sides can be different lengths
start
    int numberOfSides
    float currentSideLength
    int sideCount = 0
    float perimeter = 0
    
    output "How many sides on shape: "
    if numOfSides > 3 then
        while sideTotal < numOfSides:
            sideTotal = sideTotal + 1
            output "Length of side ", sideCount, ": "
            input sideLength
            perimeter = perimeter + sideLength
        endwhile
        output "The perimeter is ", perimeterTotal
    else
        output "Invalid shape; should have atleast 3 sides!"
    endif
    
end
```

This example has lots of syntax errors, making it non-functional as the variable names
do not match and a person would HAVE to assume which variable is which.

> We would have to go through and make sure all the variable names are correct!

> This program ALSO fails to run initially as the loop cannot start, nor can the if statement, since we never inputted the first value.


# Example 4 

This problem actually contains a special kind of selection statement called
a cases. In this type of structure we can compare multiple different explicit values
to a variable. This structure is also referred to as a switch statement (both switch and case
are used to represent this)!

```
// This program will represent a module for a
// game which translates a integer into the condition
// it repsents in game. So, perhaps, a 'fight' is occuring,
// and a character is 'poisoned'. We COULD save all the information about
// being POISONED in an object and pass that around, although, every single time
// a thing is POISONED, we would need to transfer all that data all the time,
// and this would be the case for all "conditions", so, instead, we can ascribe a number
// to point to said condition in some sort of dictionary, and then all we need to transfer is
// that number value for each condition. 
//
// In this hypothetical code, we would still need a way to see what condition this is, so, this hypothetical module is doing that
getConditionName condVal
    string name
    
    switch condVal
        case 1
            name = "poisoned"
                endcase
        case 2
            name = "bleeding"
            endcase
        case 3
            name = "sleepy"
                endcase
        case 4
            name = "sad"
            endcase
        case 5
            name = "crazy"
        endcase
    endswitch
return name
```

The problem here is one of indention. 
Although this may be the first time seeing a switch/case structure, one can see
the use of indention on 'endcase' is inconsistent.

We should always be indenting the end'structure_name' at the same level of indention that it starts on.


## Example 5

This has two problems... but we are just going to focus on one for a moment

```
// This program takes an inputs to 
// find a value to the power of another power
start
    int base
    int exponent

    output "Please input your base value: "
    input base
    output "Please input the exponent: " 
    input exponent
    
    if base not does equal 0 then
        int count = 0
        int runningTotal = 1
        while count < exponent:
            runningTotal = runningTotal * base
            count = count + 1
        output "RESULT: ", runningTotal         
    else
        output "RESULT: 0"
    endif
    endwhile
    
end
```


So, the issue here is that the while loop's endwhile is AFTER the endif statement. Since
the start of the while loop is contained within the if statement, the ENTIRE while loop needs to be
inside the if statement. The endwhile MUST be moved to before the else at the very least.

This is not the only problem with this piece of code!

-----------

# Edge Cases

When creating code, we often write it to solve a specific problem we are facing. Although, 
when creating code to do this, we may not think outside the problems we initially had. That is
to say, there may be more acceptable inputs that we failed to imagine initially.

These often outside the normal input values are what are known as **EDGE CASES**.

What can happen is that we make "working" code for our individual instance, BUT, there
exists a special input which breaks our code.

This piece of code above has a few edge cases we failed to initially account for:
- exponent being negative
- technically, exponent being a fraction, but, we are only working with integers, so we will ignore this one for simplicity’s sake

Let's fix this then:


```
// This program takes an inputs to 
// find a value to the power of another power
start
    int base
    int exponent
    bool negative_flag = False

    output "Please input your base value: "
    input base
    output "Please input the exponent: " 
    input exponent
    
    if base not does equal 0 then
        int count = 0
        float runningTotal = 1
        
        if exponent < 0:
            negative_flag = True
            exponent = exponent * -1
        endif
        
        while count < exponent:
            runningTotal = runningTotal * base
            count = count + 1
        endwhile
        
        if negative_flag:
            runningTotal = 1.0 / runningTotal 
        endif
        
        output "RESULT: ", runningTotal         
    else
        output "RESULT: 0"
    endif
    
end
```


# Debugging Tools

They just let you actually walk through real code :)

> pull up pycharm and walk through piece of code if possible

See the debug_python folder.

- Problems with sql database ip
- Problem with sql database result calculation; should be giving the internal array, instead of the whole tuple!


