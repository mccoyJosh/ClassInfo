# if you need to access a file that is 'up' a layer
# in the hierarchy of files on your computer,
# use .. to address to it!
f = open('../file1.txt', 'r')
print(f.read())
f.close()


# This allows you to go out from your current directory,
# and then into a child directory
f = open('../another_dir/file3.txt', 'r')
print(f.read())
f.close()
