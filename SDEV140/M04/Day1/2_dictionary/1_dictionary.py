# List allow you to make, well, lists of items, BUT, there are sometimes better ways to organize information:
# For example, let's say you were storing information about a number of individuals:
# You could do it this way:
phone_numbers = [
    ['Timmy', '555555555'],
    ['John',  '555373735'],
    ['Philip', '555544635'],
    ['Tiffany', '777777777']
]

# But retrieving anyone individual's information is a pain
# You would have to walk through the entire list and check
# each internal list to see if the place you are at has the right person
# Looking for Tiffany would look like this:

for person in phone_numbers:
    if person[0] == 'Tiffany':
        print(person[1])

# This would get Tiffany's phone number, BUT THERE'S GOT TO BE A BETTER WAY!

# Some sort of ways to quickly located particular data based on some sort of key value??????

######################################################################
######################################################################

# DICTIONARIES

# Dictionaries are the better way to hold THIS kind of information, that is,
# information organized by association, NOT POSITION
# Dictionaries work by organizing the data in key-value pairs (much like a real dictionary)
# With the data organized in this way, you can get immediate access to a key's value
# by providing the dictionary the key!

# To create a dictionary, use a set of curly brackets, {}, in which all the key:value pairs will be held
# Inside the curly brackets, you need to provide the python with a key, followed by a colon, :, and
# then the value you want stored at that key.

'''
GENERAL FORMAT
<dictionary name> = {
    <key_1>: <value_1>,
    <key_2>: <value_2>,
    ...,
    <key_n>: <value_n>
}
'''

# WITH DICTIONARIES, WE CAN CREATE TABLETS AND ASSOCIATION LISTS

######################################################################
######################################################################

# An empty dictionary looks like:
{}


# If we were to convert the previous attempt at holding names and phone numbers
# to a dictionary, it would look like this:
phone_numbers = {
    'Timmy': '555555555',
    'John': '555373735',
    'Philip': '555544635',
    'Tiffany': '777777777'
}

# Getting Tiffany's number would be as easy as putting her name in brackets!
print(phone_numbers['Tiffany'])

# In general, accessing values looks like this:
'''
GENERAL FORMAT:
<dictionary_name>[<key_value>]
'''

######################################################################
######################################################################
# MUTABLE

# Using this same format also allows us to change the value at this key.
# This is because dictionaries are MUTABLE!
# If we wanted to change Tiffany's phone number, it would look like this:
phone_numbers['Tiffany'] = '919191919'
print(phone_numbers['Tiffany'])
# Now Tiffany's phone number is a different value!


# Since dictionaries are mutable, it also means we can add values to em'
# Let's say we got a new number to add from George:
phone_numbers['George'] = '123456789'
print(phone_numbers['George'])

# Adding to dictionaries kinda looks like you are changing an existing variable, but you are in fact adding a new one


# If it is Mutable, it also means we can remove values from the dictionary too!
# Removing entries in our dictionary just involve calling the pop function and providing the key we want removed!
# If we wanted to remove George, what we would do is this:
phone_numbers.pop('George')
print(phone_numbers)

# ATTEMPTING TO POP AN KEY FROM THE DICTIONARY THAT IS NOT IN THE DICTIONARY
# WILL RESULT IN AN ERROR

######################################################################
######################################################################

# TRAVERSING DICTIONARY
# Just like lists, we can go through the entirety of a dictionary if need be
# It is a matter of using a for loop.
# NOTE: THE LOOP IS UNORDERED AND THE ITEMS YOU GET FROM THE DICTIONARY ARE MOSTLY RANDOMLY ORDERED

# Telling a loop to go through a dictionary without anything else will give you the keys
for key in phone_numbers:
    print(key)

# If you want the values, you will want to use the values function:
for value in phone_numbers.values():
    print(value)

# If you want both, use the items() function while also pattern matching the tow items into a tuple:
for (key, value) in phone_numbers.items():
    print(key, value)

######################################################################
######################################################################

# Dictionaries' keys do not need to all be the same type as well, so, this is valid
convert_num = {
    'one': 1,
    1:  1,
    'two': 2,
    2: 2,
    'three': "DOG", # THIS IS ALSO OKAY
    3: 3,
}

print(convert_num['one'] + convert_num[3])


# Also, last little word, keys for a dictionary are UNIQUE

######################################################################
######################################################################

# Lookup table
# One important use of a dictionary is a lookup tablet.
# All a lookup table is IS a conversion table
# For instance here we convert a hex string to its binary equivalent:

hexToBinaryTable = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101',
                    '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
                    'C':'1100','D':'1101','E':'1110','F':'1111'}

hexStr = '77AE'

for index in hexStr:
    print(hexToBinaryTable[index], end=' ')
print()

