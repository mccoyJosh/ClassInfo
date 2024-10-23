# integers are just digits that are whole numbers
10
0
9223372036854775807
-1


# integers cannot consist of anything other than digits and underscores. Use underscores to more clearly indicate
# large numbers

1_999_999_999

print(1_999_999_999 + 1)


# other than base 10 values

# BINARY
1001_0110_0111_1111  # this may look like binaryn but this is NOT. This is a base 10 value
print(1001_0110_0111_1111 + 1)

# denote binary values using the prefix 0b or 0B
print(0B1001_0110_0111_1111)  # prints 38527 (integer equivalent)
print(bin(38527))             # prints 38527 as it's binary equivalent

# OCTAL VALUES
# denote octal values using the prefix 0o or 0O
print(0o113177)
print(oct(38527))


# HEXADECIMAL
# denote hexadecimal values using the prefix 0x or 0X
print(0x967f)
print(hex(38527))

################################################################################
################################################################################


# Operators
# Now there are operators for integers as well
# we can add them, subtract them, multiply them, and a few more things, but we will get to them in just a moment,
# to understand them fully, FIRST WE NEED TO TALK ABOUT FLOATING POINT VALUES
