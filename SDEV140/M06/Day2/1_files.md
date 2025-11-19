# Text Files

## Why use files instead of just input/output

- **Unlike intput and output, files actually stick around**
- Files actually stick around on a computer to use for later
- Also, files can hold much more data
- Files can be read and be used as input much faster than typing it in each time (as a user)
- The same data be used for different programs

-----------------


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

### Writing Buffer

So, as we have seen, this "works"

```python
f = open("file.txt", 'w')
f.write("Booga")
f.close()
```

This will create us the file and write the info to it.

Although, technically, python by default doesn't write anything to the file until a new line is written. The reason
we see anything being printed off is because the file is closed so it must add everything is has accumulated.

This can be seen in the following example pretty clearly:

```python
import time

f = open("file.txt", 'w')

print("Starting To Write")
f.write("New Thing")
print("The write function is done")

time.sleep(5)
f.close()

print("FIN")
```

What is happening is that there a section where the computer builds up the text to write, and once
a new line character, or the file closing, is found, it will THEN add the text.

We also have functions to automatically cause the computer to flush out the buffer and put it to the screen...
the **flush()** function

```python
import time

f = open("file.txt", 'w')

print("Starting To Write")

f.write("Newer Thing")

print("The 1st write function is done")

time.sleep(5)
f.flush()

print("The flush function is done!")

time.sleep(5)

f.close()

print("FIN")
```

The textbook says we can do the same with following function:

```
import os
os.fsync(f.fileno())
```

I found on the linux machine I was using that it did not work while f.flush() did. Also,
the newline character also didn't. Maybe it worked on windows... something to test in class!


--------


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


## BOTH APPENDING AND WRITING TO A FILE WILL CREATE THE FILE IF IT DOES NOT EXIST, WHILE READING A FILE DOES NOT!

## APPENDING WILL KEEP THE STUFF ON AN EXISTING FILE, WHILE WRITING IT WILL REMOVE ALL PREVIOUS CONTENT

