# Loops


# While

let's say you are trying to code something, such as the Fibonacci sequence

```python
value  = 1

print("1st: ", value)
print("2nd: ", value)

value = value + 1
print("3rd: ", value)


#        2      1
value = value + 1
print("4th: ", value)


#        3      2
value = value + 2
print("5th: ", value)
```

This is time-consuming and dumb.
Most importantly, to solve more and more complex problems, you need to write more and more code


Whenever you need to do a process repeatedly, USE A LOOP
The simpliest loop is a while loop

```
while <boolean expression>:
    <statement-1>
    .
    .
    <statement-n>
```


As long as the boolean expression is true, the loop will repeat
THE WAY PYTHON DETERMINES IF SOMETHING IS
"IN THE LOOP (part of the loop body)" IS BY TABS
(ONE TAB OVER FROM LOOP HEADER)
```python
i = 0
while i < 5:
    print(i)
    i = i + 1
```


keep in mind that this WILL NOT print out 5. Once i == 5, it is no longer less than 5, so the loop stops


if we do this:

```python
while True:
    print("Hello World")
```

This will run forever


if we do this:
```python
while False:
    print("Howdy yall")
```

This wouldn't execute at all


Fibonacci Sequence nth Value
```python

t_0 = 0
t_1 = 1
value = t_1

n = 10
n = n - 2
while n > 0:
    n -= 1
    t_0 = t_1
    t_1 = value
    value = t_0 + t_1
print("Val: ", value)

```


------

# For

Let's say, we wanted to print the ascii value for every letter in a string:

does this contain
```python
str = "Bababooey!!!\n"


i = 0
while i < len(str):
    char = str[i]
    print(ord(char))
    i = i + 1
```


This works, but there is an easier way to do this!
Using a for loop

For loop general use:

```
for <item> in <sequence>:
    <statement-1>
    .
    .
    <statement-n>
```

We can simplify the previous example with a for loop
```python
for char in str:
    print(ord(char))
```

For loops will repeat as long as there is another item to go through
```python
example_list = ["One", "Two", "Three"]
for element in example_list:
    print(element)
```
Once it has printed 3, it has gone through all the items in the list and is done


The 'in' key word will make it so that every item in a list can be matched to a variable, even for MORE THAN 1 VALUE
```python
big_example_list = [
("One", 1),
("Two", 2),
("Three", 3)
]
for i1, i2 in big_example_list:
    print(i1, " | ", i2)
```


This can also be seen with the dictionary we talked about before:

```python
ex_dict  = {
 "one":1,
 "two":2,
 "three":3
}

for key, value in ex_dict.items():
 print(key, value)


```


# RANGE FUNCTION
Maybe you need to do a certain task a specific number of times.
That's when you use the for loop with the range keyword!

```
for <variable> in range(<integer>):
    <statement-1>
    .
    .
    <statement-n>

```

Range will create a sequence to a given value, EXCLUSIVE
```python
for i in range(10):
    print(i)
```

So this loop will print 0 to 9

Although, this is still 10 times total, so if you are attempting to do an instruction a certain number of times,
range(#) should work just fine
```python
for i in range(10):
print("Hello World")

```

# EXAMPLE:
Finding exponent
n^x = value

```python
n = 2
x = 10
value = 1

for i in range(x):
    value = value * n

print(n, '^', x, '=', value)
```

The way the range function works is by making a sequence, and the for loop

```python
var = range(5)
print(var[4])

# Note: this isn't a list and attempting to print 'var' out will just give you 'range(0,5)'


print(var)

```

The range function has more functionality!
You can tell the range function to begin at other values instead of 1, INCLUSIVE

```python
for i in range(5, 10):
    print(i)
```


This prints out 5, 6, 7, 8, 9


Off-by-one Error
It is a common error to incorrectly identify when a loop ends, generally by 1 unit
Typically, this happens because loops and specifically the range function works by
being exclusive of the final value
for example:

```python
for count in range(1, 4):
    print(count)
```

folks MAY think this prints out 1, 2, 3, 4, BUT, since 4 is exclusive, it doesn't include it and the count
ends up being off  by 1


Also, by default, the range function goes up 1 value at a time, BUT,
you can change the step value by adding a 3rd parameter
```python
for i in range(0, 10, 2):
    print(i)
```
This can also go backwards! WOW
```python
for i in range(20, 10, -2):
    print(i)
```

#  ENUMERATE FUNCTION
Sometimes, along with going through a list of objects, it is helpful to know the index of said item
The enumerate function will assign an index to all the values in a provided list

```python
example_list = ['x', 'y', 'z']
for i, element in enumerate(example_list):
    print("Index: ", i, " is ", element)

```


# EXAMPLE:
Let's say you need to find the index of something in a list
```python
x = [100, 200, 535, 3235, 652, 232, 535, 21, 535]
# WHERE IS 535
for index, element in enumerate(x):
    if element == 535:
        print("I found 535 at: ", index)
```
We did not need to create an extra variable to store index ourselves
(and also increment it every time we were at an index) since
all that was done for us using enumerate





----


# "In" Keyword

We have already used 'in' before

```python
for num in range(10):  # HERE
    print(num)

```

But it can be utilized in another way!
AS BOOLEAN EXPRESSIONS!
You can check if an item is 'in' most types of sequences

```python
example_list = ["apple", "banana", "cherry"]

# Able to find it in the list
if "banana" in example_list:
    print("I found banana")
else:
    print("No banana :(")


# Does not find it in the list
if "pear" in example_list:
    print("I found pear")
else:
    print("No pear :(")


# Along with the 'not' keyword,
# you can check for something to not be in a given list
if 'pear' not in example_list:
    print("I did not find a pear")


```



----

# Break & Continue


Break and continue are both very important keywords for controlling loops


# CONTINUE KEYWORD
lets say we wanted to do the exact opposite of what we just did, and wanted to print out all the indices which.
DON'T have 535.

We could use the continue keyword to skip the rest of the loop body!
For our instances, this will skip printing out the index for only elements which are 535
and thus leave us only with the values which don;t equal 535
```python
x = [100, 200, 535, 3235, 652, 232, 535, 21, 535]
for index, element in enumerate(x):
    if element == 535:
        continue
    print('Index without 535: ', index)
```

# BREAK KEYWORD
The break statement will stop a loop in its tracks!
Whenever the break statement is found, the said loop will stop and move on to whatever is after that
if we take the code we just had, and perhaps JUST wanted to find the first instance of 535,
 we could add a break statement

```python
x = [100, 200, 535, 3235, 652, 232, 535, 21, 535]
for index, element in enumerate(x):
    if element == 535:
        print("I found 535 at: ", index)
        break
```


it stops the search once we find 535 and doesn't go through the rest of the list



----


# Else


While loops and For loops can both have 'else' statements
The else statement only activates if the for/while loop exits normally
So, for instance, if a loop ends unnaturally from a break, then,
it WON'T execute the else statement
So, if we wanted to be warned that we didn't find 535 in our list, we can add and else statement to our loop
```python
x = [100, 200, 3235, 652, 232, 21, 535]

for index, element in enumerate(x):
    if element == 535:
        print("I found 535 at: ", index)
        break
else:
    print("I did not find 535")
```




-----

Nested Loops


You can put loops in loops; this is considered a nest loop
```python
box_size = 10

# all this does is print out a box of x's
for i in range(box_size):
    for j in range(box_size):
        print('x', end='  ')
    print()
```

Typically, this is done to go through 2-dimensional arrays (matrices)






