# Indexing

We have talked a lot about strings already, but there are a few things we still need to discuss

First off, strings is a type of data structure!
# DATA STRUCTURE: A compound unit that consists of several other pieces of data

Strings are a sequence of characters, which, is a compound of a bunch of data
```python 
'dog'

```

This string is a sequence consisting of 3 characters
Just like nearly every other data structure type object,
using the len() function will give up the length of the string

```python
len('dog')

print("Here is the length of 'dog':", len('dog'))

```
Again, as previously mentioned, we can access any single char from a string by using its index


```
GENERAL FORMAT:
<string>[<integer>]

```

```python
str = 'Dog'
print(str[1])

```

Indices start at 0 and increment per character


```
STRING: Here word
INDEX:  012346789
```

This is nearly* equivalent to y
(*: technically y is a list while a string is a sequence which is different, but they do index the same)


```python
x = "Here are a few words"
y = ['H', 'e', 'r', 'e', ' ', 'a', 'r', 'e', ' ', 'a', ' ', 'f', 'e', 'w', ' ', 'w', 'o', 'r', 'd', 's']
for i in range(len(x)):
    print(x[i] == y[i])  EVERY INDEX IS THE SAME
```


We have talked about the index of this before, so this should all be old news, but, it is essential for the next part:


# SLICING
Sometimes you need to get only a portion of a string, aka, a substring
This is when slicing comes in handy; to make a slice, use a colon along with some indice(s)


General Format:
```
<string>[<start integer>:<end integer>]
```

The <start integer> will be the index of where the substring will start,
and be inclusive (includes the value at that index)

The <end integer> will be the index where the substring will end,
and will be exclusive (DOES NOT include the value at the index)





```python
x = "Here are a few words"
print(x[0: len(x)])
```

This example here shows a simple slicing of a string. Here, we get the whole string
The 'slice' starts at index zero (inclusively) and ends at the length of the string (exclusivity)

Doing this will result in the same thing, as the last value defaults to the end of the string if no value is provided
```python
x = "Here are a few words"
print(x[0:])
```

Doing this will also result in the same thing, as the first value defaults to 0 if no value is provided

```python
x = "Here are a few words"
print(x[:])
```



With this in mind, if we just wanted to grab the first word in this string, we can do this:
```python
x = "Here are a few words"
print(x[:4])
```

If we wanted to grab the last word, we can do this:
```python
x = "Here are a few words"
print(x[len(x)-5:])
```

While on the subject of substrings, you can also use the 'in' keyword to see if a substring is contained within a
larger string
```python
text = '''Here are a ton of words which maybe you don\'t
know what is in it but you need to know if the word burger appears in it.
There are just a lot of words here to making an if statement and searching for the substring
yourself would be just fine but python is made to try to save you time as a developer so
using the tools it provides to you is something you may want to do. It makes life a bit easier!
'''

if 'burger' in text:
    print('Yeah burger is in the text')
else:
    print('Sorry, no burger')
```


ALSO
Strings are immutable, meaning you cannot change them once they are created
This doesn't mean the variable can't be changed
BUT, you can't change the individual characters in a string
For example, this will not work:


```python
str1 = "Hello World"
str1[0] = 'a'
```

