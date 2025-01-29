# Hash Maps

One final data structure we will talk about today is hash maps...
which actually don't use nodes and rely on arrays to work

The dictionaries in python are built on the idea of hash maps to allow us near instant access to values within them... with a cost.


# What is it to map

A map is a simple structure. All it is is a predefined space with a set number of indices where values
are placed based on what they are. So, as a simple example, imagine an array of size 10 (0 being the first index, and 9 being the last index).

Initially, the array of sorts is filled with empty spaces. We just need open indices, really
```
Indices:  0 1 2 3 4 5 6 7 8 9
Map:     [ , , , , , , , , , ]
```

We want to place a list of numbers we have inside of this data structure. 
Maybe, these numbers: 2, 3, 5, 7
Our map would then look like this:
```
Indices:  0 1 2 3 4 5 6 7 8 9
Map:     [ , ,2,3, ,5, ,7, , ]
```

Now, with these values added, we can INSTANTLY search our data structure for values:

If we are looking for if 2 is in the structure, we can use ```map[2]``` and if it isn't None, we know it is there.
There is no need to look at every index of the map, as if 2 is in there, it HAS to be at index 2.

> RESULTS IN O(1) retrieval time... we have a constant time in finding the value we are asking for 

> Downside: larger memory cost -> we need to create a large, predetermined area set aside for our map for it to correctly function

Also, this map specifically lacks a few things:
- adding values not exclusively between the values of 0 and 9
- adding duplicate values

Well, making a hashmap will solves these issues... but first, what does it mean to hash something?

----

# What is a hash

Simply put, a hash is an algorithm which converts any data, whether that be strings, numbers or OTHER data, into a fixed result, whether that be a string of characters, or a discrete set of numbers.

Hashes guarantee us that regardless of the input, we can get a usable output.

A very simply hash is converting any given number into a smaller set of given numbers.

For instance, lets say we wanted to ensure that regardless of the number provided to us, we NEED the hash
to result in something between 0 and 9. An easy algorithm to implement would be just to modulus 10 our input.

In this case, our hashing algorithm would be `input%10`.
Here are a few examples of running numbers through this hash:
- 5 -> HASH -> 5
- 45 -> HASH -> 5
- 32 -> HASH -> 2
- 99 -> HASH -> 9
- 325352435 -> HASH -> 5

## ESSENTIAL NOTE: No matter how many times you use the code, the resulting hash WILL be the same for the given input number.

----

# What if we... combined them

Now, with an understanding of what a hashing algorithm is, we can talk about hash maps. Essentially,
the only thing that changes is that we will always run our value we are trying to input into
our map through a hashing function before hand. This allows us to add numbers not part of the initial bounds of
the array.

So now, if we started with the same map as before:
```
Indices:  0 1 2 3 4 5 6 7 8 9
Map:     [ , , , , , , , , , ]
```

But now try to insert these values, 800 654 23 17 9 and 66, the map works just fine.
Note that our hashing algorithm is also `input % 10`, as to ensure the result is within the bounds
of the array. If we had map with 150 spots, our hashing algorithm would probably be something like: `input % 150`.

```
Indices:    0   1    2     3    4    5    6    7    8    9
Map:     [ 800,    ,    ,  23, 654,    ,  66,   17,    ,  9 ]
```

Just like before, we are able to find if a value is within the map near INSTANTANEOUSLY...
we just need to quickly run the value we are trying to find through the same hash algorithm 
as to see where it would be located.

If were trying to see if 76 is in the map, we could hash the number, get 6, and check that index for 76.

We can see that 66 is there and not 76, and we don't have to search the rest of the map at all!


# Collision Resolution: What happens if two of the same resulting values exists:

Well, what happens is known as a **collision**, as in two numbers are "suppose" to be in the same spot.

## Better Hashes

If you make a complex enough hash as to ensure no two input values result in the same space, you won't have to worry about a 
collision occurring. This also requires FAR MORE memory use though, as you need predefined spaces for all values which can be 
very large depending on the data you are attempting to place in your hash map.

