# THIS IS ONE OF THE MOST IMPORTANT FUNCTIONALITIES OF ANY LANGUAGE

# In most code, you need it to diverge.
# This can be for various reason, such as
# - error handling
# - alternative computations
# - optional code

# To use an if statement, use this format:
'''
if <boolean expression>:
    <statement-1>
    .
    .
    <statement-n>
'''
# Once the code reaches the 'if' statement, it will evaluate
# the boolean expression to determine if the statements
# within the loop will execute.


# If it is true, it runs the code; if false, it does not run that code

############################################################
############################################################

# BASIC EXAMPLE

# if the number is 1, you get a fun message :)

# This will print Hello Person!
number = 1
if number == 1:
    print("Hello Person!")


# This will not :(
number = 0
if number == 1:
    print("Hello Person!")

# This is the very basis to making code
# If we didn't have some sort of tool to make our code do multiple things, we would only ever be making
# very specific programs only able to do one task without the ability to automatically conform to a problem.



############################################################
############################################################

# EVEN/ODD EXAMPLE


number = 0
print("Number:", number)

if number % 2 == 0:
    print("This number is even!")

if number % 2 == 1:
    print("This number is odd!")

############################################################
############################################################

# SCOPE (initial)
# all the scope is IS the content of a given coding construct
# With the introduction of if statements, we get to our first "scope", that being the contents of the if statement
# it is everything tabbed over!

val = 1
if val == 1:
    print("This is within the scope of the if statement")
    print("This is within the scope of the if statement")
    print("This is within the scope of the if statement")
    print("This is within the scope of the if statement")
print("This is NOT within the scope of the if statement")

# we WILL talk more about this later


############################################################
############################################################

# NESTED STATEMENTS

# nested statements are simply statements found within the scope of another construct

# Here is a simple example
if True:
    if True:
        print("This is true!")


# EVEN/ODD EXAMPLE AND DECIDING IF THEY ARE PRIME LESS THAN 10

number = 0
print("Number:", number)

if number % 2 == 0:
    print("This number is even!")
    if number == 2:
        print("This number is a prime!")

if number % 2 == 1:
    print("This number is odd!")
    if number == 3 or number == 5 or number == 7:
        print("This number is a prime!")

############################################################
############################################################

# SHORTHAND FORM IF STATEMENT!
# If you only have 1 statement to run from your 'if' statement
# You can put it immediately after your colons
'''
if <boolean expression>: <instruction statement>
'''

x = 10
if x == 10: print("10 is 10 yay")

# This can help tidy up your code if you have many short, 1 line if statements
