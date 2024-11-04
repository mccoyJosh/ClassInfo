
# Most objects in any language will have methods associated with them.
# Methods are simply some functionality / process that the object provides
'''
GENERAL FORMAT:
<object>.<method name>(<arg-1>,...,<arg-n>)
'''

# Strings are no exception to this rule

# One important method is the split method. As it sounds, it splits a string
x = 'Here is a string with lots of words'

# This will take the string and split it into a list where ever it finds a space
print(x.split())

# A space is just the default value. You can also provide a value to split by, such as commas
x = 'Here,is,a,string,with,lots,of,words'
print(x.split(','))

# Or longer strings
x = 'wow That wow is wow a wow lot wow of wow words wow'
print(x.split('wow'))

# To get an explanation of what a method does, you can use the help() method
print(help("example string".split))

# To get all the methods of a type of object you can use the dir() method
print(dir(str))