# TODO: Look at Equality: Object Identity asd Structural Equivalence in chapter 5

# Hypothetically, let's say we do this:

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

# list_a also has removed 'cherry'!
# that is because both variables equal the same list!
# not only in terms of items, but also the same exact objects

# Essentially, python stores the actual list somewhere in the computer
# and variable just points to the location of the list
# When we set list_b = to list_a, it sets list_b equal to the same pointer as
# list_a, so using the methods like pop or append will effect the same list whether you use
# list_a or list_b

# THIS IS ALSO KNOWN AS ALIASING, as the new variable becomes an alias to the object

# to avoid copying the pointer an aliasing altogether,  use the list() function

list_a = ['apple', 'banana', 'cherry']
list_b = list(list_a)
list_a.pop(0)
print(list_b)


# is keyword
# To see if two objects are quite literally the same object (instead
# of merely having te same numbers), use the is keyword
list_a = ['apple', 'banana', 'cherry']
list_b = list_a
print(list_b is list_a) # will be true



list_a = ['apple', 'banana', 'cherry']
list_b = ['apple', 'banana', 'cherry']
print(list_b is list_a) # will be false




list_a = ['apple', 'banana', 'cherry']
list_b = list(list_a)
print(list_b is list_a) # will also be false