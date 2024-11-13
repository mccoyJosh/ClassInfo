# Another data structure is a tuple
# Tuples are very similar to lists, BUT TUPLES ARE IMMUTABLE
# So creating one looks like this:

'''
GENERAL FORMAT:
<tuple-name> = (<item_1>, <item_2>, ..., <item_n>)
'''

# Although once a tuple is made, it cannot be changed! (SINCE IT IS IMMUTABLE)
# You are going to want a tuple when the data you are using SHOULDN'T be changed
# Also, tuples are handled faster than lists are in python, so if you have a list of constants, USE TUPLES

tuple_1 = (1, 2, 3, 4, 5)
# tuple_1[0] = 6 # <----- THIS LINE DONT WORK SINCE IT attempts to change the tuple!
# You can access items from a tuple just like you would from a list though:
print(tuple_1[4])


################################################################################
################################################################################

# YOU CAN convert it to a list though and then change it then change it back if you really want to though
list_1 = list(tuple_1)
list_1[0] = 'hello'
print(tuple(list_1))

################################################################################
################################################################################

# Also, just like lists, tuples can also hold different types of variables

tuple_2 = ("here is a string and there is an int and float ->", 1, 5.23)

################################################################################
################################################################################

# Lists cannot be used as dictionary keys, but tuples can! (because they are immutable)
# This allows us to create keys for dictionaries based off of multiple values:

people = {
    ('1/2/1980', 'Jimmy', 'Johns') : 124525325,
    ('1/2/1980', 'Elliott', 'Johns') : 34346,
    ('1/2/1980', 'Marley', 'Lang'): 545,
    ('1/2/1980', 'Jonah', 'Hudson'): 23,
    ('1/2/1980', 'Erik', 'Selinas'): 77777,
    ('1/2/1980', 'Gabriel', 'Gaines'): 45346,
    ('7/16/1976', 'Kade', 'Garza'): 9898,
    ('7/16/1976', 'Colt', 'McClaine'): 11111,
    ('6/21/2000', 'John', 'Bravo'): 234444,
    ('1/2/1980', 'Alma', 'Clay'): 88888888,
    ('12/6/1999', 'Jonas', 'Cochran'): 126,
}

print(people[('7/16/1976', 'Kade', 'Garza')])


