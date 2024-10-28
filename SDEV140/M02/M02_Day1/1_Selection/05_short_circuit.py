
# When a boolean expression is being evaluated by python, it will (typically) read it from to right
# So, if we had
x = 10
if x > 0 and x <  100 and x % 2 == 0:
    print("This number is good :)")

# So, in this instance, it will first check if x > 0, THEN do x < 100, and THEN do x % 2 == 0
# If x were -1, the x > 0 would result in false, which would result in false for the whole statement
# Python is smart enough to know how boolean statements work, and if it figures out the first expression
# In an expression containing AND, if the first expression is false, it knows the whole statement is false
# SO, it will SHORT CIRCUIT and evaluate the whole expression as false without checking the second expression


# For example,
# If you were dividing a number by a number (which could potentially be zero), you can avoid an error by doing this:
num = int(input("Enter a number: "))

if num != 0 and 100 / num > 0:
    print("The number is good :)")

# Since it is first check if num is not zero, in the case that it is zero, the boolean check for 100/num > 0
# Is never done which prevents a ZeroDivisionError from occurring
