# When you need to address a file in an inner folder,
# just give the relative path from the current working directory
f = open('inner_dir/file2.txt', 'r')
print(f.read())
f.close()

