# Loops (reminder)

Whats the big idea with loops!

One of programming's major purposes for us is to do things for us
which would be either annoying or take a long time to do.

This is where loops come in, as they allow us to run the same code over and over again,
however many times we may need it to.

# While Loops

The while loop is the simplest loop. It determines whether it needs to run or not simply based
on a boolean statement.


Here is a set up:

```
while <boolean expression>:
    <code to run>
    ...
```

This code runs forever
```python
while True:
    print("IM RUNNING")
```


This code runs until the character in the string is 's'... determined by the index
```python
string = 'there is a long string here'
index = 0
while string[index] != 's':
    index += 1
```


# For Loops 

For loops are another type of loop which iterates through 
some type of object

Here is generic format for it:
```
for <single-item> in <iterable-object>:
    <code-in-loop>
    ...
```

Here is an example of iterating through an iterable object (a list).
This will go to each number in the list and print it out:
```python
example_list = [1, 5, 90, 12, 800]

for number in example_list:
    print(number)
```


# Nested Loops

Whenever you have a loop within another loop


# Time Complexity (maybe)

- Go through basics of time complexity with a no loop example
  - talk about how it executes how-ever many lines of code there are
- talk about the number of times a loop executes for a small, pre-set list
- assume we don't know the lists length ---> generally, how many times does the loop iterate
- lets say we have a loop inside of a loop; how many times does this execute???

This system of determining the number of lines executed helps us compare how 
efficient code is

- Piece of code with no loops (just hello world)
  - O(1) (constant time)
- Bad searching algorithm which just walks through list looking for item (maybe it is an unsorted list)
  - worst case scenario, it is not inside there,
  - O(n)
- What about finding the sum of a N by N matrix?
  - Adds every item in every n column and every n row
    - This is a loop within a loop
  - O(n^2)
