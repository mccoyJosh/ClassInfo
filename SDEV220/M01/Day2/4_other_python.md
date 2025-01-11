# Other Python Information


## Comments

- Single line comments (use a hashtag symbol i.e. #)
```python
# Here is an example comment!

variable = 10 # The comment can go after code on the same line!
```


- Multiline comments (use """ or ''')
```python
"""
Here is my multiline comment
it is surrounded by three double quotes on either side of me
you could use single quotes if you'd like

Also, you may say "Hey, isn't this the same syntax as a multiline string?!
and yes, yes it is... this actually IS a string.
We just aren't assigning it to any variable or anything so it just acts as a place to write
"""
```

*How often should you use comments:*
 When it makes sense, and probably more often than you want


## Continuing lines with \

If you have a lot to write on a single line and it just ain't cuttin it, you can use \ to use the next line too!

```python
value = "Here is my really long string that I want to join with" + \
        "another string, BUT" + \
        " that string is on another line but I still want to join them" + \
        "! SOOOO I can just use the \\ character! YAY!!!!"
print(value)
```