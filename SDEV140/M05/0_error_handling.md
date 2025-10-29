# Error Handling

We have seen this used before, but I wanted to make sure it was covered
for its own right.

Now, in Python, you will run into exceptions, that is, errors. Maybe the code tried
to convert the word 'dog' to an integer, or you try to access an index outside 
the bounds of a sequence.


```python

str = "dog"

# This:
print(int(str))


# Or this:
print(str[4])
```

In these cases, Python will stop the code. Now, typically, we don't want
our code to stop. Instead, we want to handle the situation (however we may be able to
do that), and make our program continue going.

Now, you may have seen in that last example how Python will tell you exactly what 
exception is occurring when it runs into one. 


For the integer conversion code, we got this:
```
Traceback (most recent call last):
  File "/usr/i/SDEV140/M06/example.py", line 4, in <module>
    print(int(str))
          ^^^^^^^^
ValueError: invalid literal for int() with base 10: 'dog'
```

And for the out-of-bounds code, we got this:
```
Traceback (most recent call last):
  File "/usr/u/SDEV140/M06/example.py", line 4, in <module>
    print(str[4])
          ~~~^^^
IndexError: string index out of range
```


both of these show us exactly the type of error we are encountering, that being 
ValueError and IndexError. Now, with this information, we are able to actually prevent the code
from stopping due to these errors and handle them!


----

# Try/Except Statement

The way Python deals with errors is with blocks of code in try and except statements.
Generally, they look like this:

```
try:
    <statements that might raise an exception>
except <exception type>:
    <statements that handle said exception>
```

The way it is structure is very similar to an if/else statement, as in you can't have
except without a try, and you can't have an else without an if. But, it works differently.

Python will first attempt to run the code within the **try block**, and if an error occurs, it
will jump to the **except** with the name of its given exception. If no error occurs, it 
moves past the entire try/except structure as if it wasn't there.


So, if we wanted to catch the conversion error from earlier, we would do it this way:
```python
str = '3dog'

try:
    print(int(str))
except ValueError:
    print('Hey str needs to an integer!!!')


print('I got to the end!')
```

The line 'I got to the end' gets printed out regardless of it str is a number or not.
Typically we would use this to repeat a loop until a number is an integer...
we talked about this during our input validation discussion. But, here
is an example of this nonetheless.


```python
num = -1

while True:
    try:
        num = int(input('Enter a number: '))
        break
    except ValueError:
        print("Please try again! Tht wasn't a number!!!")


print(f'10 + your number = {num + 10}')
```

The code only ever gets to **break** to end the loop with the input can be converted
to an integer with no error, thus validating it will be a number.


---

# More Exceptions

The try and except statement is not limited to one except (much like an if-elif statement).
If our code could produce a number of different errors, and we need to handle
each error with a unique case, we ca use multiple excepts.

Lets say we were trying to catch both the ValueError and the IndexError.
We would do it this way!

```python
str = "3443"

try:
    print(int(str))
    print(str[4])
except ValueError:
    print("str needs to be an integer")
except IndexError:
    print("str needs to be atleast 5 digits long")
```

----

# All Exceptions

If you don't NEED to do something for every case
of an exception and just need to catch the error regardless, 
you can just use 'Exception' which will catch all types
of errors.

```python
str = "3443"

try:
    print(int(str))
    print(str[4])
except Exception:
    print("Hey fix your code")
```

Technically you can do this as well:

```python
str = "3443"

try:
    print(int(str))
    print(str[4])
except:
    print("Hey fix your code")
```

But this is HIGHLY not recommended. This would catch EVERYTHING, including
KeyBoardInterrupt and SystemExits, so if you had a loop which was not stopping, you could
not do what you may typically do to stop your code, like CTRL+C, as it would catch them.

--- 

# Final... Extra bit of knowledge

Try/Except statements have two more keywords as part of their functionality:

- **else**: This will have code which will only execute if no errors occur
- **finally**: This will have code which will ALWAYS execute, regardless if there was an error present.

They are used just like the exception block.... just use after try/except.

```python

str = "3443l"

try:
    print(int(str))
    print(str[4])
except Exception:
    print("Hey fix your code")
else:
    print("No errors yippee")
finally:
    print('This runs no matter what')
```