An ideal hash will not only convert it to a pre-defined problem set and/or fixed length item, but also be complex enough where
data which are "close" to each other end up as completely different outputs.

Despite these values being initially similar, their outputs are very different. Hopefully this results in a greater range of values to diversify your map indices.
- 5 -> HASH -> 104
- 6 -> HASH -> 2

Also, unlike hashes for keys for cyber security where they need to be able to be 'dehashed', we do not have that "need" here as we just need the output for the purpose of like an index.

This should really be done in conjunction with the next few collision resolution items, but I digress

## (Linear) Probing

This collision technique solves collisions by placing the new colliding value in the NEXT AVAILABLE SPACE in the map.

Some probing techniques don't simply use the very next space and instead find a better spot some place else, but the idea is the same: find another, easily calculated spot to place the value.

This does mean whenever we are looking for a value, the resulting hash isn't immediately assuring us the value will be there... we may have to walk a number of indices down from the expected position until we find an empty spot proving we no longer

## (Separate) Chaining

This collision resolution solves this problem by having some sort of dynamic structure at each index of your 
array and simply appending the new value to the existing list.

This also has the problem where if a lot of items are ending up in the same location, you will
need to end up looking through the entire list of values placed there to maybe find your item,
which, if done incorrectly, can make you lose the time saving benefits of using a hash map.


## Only Allowing Uniquely Hashed Values

In this sort of collision resolutions, we simply replace the previous value
with the new value and call it a day. No need to store both values.

# Python Dictionaries is based on this hash map

The python dictionary does a few special things for it to work:

- uses keys as it's object to hash (AND THEY MUST BE UNIQUE)
  - If you try using a value which is mutable, it refuses and tells you that is in non-hashable, which makes sense (how can you expect changing values to be hashed the same???)
- Allows different types of values to be inserted into it's map
- remembers order which values were added
- DOES CHANGE SIZE
  - [How are they doing that?](https://stackoverflow.com/questions/327311/how-are-pythons-built-in-dictionaries-implemented)
    - starts with 8 slots
    - resizes if 2/3 slots in hash map is full
- does 'pseudo-random probing' if collision occurs, whether that be in insertion or looking for value

The code base for the Dictionary object can be found [here](https://hg.python.org/cpython/file/52f68c95e025/Objects/dictobject.c). Cool to look at! Also, it is written in C


# Here is an example of a hash map using separate chaining to solve collisions
```python
import math


class IntegerHashMap:
    def __init__(self, number_of_spots):
        self.size = number_of_spots
        self.held_items = 0

        # Creates list with a list at every index of the map
        init_list = []
        for _ in range(number_of_spots):
            init_list.append([])
        # Convert it to tuple as number of spots don't need to change
        self.hash_map = tuple(init_list)
    
    def simple_hash(self, value):
        return int(math.sqrt(float(abs(value))) * 1000)  % self.size # Takes square root, multiplies by 1000, modulus by size

    def insert(self, value):
        index = self.simple_hash(value)
        self.hash_map[index].append(value)
        self.held_items += 1 

    def delete(self, value):
        index = self.simple_hash(value)
        self.hash_map[index].remove(value)
        return None
    
    def contains(self, value):
        index = self.simple_hash(value)
        for val in self.hash_map[index]:
            if val == value:
                return True
        return False
    
    def print_map(self):
        print(f"Number of items: {self.held_items}")
        for index in range(self.size):
            print(f"\t{index:4}: ", end="")
            for val in self.hash_map[index]:
                print(f"{val}, ", end='')
            print()



hm = IntegerHashMap(20)
hm.insert(3)
hm.insert(30)
hm.insert(4)
hm.insert(87)
hm.insert(12)
hm.insert(54)
hm.insert(43)
hm.insert(10013)
hm.insert(899)
hm.insert(-112414)
hm.insert(90)

hm.print_map()


print(f"Is 3 in this hashmap: {hm.contains(3)}")
print(f"Is 1241532 in this hashmap: {hm.contains(1241532)}")
```

