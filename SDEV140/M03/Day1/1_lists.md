#  Lists

# Basics


Last week we briefly talked about data structures and how strings are data structures
today we are going to talk about MORE DATA STRUCTURES
Specifically, Lists, Tuples, and Dictionaries

Lists are a sequence of data values; each value is called an item or element
The items inside a list can be of any type!

You use lists whenever you need to hold multiple values all in one ordered location

Here is how you should make a list:

GENERAL LIST:

```
<list_name> = [<item_1>, <item_2>, ... , <item_n>]
```



All a list needs to be created is items seperated by commas
Here is a list of just integers:

```python
int_list = [1, 2, 3, 4, 5]
```

List with strings:

```python
string_list = ['a', 'b', 'c', 'd', 'e']
```


List of lists (two-dimensional array):

```python
list_o_lists = [[1, 2],  [3, 4]]

```
Here is a list with nothing:

```python
empty = []
```

To access items in the list, it is just like a string: use []

```python
string_list = ['a', 'b', 'c', 'd', 'e']
print(string_list[2])  # Prints out c

```
You can also print out the entire list with just the print statement!

```python
int_list = [1, 2, 3, 4, 5]
print(int_list)
```

THIS MAY NOT BE SO EASY IN OTHER PROGRAMMING LANGUAGES


When creating a list, all the items in the list are first initialized and then the list is created
So, for instance:

```python
print([2, math.factorial(7)])
```

The list contains the actual value of math.factorial(7) instead of the function


# List types
Currently, the lists we've seen have been holding only one type of variable
BUT, lists are not restricted in what they hold.
They can hold any number of different types of variables
This is a valid list

```python
type_list = ['dog', 1, 5.0, True]
```

You can just do whatever you really want with lists

```python
crazy_list = ['normal item', len([1, 2, 56, 2]), ("a", len("tuple")), 5.76/364, 5]
```

-------

# Indexing

Accessing the items in a list just like a string.

Starting at index 0, each position increments from there.

Using these positions, we can address it using brackets []

So, here is a simple example of getting the first value from a list:

```python
li = ["dog", "cat", "evil creature of the woods"]

first_val = li[0]
```

If we have a list in a list, we address each internal list after each outer list, so here is an example

```python
li = [ [9, 8] , [7, 6]  ]

the_seven = li[1][0]

```


-------


## Len function
Just like strings, you can get the length of a list with len()

```python
print(len([1, 2, 3]))
```

## Operators + and ==
Just list how you can use the + symbol to combine lists, you can do the same thing with 

```python
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = list_1 + list_2

print(list_3)
```

You can also use the == operators to see if two lists are the same, just like for strings

```python
list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
print(list_1 == list_2)
```

## Slices of lists
ALSO, just like strings, you can get a portion of a list using slices

```python
list_1 = [100, 200, 300, 400, 455, 555, 123, "last"]
print(list_1[4:7])
```

## List Loops

Iterate through list with for loop and using in keyword to check if variable is inside of list
ALSO just like a string, you can use the 'in' keyword to iterate through a list with a for loop
AND check if an item is in a list

```python
list_1 = [100, 200, 300, 400, 455, 555, 123, "last"]
for i in list_1:
    print(i)
    print("Is 500 in list_1:", 500 in list_1)
```

## NOT explicitly string related list stuff
Converting sequences to list
So, sometimes, objects that seem like lists are not lists,
For example, the range function.

```python
print(type(range(10)))
```

Doesn't look nice :/

```python
print(range(10))

range_list = list(range(10))
print(type(range_list))
print(range_list)
```

Also works on strings!

```python
print(list("Dog"))
```

## Sort list (.sort())
Also, in a ton of circumstances, you want your list to be sorted, and instead of
creating code to sort is yourself, you can just call the sort function!

```python
example_list = [4, 1, 7, 3, 8, 9, 5, 300, 150, 2]
example_list.sort()
print(example_list)
```


You can sort the letters in a string like this!

```python
letter_list = list("here are a bunch of letters")
letter_list.sort()

print(letter_list)
```

## MUTABLE
Lists are mutable! This means the contents of a list can be changed (unlike a string)

```python
our_list = [44, 55, 66]
our_list[2] = 77
print(our_list)
# Index 2 was changed to 77!


# Since lists are mutable, you can add item to lists
# There are two ways you can go about adding items:
# The append() method and the insert() method
ex = ['first']

# The append method will add a given item to the end (the last index) of the list
ex.append('second')

# The insert method will add an item to the desired index in a list
# FORMAT:    <list name>.insert(<integer of index>, <item>)
ex.insert(2, 'third')

#We should see the list now contain ['first', 'second', 'third']
print(ex)
```

