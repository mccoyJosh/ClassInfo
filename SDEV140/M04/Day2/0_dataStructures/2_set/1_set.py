# The last and final type of data structure we are going to talk about is a set


# Use {} to make a set
# KEEP IN  MIND THAT JUST {} IS ACTUALLY AN EMPTY DICTIONARY
# Really, a set is a dictionary without the associated values and just has keys (unique, unordered values)

example_set = {'apple', 'banana', 'cherry'}

# a set needs all values need to be unique

example_set = {'apple', 'banana', 'cherry', 'cherry'}
print(example_set) # The second cherry is not added


# You can't change items in the set, but you can add and remove from it

example_set.add('lemon')
example_set.add('avocado')
example_set.remove('apple')
print(example_set)

# you may have notices that the items in a set are not the same if ran multiple times
# That is because a set is unordered

# It exists to just hold items and that's about it

# You can get every item in the set with a for loop though:
for element in example_set:
    print(element)


# USES
# The main use of sets is to remove duplicate values, since sets cannot contain duplicates
# Sets in python are very similar to sets in mathematics, so using them
# to represent them as such is very helpful

# See more info here:
# https://python.land/python-data-types/python-set#Why_would_you_need_sets
