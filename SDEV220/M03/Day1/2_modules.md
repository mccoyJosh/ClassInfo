# Modules and Project Organization

Modules are simply the scope of a single Python; 
more simply: module = python file (without .py at the end)

Whenever you are working on a single file, you are writing all
of your code within said module. Things which are declared outside the scopes
of other structures (not tabbed over, not in function, class, etc.) are considered
**module variables** or **global variables** and can be accessed anywhere in the module.

## Using other modules

To utilize code from another module, simply `import` it (just like you have been doing
for some packages).

Let's say we have two files: **magic.py** and **main.py**

### magic.py
```python
apple = 'exists'

def make_apple_disappear():
    global apple
    apple = 'GONE'

def print_apples_state():
    print(apple)

def add_apple_to_string(input_string):
    return input_string + "apple"
```

### main.py
```python
import magic

magic.print_apples_state()
magic.make_apple_disappear()
magic.print_apples_state()
```


----

*ONE COULD ALSO SIMPLIFY THIS BY USING 'as' TO ALIAS THE PACKAGE NAME:*
### main.py (works the same as previously but condensed)
```python
import magic as m

m.print_apples_state()
m.make_apple_disappear()
m.print_apples_state()
```

----

*If I only wanted the make_apple_disappear method, you can specify that:*

### main.py (now only importing the one method)
```python
from magic import add_apple_to_string

apple_string = add_apple_to_string("I have an ")
print(apple_string)
```
