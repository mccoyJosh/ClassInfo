
# Directories

I don't know if you have noticed or not, but everything on your computer is organized into
directories, aka, folders. This is true whether you are on windows/mac/linux/etc.
Directories are a hierarchical structure for storing data. There is the
'top' directory from which all other directories are stored, which is called the root directory.

In mac/linux, this directory is just:
```
/
```

In windows, this directory is referenced by the drive you are using, typically being the C drive:
```
C:\
```


### Different *Path Separator*
Another difference between windows and mac/linux is that windows addresses which directory
is where using backslashes ( \ ) while mac/linux uses forward slashes ( / ).

So if we had a folder called 'dog' in the root directory of both types of addressing,
we would have the following

```
/dog/
C:\dog\
```

If we had a file named text.txt in both dog folders, it would look like this:

```
/dog/text.txt
C:\dog\text.txt
```

When running python, it will use whatever directory you are in to utilize as the
'current working directory'. Typically, this is the directory your code is in.
When opening files like we were just doing, they have all been located inside the
current working directory and that is why we were able to access them
with just their names

------

# OS Module

To help deal with the differences in Operating Systems, there is the OS package to deliver us a number of very
useful functions!

For these, you are going to want to import the package by using ```import os```

### os.path.join

This function takes a list of directories/file as input and returns them as a path, inserting
the OS's path separator between each value.


### os.path.sep

This stores the path separator for the current operating system you are on, so, on Mac, it returns "/"
while on Windows it returns "\".


### os.path.exists

This takes a path as input and lets the user know if it actually exists on your machine.

## os.path.getsize

This returns the number of bytes a path is


## os.walk

This is a super helpful function to walk through a directory tree on an operating system.

See the following example from section 14.3 in the book:

EXAMPLE FILE SYSTEM
``` 
logs/
    2009/      
        April/
                1/
                 log.txt
                 words.doc                                     
        January/
               15/
                 log.txt
               21/
                 log.txt
                 temp23.pdf
               24/
                 presentation.ppt
    2010/
        March/
             3/
              log.txt
             7/
              music.mp3
```


```python
import os

year = input("Enter year: ")
path = os.path.join("logs", year)
print()

for dirname, subdirs, files in os.walk(path):
    print(dirname, "contains subdirectories:", subdirs, end=" ")
    print("and the files:", files)
```


------


# Dir Access

Sometimes when you are trying to edit files, they may not be in the same directory as
the one you are in, so you need to be able to access it using paths

The rudimentary path is the absolute pathname
this is the list of directories that lead all the way up to
the file you need.

Generally, you want to try to avoid using absolute paths for 2 reasons:
1. They can get very long and annoying
   Here is an example absolute path:
   /Users/johnsmith/Development/CodingProjects/Spring/MathematicsProject/src/modules/app.txt
   This is annoying to look at when dealing with in code, and if
   there is something wrong with the path, it is hard to debug.

2. The code will not work on another computer
   Since an absolute path will describe where a file is on one's computer,
   trying to run the same code on another computer will probably
   fail. It will probably not be able to find the same directories/files!

The only real bonus is that absolute paths WILL work, as it tells a program
EXACTLY where something is on the computer


This is why instead we use RELATIVE PATH NAMES!
That is what we have been doing up to this point!
By just putting 'fileToRead.txt', we are asking the computer
to look for this file in the current working directory.
The file just happens to be relatively in the same folder as the code being run!
(NOTE: This code is meant to be run in example.py file, otherwise it won't work!)

```python
f = open('fileToRead.txt', 'r')
print(f.read())
f.close()
```

# SEE CODE 1

# SEE CODE 2





