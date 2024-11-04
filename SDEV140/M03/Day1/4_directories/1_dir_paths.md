
# Directory

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

