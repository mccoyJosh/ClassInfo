# ERROR HANDLING

# When coding, many errors CAN occur and up to now, we could just have to hope that didn't happen
# NOW tho, we have if statements, which can be used to stop these errors

#################

# EXAMPLE ERROR
# This for example will error our as it tries to convert
number = int("one")
print(number + 1)


# an if statement could TECHNICALLY prevent this error
# we add a check which ensure our value is in fact a number

val = "one"
if val.isnumeric():
    number = int(val)
    print(number + 1)

# here is a better example

#################

# Let's say we are making a calculator to divide two numbers
# We want to make sure that we don't cause an error, such as attempting to divide by 0,
# so, we can use an if statement for checking if our divisor is 0

dividend = float(input("Please enter dividend: "))
divisor = float(input("Please enter divisor: "))

if divisor == 0:
    print("Cannot divide by 0!")
    exit(0)
print("Result: ", dividend / divisor)

