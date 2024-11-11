# Sometimes when you are trying to edit files, they may not be in the same directory as
# the one you are in, so you need to be able to access it using paths

# The rudimentary path is the absolute pathname
# this is the list of directories that lead all the way up to
# the file you need.

# Generally, you want to try to avoid using absolute paths for 2 reasons:
# 1. They can get very long and annoying
#    Here is an example absolute path:
#    /Users/johnsmith/Development/CodingProjects/Spring/MathematicsProject/src/modules/app.txt
#    This is annoying to look at when dealing with in code, and if
#    there is something wrong with the path, it is hard to debug.

# 2. The code will not work on another computer
#    Since an absolute path will describe where a file is on one's computer,
#    trying to run the same code on another computer will probably
#    fail. It will probably not be able to find the same directories/files!

# The only real bonus is that absolute paths WILL work, as it tells a program
# EXACTLY where something is on the computer


# This is why instead we use RELATIVE PATH NAMES!
# That is what we have been doing up to this point!
# By just putting 'fileToRead.txt', we are asking the computer
# to look for this file in the current working directory.
# The file just happens to be relatively in the same folder as the code being run!
# (NOTE: This code is meant to be run in example.py file, otherwise it won't work!)
f = open('fileToRead.txt', 'r')
print(f.read())
f.close()

# SEE CODE 1

# SEE CODE 2

