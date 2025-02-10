# Testing... In General

Whenever making a program, you want it to work, obviously. Now, what it 
means for something to 'work' means different things to different people and mean
different things for different kinds of projects.

When making a package for others to use, working can simply mean that the 
person using your package has code which does the task explained.

A working website can include things like not being slow, does the actual task
of the website, secures your information while using it, and if it visually makes sense to the user.

With such variability in what is considered "working", there is much

---------------

# Types of Tests


---------------

# Functionality Testing

When you want to simply know if the code runs and returns the correct
response, you are simply trying to test its functionality.

To an ensure a system is working correctly, there are many steps to testing that we want to ensure are all working. 

# Code Coverage

When wanting to know if our system is working, we typically want to ensure all of our code is working.
There are many ways to describe how 'all the code'.

Typically, the way we describe this is by CODE COVERAGE, that is
how much of the code is actually covered. Specifically, we want to a few specific measurements, all
of which are typically given in percentages:

### Function Coverage

Code is typically split up into many different functions.
Making sure all of your functions are tested is essential, so,
this metric is to count the number of functions which are all covered.
The goal is to have all your functions tested.

### Line Coverage

Line coverage is the number of lines in your code which has been tested.
If you create a piece of code with 100 lines of code, and
you executing it in a test only hits 60 of those lines, you
would only have 60% line coverage.

### Branch Coverage

Whenever we encounter something like an if statement, it crates a different branch in 
the programs' execution. 

If we look at this piece of code here:

```python
num = input('Please type in a number')

try:
    num_val = int(num)
    if num_val > 0:
        if num % 2 == 2: # Divisible by 2
            print("YAY")
        else:           # Odd Number
            print('Yeppperz')
        
        if num % 3 == 0: # Divisible by 3
            print('WHAT')
    
except Exception: # Not a number
    print('Not a number')
```

In this example, we can see how we may hit every line with a few tests, but not necessarily every branch.

For instance, we could hit every line with these tests:
- Entering a value which isn't a number
- Entering 6
- Entering 5

This would hit every line, as we have a test with both a number divisible by 2 and 3, and then an odd number.

What these set of tests fails to account for is the PATH where the user enters an odd number
which is divisible by 3. So, this code MAY have a 100% line coverage, but not 100% branch coverage.

### Conditional Coverage

This is a separate metric which is to ensure all boolean expressions have been tested with both
True and False. This helps in getting a high branch coverage.


Now, these are not ALL metrics. There are many, MANY additional metrics that can be tested, but these are very common
ones. There are some which also focus the syntax of the code itself and tries to 
measure how easy a piece of code it written in understanding it.

--------

# WITH ALL OF THESE THINGS TO TEST, HOW DO WE TEST EM??

### Manual Testing

This is the simplest way of testing, and it is how we have been testing
up to this point.

And it is simple. This is just running your program, inputting what you want to test, getting results.

### Unit Testing and intro to automated testing

There is a huge problem with ONLY manually testing your system:

- It is slow

Everytime you add a new feature or change your code a bit, it can be difficult to 
re-test all the previously made functionality, as it takes a lot of time to do so.

This will waste your time the longer you go on manually test your code.

Instead, what we can do is create code to test our code and automate this process of testing.
We refer to these tests as 'Unit Tests' and they allow us to re-run all of our tests very 
quickly so that we can be rest assured all the steps of our system still work. It will be
an initial up front cost of creating the code itself, but, we gain:

- saving ourselves time
- identify bugs more quickly (as a BAD change in a piece of code will fail our tests, so we are alerted at the mistake)
- seeing exactly how our code will be used (in said tests)
- maintain code's usability as we don't want the tests to become unusable as we change the underlying code to something completely different

Typically, when making unit tests, we make tests for functions in our code. There should exist multiple 
unit tests per function which test the basic functions of it, and also test for outliers of what could be implemented.

For instance, if we were making some sort of data structure, we would want to test its insert function
with the normal kind of values we would, along with testing to see what would happen if we tried inserting
outside the bounds of the structure.


### System/End-To-End Testing

If unit testing was testing the individual functionalities of your code, end-to-end testing
would be testing everything for it to function, start to finish. This can include unit test
that build up to include everything start to finish, or more likely,
placing your code in different environments and using it as an end user would.
Obviously, realistic, it is not one or the other but rather more a combination of both.

### Black Box Testing

This simply another term that you should be aware of. This refers to testing a piece
of software without being aware of the underlying workings of. 

This would be done when developing in a group, and another person developed a portion of the project,
and you would black box test as to provide insight as a user of the piece of code would.

----------------

## Other Testing

### Performance Testing

### Stress/Load Testing

### Usability Testing

### Compatibility


---------

# Testing in Python 

- Built in testing

Look to ./example_test_project for example


Run to see results:
```
python -m unittest
```


**Pytest** is a third-party testing package which has a lot more bells and whistles compared to
the built-in testing of python.



# Testing Results in an IDE

Try running your tests in an IDE and see the gui make it look pretty :)

------

## Difficult Things to (Unit) Test

- Games (as they typically allow a player to explore a whole environment... and we can not possibly code for every possible location and configuration in it)
- Code for UI (not impossible though)
- Unorganized code
  - If code it not split up into functions, we don't have anyway to access the individual parts of our code to actually test it
- Pieces of code which are very dependent on some sort of global state, as unit tests would have to re-enact a global state for it to work properly
- Program whose development environment is entirely different than its runtime environment
