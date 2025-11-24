# Exceptions

What are exceptions?

So, up to now, we have been discussing ERRORS, that is, problems which
break our code or can result in an incorrect solution; these NEED to be
fixed before running our code.

There are lesser versions of this where we can have the code actually deal with it.

Technically, these are also bugs and errors in many instances, but we are going to
create code to deal with when these arise.

Now, without anything special, we can create *error-checking code", which is
like an if-statement which checks for a variable being equal to 0 to avoid dividing by 0.

This is fine and good, but this is not exception handling. When an error like this occurs, it will create an exception.

For problems that the program can identify, we can CATCH that exception and act according to it.

THIS is exception handling.

## Handling Exceptions

One common error is when an unexpected input is used.

For instance, in SO many programs, the user is given the ability to type in ANYTHING
when we really want an expected input, like, an integer, or a floating point value, and they can
type "dog".

Here is a simple example:

```python

number = int(input("Please type in a value to add 10 to: "))

print(f"Here is the new value: {number + 10}")
```

In this situation, we need to catch the exception and let the user know this is not
a valid input.

We can do this by using a try/except block. This will run the code like normal, but if an error occurs
in the 'try' block, it will run the except block instead.

In general, it looks like this:

```
try:
    ------- code to run ---------
except:
    ------- just in case code ---------

```

This is basically like an if/else statement that is for running code and catching errors which may exist.

Here is an example of using it in the previous example:
```python
try:
    number = int(input("Please type in a value to add 10 to: "))
    
    print(f"Here is the new value: {number + 10}")
except:
    print("You did not type in a number!")

```

This successfully catches the failing code when you don't type in the correct value!

Now, as is, this is a general catch-all for any exceptions which may arise, although,
this is not always desired or necessary.

Within python, there are a number of exceptions within python:

| Type              | Reason                                                      |
|-------------------|-------------------------------------------------------------|
| EOFError          | input() hits an end-of-file (EOF) without reading any input |
| KeyError          | a dictionary key is not found in the set of keys            |
| ZeroDivisionError | divide by zero                                              |
| ValueError        | invalid value (like, improper casting)                      |
| IndexError        | index is out of bounds for lists/tuples/etc.                |

> Most of these can be seen when they are encountered in code. If not caught, the code typically STOPS and prints out
> this error

When using the try/except block(s), it is best practice to anticipate a specific type of 
error to occur. So, instead of the general catch-all solution from before, it would be wiser to do something like this:

```python
try:
    number = int(input("Please type in a value to add 10 to: "))
    
    print(f"Here is the new value: {number + 10}")
except ValueError:
    print("You did not type in a number!")

```

The whole point here is to catch specific errors and respond to them. For instance here, we want to
inform the user that they did not type in a number when the code fails to convert to an integer, which,
if the code errored out for a different reason, we would not want to just lie to the user!

## Multiple Handlers

Sometimes, a piece of code can contain multiple types of errors and we need to code to catch all
the errors and react differently.

All we need to do it string together the "excepts" after the "try" block.

Generally, it would look like this:

```
try:
    ------- code to run ---------
except ERROR1:
    ------- just in case code for error 1---------
except ERROR2:
    ------- just in case code for error 2---------

```

For a realistic example, here is one from the book:

```python
user_input = ""
while user_input != "q":
    try:
        weight = int(input("Enter weight (in pounds): "))
        height = int(input("Enter height (in inches): "))

        bmi = (float(weight) / float(height * height)) * 703
        print(f"BMI: {bmi}")
        print("(CDC: 18.6-24.9 normal)\n")  # Source www.cdc.gov
    except ValueError:
        print("Could not calculate health info.\n")
    except ZeroDivisionError:
        print("Invalid height entered. Must be > 0.")

    user_input = input('Enter any key ("q" to quit): ')
```



## Raising Exceptions

Sometimes, you need to also create errors.

This is especially true when you begin creating custom types and 
have them interact with each other. You are writing the rules for them.

Thus, you need to actually tell python an error is occurring. This is so that you or anyone
else using your code can catch the error with a try and except block.

We can do this by simple using a line like this:
```
raise <error type>(message)
```

```python
raise ValueError("Invalid height.")
```


Here it is being used within the previous code:

```python
user_input = ""
while user_input != "q":
    try:
        weight = int(input("Enter weight (in pounds): "))
        if weight < 0:
            raise ValueError("Invalid weight.")

        height = int(input("Enter height (in inches): "))
        if height <= 0:
            raise ValueError("Invalid height.")

        bmi = (float(weight) * 703) / (float(height * height))
        print(f"BMI: {bmi}")
        print("(CDC: 18.6-24.9 normal)\n")
        # Source www.cdc.gov

    except ValueError as excpt:
        print(excpt)
        print("Could not calculate health info.\n")

    user_input = input('Enter any key ("q" to quit): ')
```


Also, note the use of *as* here. It is creating an alias for the ValueError being generated.
This gives us access to the message being put inside the error.



## Exceptions With Functions

This is kinda strange why we would want to raise errors in the previous examples, as we
can kinda already see what is being done in all the code present on our screen.

This is why is can be better to see it being used in a function:

```python
def get_weight():
    weight = int(input("Enter weight (in pounds): "))
    if weight < 0:
        raise ValueError("Invalid weight.")
    return weight

def get_height():
    height = int(input("Enter height (in inches): "))
    if height <= 0:
        raise ValueError("Invalid height.")
    return height

user_input = ""
while user_input != "q":
    try:
        weight = get_weight()
        height = get_height()

        bmi = (float(weight) / float(height * height)) * 703
        print(f"BMI: {bmi}")
        print("(CDC: 18.6-24.9 normal)\n")
        # Source www.cdc.gov

    except ValueError as excpt:
        print(excpt)
        print("Could not calculate health info.\n")

    user_input = input('Enter any key ("q" to quit): ')
```

Typically, the code within functions is hidden from us. The only way we know something is error-ing within the function
is if it gives us some kind of message about it. This is where the exceptions come in, as it gives us
the ability to see the thing which is wrong!

## Finally

Another part of the try-except block is the "finally" statement. This is code which will run regardless
of what occurs:

```python
user_input = ""
while user_input != "q":
    try:
        weight = int(input("Enter weight (in pounds): "))
        height = int(input("Enter height (in inches): "))

        bmi = (float(weight) / float(height * height)) * 703
        print(f"BMI: {bmi}")
        print("(CDC: 18.6-24.9 normal)\n")  # Source www.cdc.gov
    except ValueError:
        print("Could not calculate health info.\n")
    except ZeroDivisionError:
        print("Invalid height entered. Must be > 0.")
    finally:
        user_input = input('Enter any key ("q" to quit): ')
    
```


## Custom Exception Types


We can also create errors too!
This is getting into class creation, but know it looks like this, generally:

```python
class Name(Exception):
    def __init__(self, value):
        self.value = value
```


Here is a specific example:

```python
class LessThanZeroError(Exception):
    def __init__(self, value):
        self.value = value

my_num = int(input("Enter number: "))

if my_num < 0:
    raise LessThanZeroError("my_num must be greater than 0")
else:
    print(f"my_num: {my_num}")
```
