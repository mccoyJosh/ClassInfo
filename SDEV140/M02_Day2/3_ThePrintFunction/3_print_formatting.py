# Sometimes, to create better, and more comprehensible print statements, you want to use some formatting tool
first_name = "John"
last_name = "Doe"

# We could do this
print("Name:", first_name, last_name)

# or we could use an f'' formatting string.
# This allows us to just place the variable in the string where ever they need to go (given we put them within {}s )
print(f"Name: {first_name} {last_name}")


# There is another way to use formatting, that being using the format function:
print("Name: {} {}".format(first_name, last_name))
# Where you place a set of curly braces {}, it is expecting a variable

# This comes with the added bonus of being able to reorganize which variables are printed in what order
# NORMAL
print("Name: {0} {1}".format(first_name, last_name))
# REORGANIZED (now prints Name: Doe John)
print("Name: {1} {0}".format(first_name, last_name))


# Formatting also has the ability to format types of data:
# MOST COMMON USAGE: FLOATS
val = 40000/3
print(val)
# This prints out 13.333333333333334, which, typically you don't care about the exact decimal values.
# To format the floats to round up the decimal place, use format strings
print(f'{val:.2f}')

