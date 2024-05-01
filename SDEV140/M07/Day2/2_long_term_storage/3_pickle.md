# Pickle

## What is it?
Pickle is a built in python library which allows
us to save python data and load it back into python objects
without much hassle. 

Unlike the other types of data we had looked at, this
data-saving process cannot be utilized for transferring data from one
language to another... as the pickled data is for python alone.

----

# Saving Objects

Notice when you save the object, it is not in a human-readable
format! Pickle converts python objects to a byte-stream, so
it can be re-read straight into python. 

KEEP IN MIND THE DATA YOU UNPICKLE CAN BE MALICIOUS AND 
CAN EXECUTE CODE SO DO NOT UNPICKLE CODE YOU DON'T TRUST

See more here: https://docs.python.org/3/library/pickle.html

```python
import pickle


def save(self, fileName=None):
    if fileName is None:
        return
    fileObj = open(fileName, 'wb')
    pickle.dump(self, fileObj)
    fileObj.close()


class ExampleClass:
    def __init__(self, val, num, cost):
        self.val = val
        self.num = num
        self.cost = cost

    def __str__(self):
        return f'{self.val} {self.num} {self.cost}'


e = ExampleClass('eeee', 10, 10000)
b = ExampleClass('bbbb', 11, 10000)

save(e, 'e.save')
save(b, 'b.save')
```

---


# Loading Objects

```python
import pickle

def load(fileName = None):
    if fileName is None:
        return
    fileObj = open(fileName, 'rb')
    try:
        ex = pickle.load(fileObj)
        fileObj.close()
        return ex
    except EOFError:
        fileObj.close()


class ExampleClass:
    def __init__(self, val, num, cost):
        self.val = val
        self.num = num
        self.cost = cost

    def __str__(self):
        return f'{self.val} {self.num} {self.cost}'

print(load('e.save'))
```