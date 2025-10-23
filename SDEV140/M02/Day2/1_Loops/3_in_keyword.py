# We have already used 'in' before

for num in range(10):  # HERE
    print(num)

# But it can be utilized in another way!
# AS BOOLEAN EXPRESSIONS!
# You can check if an item is 'in' most types of sequences


example_list = ["apple", "banana", "cherry"]

# Able to find it in the list
if "banana" in example_list:
    print("I found banana")
else:
     print("No banana :(")


# Does not find it in the list
if "pear" in example_list:
    print("I found pear")
else:
     print("No pear :(")


# Along with the 'not' keyword,
# you can check for something to not be in a given list
if 'pear' not in example_list:
    print("I did not find a pear")

