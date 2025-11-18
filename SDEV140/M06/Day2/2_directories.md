
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





