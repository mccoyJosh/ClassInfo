
# Whenever you need to create and write a file, you have to use a file object
"""
GENERAL FILE OBJECT CREATION:
<file_object_variable> = open(<string of file name>, <file access string>)
"""


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

