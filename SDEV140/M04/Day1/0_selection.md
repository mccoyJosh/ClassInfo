# Selection Statements


## If

THIS IS ONE OF THE MOST IMPORTANT FUNCTIONALITIES OF ANY LANGUAGE

In most code, you need it to diverge.
This can be for various reason, such as
- error handling
- alternative computations
- optional code

To use an if statement, use this format:
```
if <boolean expression>:
    <statement-1>
    .
    .
    <statement-n>
```
Once the code reaches the 'if' statement, it will evaluate
the boolean expression to determine if the statements
within the loop will execute.


If it is true, it runs the code; if false, it does not run that code

# BASIC EXAMPLE

if the number is 1, you get a fun message :)

This will print Hello Person!
```python
number = 1
if number == 1:
    print("Hello Person!")
```

This will not :(
```python
number = 0
if number == 1:
    print("Hello Person!")
```
This is the very basis to making code
If we didn't have some sort of tool to make our code do multiple things, we would only ever be making
very specific programs only able to do one task without the ability to automatically conform to a problem.



# EVEN/ODD EXAMPLE

```python
number = 0
print("Number:", number)

if number % 2 == 0:
    print("This number is even!")

if number % 2 == 1:
    print("This number is odd!")

```

# SCOPE (initial)
all the scope is IS the content of a given coding construct
With the introduction of if statements, we get to our first "scope", that being the contents of the if statement
it is everything tabbed over!
```python
val = 1
if val == 1:
    print("This is within the scope of the if statement")
    print("This is within the scope of the if statement")
    print("This is within the scope of the if statement")
    print("This is within the scope of the if statement")
print("This is NOT within the scope of the if statement")
```
we WILL talk more about this later

# NESTED STATEMENTS

nested statements are simply statements found within the scope of another construct

Here is a simple example
```python
if True:
    if True:
        print("This is true!")
```

# EVEN/ODD EXAMPLE AND DECIDING IF THEY ARE PRIME LESS THAN 10
```python
number = 0
print("Number:", number)

if number % 2 == 0:
    print("This number is even!")
    if number == 2:
        print("This number is a prime!")

if number % 2 == 1:
    print("This number is odd!")
    if number == 3 or number == 5 or number == 7:
        print("This number is a prime!")
```



# SHORTHAND FORM IF STATEMENT!
If you only have 1 statement to run from your 'if' statement
You can put it immediately after your colons
```
if <boolean expression>: <instruction statement>
```

```python
x = 10
if x == 10: print("10 is 10 yay")
```


This can help tidy up your code if you have many short, 1 line if statements


-------

## Intro To Error Handling... kinda

# ERROR HANDLING

When coding, many errors CAN occur and up to now, we could just have to hope that didn't happen
NOW tho, we have if statements, which can be used to stop these errors


# EXAMPLE ERROR
This for example will error our as it tries to convert
```python
number = int("one")
print(number + 1)
```

an if statement could TECHNICALLY prevent this error
we add a check which ensure our value is in fact a number

```python
val = "one"
if val.isnumeric():
    number = int(val)
    print(number + 1)
```

here is a better example

Let's say we are making a calculator to divide two numbers
We want to make sure that we don't cause an error, such as attempting to divide by 0,
so, we can use an if statement for checking if our divisor is 0

```python
dividend = float(input("Please enter dividend: "))
divisor = float(input("Please enter divisor: "))

if divisor == 0:
    print("Cannot divide by 0!")
    exit(0)
print("Result: ", dividend / divisor)
```


-----


## If Else

In some cases, you may want to have a certain action occur if the 'if' statement fails
This is where the else comes in.
The else statement occurs if the 'if' statement's boolean expression fails

```
if <boolean expression>:
    <statement-1>
    .
    .
    <statement-n>
else:
    <statement-1>
    .
    .
    <statement-n>
```


For instance, you could use an else statement for the previous example

```python
dividend = float(input("Please enter dividend: "))
divisor = float(input("Please enter divisor: "))

if divisor == 0:
    print("Cannot divide by 0!")
else:
    print("Result: ", dividend / divisor)
print("Look I'm still running!")
```

This helps simplify the code, and allows for the continuation of the code following the if-else statement



-----

## Elif

SOMETIMES, you need to check more than one thing, which are typically
dependent on the other boolean expressions being used

```
if <boolean expression>:
    <statement-1>
    .
    .
    <statement-n>
elif <boolean expression>:
    <statement-1>
    .
    .
    <statement-n>
else:
    <statement-1>
    .
    .
    <statement-n>
```


For instance, if you were making code to get the letter grade of a student based off
their in-class grade percentage, using a if-elif-else statement would be how you get that done
# EXAMPLE FIND GRADE

```python
grade = float(input("Enter your grade: %"))

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
```



-----

## Match

There are also cases where you may need to see if a variable equals a number of other values
You could use an  if-elif-else statement to determine whether the variable is whatever one of the
values you are checking for, but there is a tool called the match statement which makes checking
variables more readable

```
match <variable>:
    case <pattern-1>:
        <instruction>
        .
        .
    case <pattern-n>:
        <instruction>
    case _:
        <default>
```


Let's say we are trying to determine the month based off of a number. Again,
we could use a long list if elif else statements to connect the number to
it's corresponding month, OR we could use a match statement:

```python
month_num = int(input("Enter the month number: "))

match month_num:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Error: Invalid Month")
```

NOTE: if your version of python is not updated past version 3.9, match statements do not work






------


## Short Circuit



When a boolean expression is being evaluated by python, it will (typically) read it from to right
So, if we had

```python
x = 10
if x > 0 and x <  100 and x % 2 == 0:
    print("This number is good :)")

```

So, in this instance, it will first check if x > 0, THEN do x < 100, and THEN do x % 2 == 0
If x were -1, the x > 0 would result in false, which would result in false for the whole statement
Python is smart enough to know how boolean statements work, and if it figures out the first expression
In an expression containing AND, if the first expression is false, it knows the whole statement is false
SO, it will SHORT CIRCUIT and evaluate the whole expression as false without checking the second expression


For example,
If you were dividing a number by a number (which could potentially be zero), you can avoid an error by doing this:

```python
num = int(input("Enter a number: "))

if num != 0 and 100 / num > 0:
    print("The number is good :)")
```

Since it is first check if num is not zero, in the case that it is zero, the boolean check for 100/num > 0
Is never done which prevents a ZeroDivisionError from occurring
