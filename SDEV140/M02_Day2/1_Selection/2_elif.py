# SOMETIMES, you need to check more than one thing, which are typically
# dependent on the other boolean expressions being used
'''
if <boolean expression>:
    <statement-1>
    .
    .
    <statement-n>
elif <boolean expression>:
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

# For instance, if you were making code to get the letter grade of a student based off
# their in-class grade percentage, using a if-elif-else statement would be how you get that done
# EXAMPLE FIND GRADE

grade = float(input("Enter your grade: %"))

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
