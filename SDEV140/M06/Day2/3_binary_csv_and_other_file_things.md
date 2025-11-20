# Other Ways to Store Things on files

Instead of simply text in a file, sometimes it is better to store our characters 
in a way to make it usable for specific tasks.

# Binary Data

Some files store bytes of information, which is **BINARY DATA**.
This is store information like videos and pdf files... things which represent images/sounds/documents
which isn't as easily stored with characters. Instead, it is more efficient to store the data as bytes.

If you open these files in something like a text editor, it would be unreadable.

We can use bytes within python by making a byte object with the function bytes().
This byte object represents a sequence of single bytes values, such as binary data from a file.

These values are **immutable**!

Here are bany ways we can use it in python:

### bytes("string", "ascii")

This creates a sequence of bytes by encoding the string using ASCII


### bytes(100)

Creates a list of 100 bytes whose values are all 0

### bytes([12, 15, 20])

Creates a sequence of the three given values into bytes

When we try printing off these values, it will attempt to give us the readable equavelent
(characters in ascii)

In the following example, we see ABC printed out because those are the ascii value equibalent of the values given:

```python
p_obj = bytes([65, 66, 67])

print(p_obj)
```

### Reading files in **binary mode**

Up to now, we have been reading files as text files, because that is typically what we actually want to do.

We can also read them in binary mode as well:

Here is an example from the book reading the contents of an image:
```python
f = open("ball.bmp", "rb")  # Open in binary mode using "b"

# Read image binary data
contents = f.read()

print("Contents of ball.bmp:\n")
print(contents)

f.close()
```

------

# CSV Files

Another type of file is a CSV file; CSV files are files which
store data that is separated by a comma... the name being shorthand for
COMMA SEPERATED VALUES


Here is what the contents of a CSV file may look like
```
id,first name,last name,age,amount
1231,Jim,Bim,53,100235
212,George,Lorez,23,3
981,Francis,Jumper,45,42234
```

This kind of data is super easy to work with since it is simply characters
and we designate 1 character as the deliminator, that being the comma.

Honestly, reading this data into our code can be easily done 
by just splitting strings by commas, but to further help us do this, we can use the CSV module
to do this for us:

```python
import csv

with open("example.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    row_num = 1
    for row in reader:
        print(f"Row #{row_num}: {row}")
        row_num += 1
```
## with statement

Do also notice our use of the 'with' statement in the last example. 

It allows us to basically automatically open and close a file by making what's known
as a **context manager** for our file.

```
with open("myfile.txt", "r") as myfile:
    # Statement-1
    # Statement-2
    # ....
    # Statement-N
```
