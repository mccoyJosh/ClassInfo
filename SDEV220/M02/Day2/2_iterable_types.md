# Iterable Types

There are many types (I'm sure has already seen) to store many values within it.

None of these types necessarily care about what types are used within it. 
This is different compared to other programming languages where you 
need to make arrays of a certain type


# Mutability

Some types of objects in python are immutable.

*Immutable*: cannot change once it is made

*Mutable*: CAN change

Strings are immutable, for instance. Once they are made, you cannot change it.
You can reassign a variable holding a string, SURE, but not actually change the string 
object.


# Lists

- mutable
- can add/remove items from list
- created using [] with commas separating each value within
- use [INDEX] to get specific values from list

EXAMPLE:
```python
listi = [1, 2, 5, 7, 23]
listi.append("AJJ")
listi.remove(23) # removes this VALUE from the list
listi.pop(2) # removes this INDEX from the list
print(listi)
```

# Tuples

- immutable
- cannot ADD nor REMOVE anything from a tuple; is the same after initialization
- created using () with commas separating each value within
- uses [INDEX] to get a specific value from the tuple
- technically retrieves values faster than a list since the computer KNOWS for sure where they are, unlike
  a list where the items in the list can and will move around due to its mutability

EXAMPLE
```python
tupe = ('here', 'are', 4,  'items')
print(tupe[3])
```

# Dictionaries

- mutable
- can add/remove Key, Value pairs
- keys are unique (adding the same key twice overrides previous value)
- created using {}


```python
dictionary = {"Cat":100, "Dog":12124}
dictionary["Lemur"] = 777
dictionary["Bear"] = 992929
dictionary.pop("Cat") # Removes this key
print(dictionary["Dog"])
```



# Sets

- immutable
- represents a set like in mathematics
- unordered SET of values
- created using {} but not using key,value pairs
- USING JUST {} STILL CREATES A DICTIONARY
