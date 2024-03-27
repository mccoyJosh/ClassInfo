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

# If it is true, it runs the code; if false, it skips it

# Let's say we are making a calculator to divide two numbers
# We want to make sure that we don't cause an error, such as attempting to divide by 0,
# so, we can use an if statement for checking if our divisor is 0

dividend = float(input("Please enter dividend: "))
divisor = float(input("Please enter divisor: "))

if divisor == 0:
    print("Cannot divide by 0!")
    exit(0)
print("Result: ", dividend / divisor)


# SHORTHAND FORM IF STATEMENT!
# If you only have 1 statement to run from your 'if' statement
# You can put it immediately after your colons
'''
if <boolean expression>: <instruction statement>
'''

x = 10
if x == 10: print("10 is 10 yay")

# This can help tidy up your code if you have many short, 1 line if statements
