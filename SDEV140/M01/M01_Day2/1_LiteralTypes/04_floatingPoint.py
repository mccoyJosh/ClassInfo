
# For real numbers (values which contain a decimal) use floating point values
# HERE ARE SOME VALID FLOATING POINT VALUES
1.0
3.14159
-12309723905702937527.


# you can also use sciencitific notation to declare a floating point value
# so instead of this:
30_000.
# you can do this:
3e4

print(30_000. == 3e4)  # This prints True, because these values are quite literally the same thing

# represent small decimal values as well:
print(4.5E-2)
# if it is very small, python will print it out as scientific notation automatically
print(4.5E-10)
