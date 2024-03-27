first_name = "John"
last_name = "Doe"

# There is a way for the print function to also utilize formatting
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


# We can also use this print formatting to use the format 'code' we were using earlier:
val = 40000/3
print(f'{val:.2f}')

