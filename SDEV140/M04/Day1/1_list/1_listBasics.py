# Last week we talked about data structures and how strings are data structures
# today we are going to talk about MORE DATA STRUCTURES
# Specifically, Lists, Tuples, and Dictionaries

# Lists is a sequence of data values; each value is called an item of element
# The items inside a list can be of any type!

# You use lists whenever you need to hold multiple values all in one ordered location

# Here is how you should make a list:
'''
GENERAL LIST:
<list_name> = [<item_1>, <item_2>, ... , <item_n>]
'''
import math

# All a list needs to be created is items seperated by commas
# Here is a list of just integers:
int_list = [1, 2, 3, 4, 5]

# List with strings:
string_list = ['a', 'b', 'c', 'd', 'e']

# List of lists:
list_o_lists = [[1, 2],  [3, 4]]

# Here is a list with nothing:
empty = []

# To access items in the list, it is just like a string: use []
print(string_list[2])  # Prints out c

# You can also print out the entire list with just the print statement!
print(int_list)


# When creating a list, all the items in the list are first initialized and then the list is created
# So:
print([2, math.factorial(7)])
# The list contains the actual value of math.factorial(7) instead of the function


# List types
# Currently, the lists we've seen have been holding only one type of variable
# BUT, lists are not restricted in what they hold.
# They can hold any number of different types of variables
# This is a valid list

type_list = ['dog', 1, 5.0, True]

# You can just do whatever you really want with lists
crazy_list = ['normal item', len([1, 2, 56, 2]), ("a", len("tuple")), 5.76/364, 5]


# Len function
# Just like strings, you can get the length of a list with len()
print(len([1, 2, 3]))


# Operators + and ==
# Just list how you can use the + symbol to combine lists, you can do the same thing with lists
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = list_1 + list_2

print(list_3)

# You can also use the == operators to see if two lists are the same, just like for strings
list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
print(list_1 == list_2)


# Slices of lists
# ALSO, just like strings, you can get a portion of a list using slices
list_1 = [100, 200, 300, 400, 455, 555, 123, "last"]
print(list_1[4:7])


# Iterate through list with for loop and using in keyword to check if variable is inside of list
# ALSO just like a string, you can use the 'in' keyword to iterate through a list with a for loop
# AND check if an item is in a list
list_1 = [100, 200, 300, 400, 455, 555, 123, "last"]
for i in list_1:
    print(i)
print("Is 500 in list_1:", 500 in list_1)


# NOT explicitly string related list stuff
# Converting sequences to list
# So, sometimes, objects that seem like lists are not lists,
# For example, the range function.
print(type(range(10)))

range_list = list(range(10))
print(type(range_list))
print(range_list)


# Sort list (.sort())
# Also, in a ton of circumstances, you want your list to be sorted, and instead of
# creating code to sort is yourself, you can just call the sort function!
example_list = [4, 1, 7, 3, 8, 9, 5, 300, 150, 2]
example_list.sort()
print(example_list)


# MUTABLE
# Lists are mutable! This means the contents of a list can be changed (unlike a string)
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

# We should see the list now contain ['first', 'second', 'third']
print(ex)


# We can also add an entire list of items to a current list of items
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_1.extend(list_2)
print(list_1)

# Now, you wouldn't want to use insert or append here as an attempt to add all the items
# from one list to another, as it would just add the whole list as one item
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_1.append(list_2)
print(list_1)


# Removing Items from list
# Since lists are mutable, that means that it can be changed, which also includes removing items from it
list_1 = [1, 8, 2, 3, 2, 5]

# The first way to remove an item is by calling the remove method
# It will remove the first occurrence of an item
list_1.remove(2)
print(list_1)

# You can also remove items by their index if you use the pop method
list_1.pop(1)
print(list_1)


# Explain how .sort() and .append() and other methods are all mutator methods (don't do thing = thing.mutatorMethod())
'''
Now, as you may have notices, both method we just used didn't reassign a value to another variable
We simply made a list, and called the methods from it; the method then applied the change on the list
For example:
'''
l = [1, 2, 3]
l.append(4)

# This method changes the original object by adding a value to it
# This is considered a MUTATOR method
# All it means is it mutates the object it is being called from to some capacity

# Sort also mutates the object by just calling the method:
l = [90, 32, 1, 64, 2322, 5]
l.sort()
print(l)
# The list is now FOREVER changed to being sorted

# Also note that mutator methods often don't return anything, so trying to print out l.sort() is not super helpful
l = [90, 32, 1, 64, 2322, 5]
print(l.sort())
# It just prints out None



