# The Very Basics: Input Output

Nearly every program we write will look like this format:

- input
- proces
- output

Whether that be a website, a calculator, or a game, so much can be summarized by these steps.

So, how do we do them in python?


## Output.... print()

```python
print("hello")
```

Within the strings here, it will put your strings exactly as they appear, so, for instance:

```python
print("h    e    l   l  o")
```

This means you can also print things in shapes and what not....
this is typically considered ASCII art

* I am not super talented: this whale is from: https://www.asciiart.eu/animals/fish

```python
print('''
       .
      ":"
    ___:____     |"\\/"|
  ,'        `.    \  /
  |  O        \___/  |
~^~^~^~^~^~^~^~^~^~^~^~^~
''')
```


## Input....  input()

```python
age = input()
```

You can also put a string within a pair of quotation marks to provide the user a **prompt**!

```python
age = input("Please input your age:")
```