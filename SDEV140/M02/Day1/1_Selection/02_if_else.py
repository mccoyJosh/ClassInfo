# In some cases, you may want to have a certain action occur if the 'if' statement fails
# This is where the else comes in.
# The else statement occurs if the 'if' statement's boolean expression fails

'''
if <boolean expression>:
    <statement-1>
    .
    .
    <statement-n>
else:
    <statement-1>
    .
    .
    <statement-n>
'''


############################
############################

# For instance, you could use an else statement for the previous example

dividend = float(input("Please enter dividend: "))
divisor = float(input("Please enter divisor: "))

if divisor == 0:
    print("Cannot divide by 0!")
else:
    print("Result: ", dividend / divisor)
print("Look I'm still running!")

# This helps simplify the code, and allows for the continuation of the code following the if-else statement




