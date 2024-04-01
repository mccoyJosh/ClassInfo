# let's say yu are trying to code something, such as the Fibonacci sequence
value  = 1

print("1st: ", value)
print("2nd: ", value)

value = value + 1
print("3rd: ", value)


#         2      1
value = value + 1
print("4th: ", value)


#         3      2
value = value + 2
print("5th: ", value)

# This is time-consuming and dumb.
# Most importantly, to solve more and more complex problems, you need to write more and more code


# Whenever you need to do a process repeatedly, USE A LOOP
# The simpliest loop is a while loop
'''
while <boolean expression>:
    <statement-1>
    .
    .
    <statement-n>
'''
# As long as the boolean expression is true, the loop will repeat
# THE WAY PYTHON DETERMINES IF SOMETHING IS
# "IN THE LOOP (part of the loop body)" IS BY TABS
# (ONE TAB OVER FROM LOOP HEADER)

i = 0
while i < 5:
    print(i)
    i = i + 1

# keep in mind that this WILL NOT print out 5. Once i == 5, it is no longer less than 5, so the loop stops


# if we do this:
'''
while True:
    print("Hello World")
'''
# This will run forever


# if we do this:
while False:
    print("Howdy yall")
# This wouldn't execute at all


# Fibonacci Sequence nth Value
t_0 = 0
t_1 = 1
value = t_1

n = 10
n = n - 2
while n > 0:
    n -= 1
    t_0 = t_1
    t_1 = value
    value = t_0 + t_1
print("Val: ", value)


