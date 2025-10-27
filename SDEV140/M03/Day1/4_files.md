# Text Files

## Why use files instead of just input/output

- **Unlike intput and output, files actually stick around**
- Files actually stick around on a computer to use for later
- Also, files can hold much more data
- Files can be read and be used as input much faster than typing it in each time (as a user)
- The same data be used for different programs

-----------------

# Writing To Files



Whenever you need to create and write a file, you have to use a file object

### GENERAL FILE OBJECT CREATION:
```
<file_object_variable> = open(<string of file name>, <file access string>)
```

```python
f = open("file.txt", "w")


# 'f' is a file object now. You can use it to write to a file, specifically since be
# put 'w' in the open() function

# To actually put stuff on a file, just use the write function!

f.write("wow i wrote to a file")

# After you have used the file object, make sure you close it
# If you don't close the file, SOMETIMES,
f.close()


# When you write to a file, it expects a string as the input
# so if you want to input another type of data, you need to make sure it is converted to a string
f = open("num_file.txt", 'w')
for i in range(10):
    f.write(f"This is a number: {str(i)}\n")
f.close()

```


--------

# Reading A File



You also need to read files sometimes too
You use the same open function to open a file and read it
instead of 'w' to write, we just need to use 'r' instead

```python
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
```

Put that in a loop, and you can control exactly how and which lines you are reading!


Using a for loop, you can iterate through each line more easily

```python
file = open("fileToRead.txt", 'r')
for line in file:
    print(line)
file.close()
```

You could easily get the number of characters per line in a file with code like this:
```python
file = open("fileToRead.txt", 'r')
print("Number of characters per line:")
for line_num, line in enumerate(file):
    print(f"Line {line_num}: {len(line)}")
file.close()
```

If we need to perhaps read some numbers from a file,
we need to convert the strings from the file to numbers.
We could add all the numbers found in a file with this kind of information:

```python
file = open("numbers.txt", 'r')
summation = 0

for line in file:
    line = line.strip()
    summation = summation + int(line)

print(f'Sum of numbers: {summation}')
file.close()
```



-------

# Appending To Files



Sometimes you need to add things to existing files
This is called "appending" to a file
Writing to a file will completely replace the text on a file
To just add to a file, you need to make sure you use the append functionality
by using 'a' in the open() function

```python
f = open('app.txt', 'a')
f.write('Hello World!')
f.close()

```






