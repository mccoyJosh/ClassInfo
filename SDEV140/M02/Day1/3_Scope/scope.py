# So currently we've covered 'if' statements
# Each of these have a rule for what is contained within the loop 1 tab over from the header of the statement
# For example:
n = input('Enter a thing: ')

if n == "Something":
    # This is inside the if statement
    pass
    # This is also inside the if statement
# This is NOT in the if statement


# The area that is tabbed over and inside an if statement or loop
# is considered inside an 'if' statement's or loop's scope
# In Python, scope is determined by the number of tab characters before a given statement on a line
# In other languages, scope is often determined by curly braces instead of tabs
# So, if we labeled the scope of the previous if statement, it would be like this:

if n == "Something":
    # Within scope of if statement
    pass
    # Also within scope of if statement
# This is NOT in the scope of the if statement


# You can have multiple scopes contained within each other
# For example:
char = 'x'
if char in n:
    # Only within the scope of the 'for' loop
    if char == 'x':
        # Within the scope of both the 'if' statement AND 'for' loop
        pass
    # Also just within the scope of the 'for' loop
# Not in either 'for' or 'if' scopes


# Everything is contained in what is considered the "global scope"

# Now, along with describing what code is executed for an if statement or for loop,
# They also describe the life-span of a variable


# X was made in the global scope, and can be used within the scope of the if statement just fine
x = 10
if True:
    x = x + 10
print(x)


# If you are familiar with other languages,
# the scope can often prevent you from using
# a variable created in an inner scope
'''
JAVA:
if (true) {
    int x = 20;
}
System.out.println(x);
'''

'''
GOLANG:
x := 10
    if true {
        x := 20
        fmt.Println(x)
    }
fmt.Println(x)      // <---- this x here is not the same x as was made in the inner scope
'''

# In python though, you can create a variable in an 'inner' scope and still use it in the global scope
if True:
    x = 80
print(x)

# Even something really dumb like this works:
if True:
    if True:
        if True:
            if True:
                if True:
                    if True:
                        x = 80
print(x)


# Now do be aware that the previous example only worked because that most inner scope was actually run
# If we had something like this:
if False:
    x = 10
print(x)
# The line with x = 10 never is run, so when we try to print out x, it was never created, so it fails


# The only time scope DOES MATTER is when creating functions, which, we will get into later,
# but, just as a quick example, here is something that DOES NOT WORK

'''
def function_name():
    example_variable = 90
    print(example_variable)

print(example_variable)
'''


# The definition of the function, just like the 'if' statement and 'for' loop, has a scope
# of what is considered inside of it. The example_variable is created inside the
# function, BUT, python considers this variable to be a local variable to the function
# and not accessible to the global scope

# Now, there ARE ways around this, such as using the global keyword

def function_name():
    global example_variable
    example_variable = 90


function_name()
print(example_variable)
