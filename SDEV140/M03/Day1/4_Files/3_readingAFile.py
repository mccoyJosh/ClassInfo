
# You also need to read files sometimes too
# You use the same open function to open a file and read it
# instead of 'w' to write, we just need to use 'r' instead
file = open("fileToRead.txt", 'r')

# reading it with the read() function will read the entire file
# (remember to close() it!)

entirety_of_file = file.read()
print(entirety_of_file)
file.close()


#  You can also read just one line in a file if you would like
file = open("fileToRead.txt", 'r')
line_in_file = file.readline()
print(line_in_file)
file.close()

# Put that in a loop, and you can control exactly how and which lines you are reading!


# Using a for loop, you can iterate through each line more easily
file = open("fileToRead.txt", 'r')
for line in file:
    print(line)
file.close()


# You could easily get the number of characters per line in a file with code like this:
file = open("fileToRead.txt", 'r')
print("Number of characters per line:")
for line_num, line in enumerate(file):
    print(f"Line {line_num}: {len(line)}")
file.close()


# If we need to perhaps read some numbers from a file,
# we need to convert the strings from the file to numbers.
# We could add all the numbers found in a file with this kind of information:
file = open("numbers.txt", 'r')
summation = 0

for line in file:
    line = line.strip()
    summation = summation + int(line)

print(f'Sum of numbers: {summation}')
file.close()

