# Lab

---------

# Sorting Time (But Badly)

MAYBE YOU DON'T HAVE ACCESS TO THE SORTING METHOD FOR SOME REASON
but still need stuff sorted

> Make a piece of code where, given a list of integers, it is able to sort them in ascending order

This code is very inefficient. We are visiting every element in the list two times over.
(Similar to bubble sort)

```python
import sys

# Initializes data
data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

sorted_list = []
size = len(data)

# For every value in the list
for i in range(size):
    # Inits smallest_value variable
    smallest_value = int(sys.maxsize)
    
    # Finds smallest value in list
    for val in data:
        smallest_value = min(smallest_value, val)
    # Removes it from OG list
    data.remove(smallest_value)
    # Adds it to end of new list
    sorted_list.append(smallest_value)


print('Sorted Array in Ascending Order:')
print(sorted_list)
```




---------

# Dictionary Time

> Read in a csv file containing information about members in an organization
> and create a text based database system by utilizing a dictionary to view
> information on users based off their member id or name


Only problem with using the name as the key is that if two people have the same
name, they will overwrite each other and one of their information will be deleted.

To avoid this and to ensure unique names are used as keys, we typically
generate keys of some sort and or use uniquely identifying information.

In this case, we just have keys assigned to each person, but we could have usernames, for instance.

The current code has the names as the keys, but that can easily be switched to id

```python
# Opens file
file = open('assets/members.csv', 'r')

# Strips first line as it is the header
header = file.readline().strip()
header = header.split(',')

# Creates database object (dictionary)
db = {}

# Goes to each line in the file
for line in file:
    # Splits line by commas to get to individual values
    items = line.split(',')
    
    # Uses the id or name as unique identifier and adds entry to database
    id = items[0]
    name = items[1]
    db[name] = items

# Closes file
file.close()

# Creates loop for user interface to interface
print("WELCOME TO THE MEMBER DATABASE")
while True:
    # Gets user input and ensures it is a valid input
    user_input = input("Name to search or STOP: ")
    if user_input in db:
        user_info = db[user_input]
        print("--------------------")
        # Prints out all the info available
        for index in range(len(header)):
            print(f"{header[index]}: {user_info[index]}")
    elif user_input == 'STOP':
        break
    else:
        print("Please enter a valid input")
    
print("FIN")
```

