
# Print Statement and Formatting

------

# Printing

## Print Function

As you know, the print statement writes any text/string to the screen
```python
print("Hello")
```

 Print statement will automatically convert non-string values to stirngs (if it can)
Prints out 10 no problem
```python
print(10)
```
Equivalent to:
```python
print(str(10))
```

Even for custom-made objects, python will ATTEMPT to convert it to a string

```python
class example_class1:
    def __init__(self):
        pass


example_class = example_class1()
print(example_class)
```

But if you add a __str__ method to the object, it should use whatever you define within it as the string

```python
class example_class2:
    def __init__(self):
        pass

    def __str__(self):
        return "This is an example class"


example_class = example_class2()
print(str(example_class))
```

 I don't know if you have noticed, but every time you do a print statement, it ends with printing a new line

```python
print('Line 1')
print('Line 2')
```
 Without any text it will just print a new line

```python
print("Line 1")
print()
print("Line 3")
```
But, you have the option to change that! It doesn't have to be a new line
This would print out a new line at the END like normal

```python
print("Whatever you wanted to print out")
```
But to change the END, add another parameter called end

```python
print("Whatever you wanted to print out", end='!')
print("Whatever you wanted to print out", end='')
print("Whatever you wanted to print out", end='<THIS IS THE NEW END>')
```

### EXAMPLE
Common usage of this is if you want to print multiple things out on the same line

```python
for i in range(10):
    print("hey ya", end=' ')
print()

```
If you are making an application where it takes a bit of time to do a process,
but don't want the user to think it's not doing anything, you can add a progress bar

```python
import time
print('Progress: ', end='')
for i in range(10):
    time.sleep(0.5)
    print('.', end='')
    print(' DONE')
```

 If you have multiple things to string together in your print statement, use commas to print em all out
 Adding commas automatically separates each item by a space

```python
first_value = 80
second_value = 120

print("The first values is", first_value, "and the second values is", second_value)
```

Notice how you didn't need to end the string with spaces because the commas adds it itself


 Now, the commas are considered "separators" and the default value that python uses to put in their places is a space
 You can change that though!

```python
print("I", "Have", "Some", "Text", "To", "Print", "!")

print("I", "Have", "Some", "Text", "To", "Print", "!", sep='*')
```

 It can be nothing

```python
print("I", "Have", "Some", "Text", "To", "Print", "!", sep='')
```

OR however long of a string you would like

```python
print("I", "Have", "Some", "Text", "To", "Print", "!", sep='<SPACE>')
```

EXAMPLE

```python
val1 = 10
val2 = 20
val3 = 30
print(val1, val2, val3, sep=' + ', end=' = ')
summation = val1 + val2 + val3
print(summation)

```

---------------

---------------



# Format Strings


In many circumstances, you will need to format your strings so the data being presented can be more easily read
For instance, lets say we were printing out a chart of data
```python
l = [(0, 122), (1, 21), (2, 325), (3, 0), (10, 2444), (11, 223)]

print("| ID | Number of hours |")
for e_id, hours in l:
    print("| ", id, " | ", hours, " |", sep="")
```

When this prints out, it looks bad
Only if there was some way to make the data appear uniform... oh wait there is!
```python
print()
```
F O R M A T T I N G    S T R I N G S
Formatting strings allows us to convert our data to strings for a better formatting experience
General format:

```
<format string> % <data being formatted>
```


and if you have multiple data values, you can do this:


```
<formatting strings> % ( <data-1>, ..., <data-n> )
```

For instance, one common formatting tool is being rounding floating point values
```python
float_val = 10.23525
print('Val: %.2f' % float_val)

```
If we just look through this example formatting string, we can gather a lot of the aspects of a formatting string

first off, the string is essentially a normal string until the % sign. This tells python
that a data will need to be formatted at this place in the string

The last char of the format, which is 'f' in this instance, tells python it will be formatting a floating point value
if we used 's', it would interpret it as a string
if we used 'd', it would interpret is as an integer (it is 'd' instead of 'i' because it represents the word decimal)

Now, since this is an integer, the .2 means that, following the decimal point, we only want 2 values
This will round the number provided to the second decimal value

We end up with the code printing out: Val: 10.24


Now if we change just one character, the 'f' to an 's', we get a very different print statement:
```python
float_val = 10.23525
print('Val: %.2s' % float_val)
```

This prints out Val: 10

With this same value now being interpreted as a string, instead of rounding to the second decimal place
(because strings don't have decimal places), it instead does what a .2 means for a string-type formatting string
What it means is to limit the size of the string to the length of whatever is after the decimal
SO, it limits 10.23525 to its first two characters, 10

This is more easily seen when we just use an actual string for this job
```python
x = 'doggo'
print('Val: %.2s' % x)
```
This prints out Val: do



Another function of a formatting string is to ensure that a string is a minimum number of characters
For instance, if we wanted to print out a bunch of numbers and to make sure the all appear in-line, we can use this
functionality. All you need to do is put a number to represent the length after the %
```python
val1 = 3
for i in range(10):
    print('Val: %6d' % (val1 ** i))

```
To ensure the string is the desired length, python will fill in the other spaces with
just adding a number, it will put these spaces before the item being formatted, but,
you can instruct python to put it AFTER the formatted item with using a - sign
```python
val1 = 3
for i in range(10):
    print('Val: %-6d ||' % (val1 ** i))
```


FOR MORE ON THE SPECIFICS OF FORMAT STRINGS, SEE THIS CHEAT SHEET:
https://learnpython.com/blog/python-string-formatting/


 Now we can fix our chart

```python
print("| ID | Number of hours |")
for e_id, hours in l:
    print("| ", "%2s" % e_id, " | ", "%-15s" % hours, " |", sep="")

```

----------------

## Print Formatting

```python
first_name = "John"
last_name = "Doe"

```


There is a way for the print function to also utilize formatting
This allows us to just place the variable in the string where ever they need to go (given we put them within {}s )

```python
first_name = "John"
last_name = "Doe"
print(f"Name: {first_name} {last_name}")

```
There is another way to use formatting, that being using the format function:

```python
first_name = "John"
last_name = "Doe"
print("Name: {} {}".format(first_name, last_name))
```

Where you place a set of curly braces {}, it is expecting a variable

This comes with the added bonus of being able to reorganize which variables are printed in what order
NORMAL

```python
first_name = "John"
last_name = "Doe"
print("Name: {0} {1}".format(first_name, last_name))
```

REORGANIZED (now prints Name: Doe John)

```python
first_name = "John"
last_name = "Doe"
print("Name: {1} {0}".format(first_name, last_name))
```

We can also use this print formatting to use the format 'code' we were using earlier:

```python
val = 40000/3
print(f'{val:.2f}')


```