# Files and Folders

With simple code, we've been just writing code, and the code runs, and the information from said code only lasts while it is running, and is no longer in existence hence forth.

The easiest way to store stuff on your computer is with files.

Here is a simple way of reading and writing to a file, and also saving data
as to not need to ask for it every time a user uses a program:

```python
from pathlib import Path

# Initializes name var and Path variable
file_check = Path('saved_data.txt')
name = ''

if file_check.exists(): # First checks to see if file is made 
    file = open("saved_data.txt", 'r')
    name = file.read()
    file.close()
else:
    name = input('What is your name: ')
    file = open("saved_data.txt", 'w')
    file.write(name)
    file.close()

print('Here is your name backwards:')
for index in range(len(name) - 1, -1, -1):
    print(f'{name[index]}', end='')
print()
```
None of this should be new. File opening and closing is nothing crazy.

# Folders/Directories

We also have folders and directories to deal with when using/locating files.

Folders are organized as a tree structure on your device.
There is a root folder from which all other folders descend from.

```
root
|
|- etc
|
|- bin
|
|- usr
...
```
When navigating to specific files, they will always have a path starting from the root.

In linux/mac, the root is /

In Windows, the root is C:\



If on our computer, we had a folder named `dev` inside the `user` folder that was inside the `root` folder, 
getting to the dev folder would look like this:

Mac/Linux
```
cd /user/dev
```

Windows
```
cd C:\user\dev
```

They are VERY similar, just windows uses backward slashes instead of forward slashes (and the root, obviously).

Using the correct forward/backward slash is not super important, as most languages do automatically fix the direction depending on your operating system.

Also, these paths that start from the root and go to a file/directory are considered **absolute paths**.

The other type of path, **relative paths** start from whatever your current working directory and finds files 
relatively from there.

For instance, if your code was running inside of a directory with a folder called `assets` in it, and you wanted to use 
`picture.png` from aforementioned directory, access said file with a path like this:

Mac/Linux
```
assets/picture.png
```

Windows
```
assets\picture.png
```

The only real difference between this and the absolute paths is that you are NOT starting the path with / or C:\ and instead using the directories/files name!