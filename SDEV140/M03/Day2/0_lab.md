# Lab


------

> Implement a guessing game where the computer makes up a number from a provided range and the user is expected to guess that value.
> Have the user the ability to continuously guess until they get the number while letting them know if each guess is greater or less than the
> number they are guess. When they found the correct number, let them know and print out the number of guesses they tried.
>
> Please validate the users input and limit the user to guess only log(range_diff)*1.5 (as an integer)

Good example of allowing a user to keep doing 'something' and validating the user input!

```python
import random
import math

# Get input from the user
lower_range = int(input("Enter the lower range: "))
upper_range = int(input("Enter the upper range: "))

# Initializes the number being guessed and counting variable to print out number of tries at the end
secret_number = random.randint(lower_range, upper_range)
guesses_count = 0
number_of_guesses = int(math.log(upper_range - lower_range) * 1.5)

# Repeats until the user guesses the number or exceeds limit
while guesses_count < number_of_guesses:
    # Gets a new guess
    user_guess = input("Enter your guess: ")
    
    # Validates user's input
    
    # Ensures a number was entered
    if user_guess.isnumeric():
        user_guess = int(user_guess)
        
        # Ensures the guess was within range
        if lower_range > user_guess or user_guess > upper_range:
            print("Your guess was outside the range!")
            continue
    else:
        print("Please type in a number!")
        continue
    
    # Only updates count if provided a valid guess
    # (we are not penalizing for a not-real guess, but we could if we wanted to)
    guesses_count += 1
    
    # Determines if they found the number or not
    if user_guess < secret_number:
        print("Too small!")
    elif user_guess > secret_number:
        print("Too large!")
    else:
        print(f"You have found the number! You guessed {guesses_count} times!")
        break
else:
    print(f"Ran out of guesses! The correct answer was {secret_number}")
```


----------

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