We can also add an entire list of items to a current list of items

```python
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_1.extend(list_2)
print(list_1)
```

Now, you wouldn't want to use insert or append here as an attempt to add all the items
from one list to another, as it would just add the whole list as one item

```python
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_1.append(list_2)
print(list_1)
```

##  Removing Items from list
Since lists are mutable, that means that it can be changed, which also includes removing items from it

```python
list_1 = [1, 8, 2, 3, 2, 5]

```

The first way to remove an item is by calling the remove method
It will remove the first occurrence of an item

```python
list_1 = [1, 8, 2, 3, 2, 5]
list_1.remove(2)
print(list_1)
```

You can also remove items by their index if you use the pop method

```python
list_1 = [1, 8, 2, 3, 2, 5]
list_1.pop(1)
print(list_1)
```


Providing no value to pop will remove the last value of the list by default

```python
list_1 = [1, 8, 2, 3, 2, 5]
list_1.pop()
print(list_1)
```

Explain how .sort() and .append() and other methods are all mutator methods (don't do thing = thing.mutatorMethod())



Now, as you may have notices, both method we just used didn't reassign a value to another variable
We simply made a list, and called the methods from it; the method then applied the change on the list
For example:


```python
l = [1, 2, 3]
l.append(4)
```


This method changes the original object by adding a value to it
This is considered a MUTATOR method
All it means is it mutates the object it is being called from to some capacity

Sort also mutates the object by just calling the method:

```python
l = [90, 32, 1, 64, 2322, 5]
l.sort()
print(l)
```

The list is now FOREVER changed to being sorted

Also note that mutator methods often don't return anything, so trying to print out l.sort() is not super helpful

```python
l = [90, 32, 1, 64, 2322, 5]
print(l.sort())
```

It just prints out None




--------

# Pointers


Hypothetically, let's say we do this:

```python
list_a = ['apple', 'banana', 'cherry']
list_b = list_a
print(list_b)


# list_b has the same values as list_a, as expected
# But, what if we do this:


list_b.pop(2)
print(list_b)


# just as expected, cherry is gone from list_b
# BUT what about list_a


print(list_a)
```


list_a also has removed 'cherry'!
that is because both variables equal the same list!
not only in terms of items, but also the same exact objects

Essentially, python stores the actual list somewhere in the computer
and variable just points to the location of the list
When we set list_b = to list_a, it sets list_b equal to the same pointer as
list_a, so using the methods like pop or append will effect the same list whether you use
list_a or list_b

THIS IS ALSO KNOWN AS ALIASING, as the new variable becomes an alias to the object

to avoid copying the pointer an aliasing altogether,  use the list() function

```python
list_a = ['apple', 'banana', 'cherry']
list_b = list(list_a)
list_a.pop(0)
print(list_b)
```


##  is keyword
To see if two objects are quite literally the same object (instead
of merely having te same numbers), use the is keyword

```python
list_a = ['apple', 'banana', 'cherry']
list_b = list_a
print(list_b is list_a) # will be true
```

```python
list_a = ['apple', 'banana', 'cherry']
list_b = ['apple', 'banana', 'cherry']
print(list_b is list_a) # will be false
```

```python
list_a = ['apple', 'banana', 'cherry']
list_b = list(list_a)
print(list_b is list_a) # will also be false
```


# Sorting List

Lists, as an object, has some built in methods.

One such of these is the SORTING method

### .sort()

This one is an easy one. To call the sort method from a list, we just use .sort()
on it.

```python
li = [1, 9, 0, -6, 10]
li.sort()
print(li)
```


Here we are easily see it sort a list.
This method also is known as a mutator method, in that is changes the object it is called from.

Sometimes, you need a sorted list without changing the list on hand.


### sorted()

This is when we want to use sorted()

When we call sorted, it creates a new list with the items from the given
list but sorted.

```python

li = [1, 9, 0, -6, 10]
new_li = sorted(li)
print(li)

print(new_li)
```


## key argument

Both the sorted and .sort methods have an optional key parameter.
This is just like print() statement's end and sep keyword.

This will apply a function first and then do the sorting


This will not sort the letters like we would expect because some letters are uppercase
and some are lower case.
```python
names =  ["Jeff Will", "bill buff", "alfred Pigman", "Richard reels", "paulo Coelho", "Archer bacht"]

names.sort()

print(names)
```


Instead, we can give the list the str.lower() function to first make the string lowercase
before it does the sorting.

```python
names =  ["Jeff Will", "bill buff", "alfred Pigman", "Richard reels", "paulo Coelho", "Archer bacht"]

names.sort(key=str.lower)

print(names)
```
