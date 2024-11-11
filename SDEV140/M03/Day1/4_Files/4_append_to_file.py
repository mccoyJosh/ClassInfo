
# Sometimes you need to add things to existing files
# This is called "appending" to a file
# Writing to a file will completely replace the text on a file
# To just add to a file, you need to make sure you use the append functionality
# by using 'a' in the open() function

f = open('app.txt', 'a')
f.write('Hello World!')
f.close()


