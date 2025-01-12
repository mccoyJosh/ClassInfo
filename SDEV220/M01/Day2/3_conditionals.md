# Conditionals

Conditional statements and structures are the most fundamental 
way we make our code make decisions. Every one of these structures
gives us the ability to use boolean values & expressions to do certain 
actions. 

## If Statements

If statements are the simplest form of a conditional statement.

Given a boolean expression, it will run a piece of code if the boolean
expression is equal to True. If it is False, it does not run

```python
# Here is an if statement where the code does run

if 10 == 10: # This is True
    print("Hey, this code runs!")


# Here is piece of code that does not run

val = "Dog"
val2 = "Cat"

if val == val2:
    print("This does not run :(")
```

## Else Statements

Else statements allow us to make alternative routes for when our if statement's
code does not run. Really, it runs if the boolean expression is False, so,
it acts as the foil to the if statement.

```python

boolean_value = False

if boolean_value:
    print("This fails to run")
else:
    print("This DOES print out!")
```

## Elif Statements

Elif statements are the equivalent to else if statements in other languages.
These are essentially additional if statements IF the first one fails. 
We can add a long line of elif statements to check for multiple conditions.

```python
temp = 50

if temp > 75:
    print("HOT")
elif temp < 34:
    print("COLD")
```


There is also nothing preventing us from adding an else statement to the end of this long ling of if/elif statements.

```python
points = 89

if points >= 90:
    print("A")
elif points >= 80:
    print("B")
elif points >= 70:
    print("C")
elif points >= 60:
    print("D")
else:
    print("F")
```


## Switch Statements

If you have multiple explicit values you are checking for,
you can use a switch statement (aka match statement), to run code.

This is equivalent to a long string of if/elif statements, but
this saves on time and makes your code far more readable.

```python
month_value = 9

match month_value:
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
        print("This ain't a month bud :/")

```

## Expressions with 'in' in it

If you have some sort of list and need to check for a value within it, you can use
'in' to do so.

This includes characters in strings!


```python

example_string = "DOG"

print('D' in example_string)

print('C' in example_string)
```