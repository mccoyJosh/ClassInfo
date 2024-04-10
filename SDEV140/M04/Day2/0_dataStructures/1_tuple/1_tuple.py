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
# Lists cannot be used as dictionary keys, but tuples can! (because they are immutable)

tuple_1 = (1, 2, 3, 4, 5)
# tuple_1[0] = 6 # <----- THIS LINE DONT WORK SINCE IT attempts to change the tuple!
# You can access items from a tuple just like you would from a list though:
print(tuple_1[4])

# YOU CAN convert it to a list though and then change it then change it back if you really want to though
list_1 = list(tuple_1)
list_1[0] = 'hello'
print(tuple(list_1))

# Also, just like lists, tuples can also hold different types of variables

