# Lab

-------

## Alternative Sorting Algo (especially if missed in monday's lecture)

Hypothetically, if you need to sort values and get top 3 numbers, this is one solution to doing so!

```python
numbers = [9, 4, 1, 10, 0, 2, 3, 7, 5, 2]
print(f"Original List: {numbers}")

# This will go from highest to lowest
sorted_list = []

# Goes through OG list
for new_number_to_add in numbers:
    # If it doesn't find a number it is smaller than, it is put at the end of the line
    append_index = len(sorted_list)
    
    # Goes through current "sorted list"
    for index, current_number_in_sorted_list in enumerate(sorted_list):
        # If it finds a number it is greater than, it inserts itself before it
        if new_number_to_add >= current_number_in_sorted_list:
            append_index = index
            break
    
    # Inserts the new number regardless of what happens! 
    sorted_list.insert(append_index, new_number_to_add)

# Prints out result
print(f"Sorted List:   {sorted_list}")
print(f"#1: {sorted_list[0]}")
print(f"#2: {sorted_list[1]}")
print(f"#3: {sorted_list[2]}")
```

If you were perhaps doing this with the values associated with numbers in a dictionary, you would simply store
the keys in your 'sorted list' and when you do the >= comparison, you just grab the associated values
from the dictionary using these keys.


-------

## Mixing

> Make code to mix the colors red, blue, and yellow together and output their result... USING FUNCTIONS

With the knowledge of functions, we can now implement a slightly more nicer-to-look at piece of code
for this previous problem

```python
def main():
    print('Welcome to the primary color mixer!')
    color_1 = get_color()
    color_2 = get_color()
    
    colors = (color_1, color_2)
    result = ''
    if color_1 == color_2:
        result = color_1
    elif "red" in colors and "blue" in colors:
        result = "purple"
    elif "red" in colors and "yellow" in colors:
        result = "orange"
    elif "blue" in colors and "yellow" in colors:
        result = "green"
    
    print(f"{color_1} and {color_2} make {result}")
    
    
def get_color():
    colors = ('red', 'blue', 'yellow')
    while True:
        color = input("Enter a primary color: ").lower()
        if color in colors:
            return color
        else:
            print("Invalid color! Please input either red, blue or yellow")

if __name__ == "__main__":
    main()
```


--------

--------

## Text Analysis

> Read file, print out most common word and letter and give user ability to see how many times any word appears


```python
import re

def main():
    text = get_text('assets/words.txt')
    words = count_words(text)
    chars = count_chars(text)
    print(f"Most common word: '{find_largest_key_in_dictionary(words)}'")
    print(f"Most common character: '{find_largest_key_in_dictionary(chars)}'")
    print("Please enter your queries like so to indicate whether you want to search for character or word: c c     OR       w word")
    while True:
        user_input = input("Enter the word (w) or character (c) you would like the count of: ")
        user_input = user_input.lower().split()
        mode = user_input[0]
        key = user_input[1]
        if mode == 'w':
            print_count(words, key)
        else:
            print_count(chars, key)



def get_text(filename):
    f = open(filename, 'r')
    text = f.read()
    f.close()
    return text


def count_words(text):
    words = {}
    words_list = re.split('[^a-zA-Z]', text)
    for w in words_list:
        w = w.lower()
        if w == '':
            continue
        elif w in words:
            words[w] = words[w] + 1
        else:
            words[w] = 1
    return words


def count_chars(text):
    characters = {}
    for char in text:
        if char in characters:
            characters[char] = characters[char] + 1
        else:
            characters[char] = 1
    return characters

def find_largest_key_in_dictionary(dictionary):
    if len(dictionary) == 0:
        return ''
    else:
        largest = 0
        largest_key = ''
        for k, v in dictionary.items():
            if v > largest:
                largest = v
                largest_key = k
        return largest_key

def print_count(dict, key):
    if key in dict:
        print(f"Count: {dict[key]}")
    else:
        print('Not found')


if __name__ == "__main__":
    main()
```


-----------------


## Average Number

> Write a program that computes and prints the average of the numbers in a text file. You should make use of two higher order functions to simplify the design


```python
from functools import reduce

def convert_to_int(num_str):
    try:
        return int(num_str)
    except ValueError:
        print(f'Could not read number: {num_str}')
        return 0

def put_file_contents_within_list(filename):
    f = open(filename, 'r')
    li = []
    for line in f:
        li.append(line)
    f.close()
    return li
    

def main():
    numbers = put_file_contents_within_list('assets/numbers.txt')
    size = len(numbers)
    numbers = map(convert_to_int, numbers)
    total = reduce(lambda x, y : x + y, numbers)
    print(f"Average: {total/size}")


if __name__ == "__main__":
    main()
```


----------------------


# Sorting Time (Better Sorting :) (AKA QUICK SORT) )

Previously we discussed a bad sorting algorithm which was very simple but also very in-efficient.

Today, we make a better sorting algorithm.

Good visualization of quick sort (their algorithm is a bit different but same idea persists):
https://www.hackerearth.com/practice/algorithms/sorting/quick-sort/visualize/

```python
# Obviously where the partitioning takes place
def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # Moves high value down until it is less than pivot value (OR PASSES LOW VALUE)
        while low <= high and array[high] >= pivot:
            high = high - 1
        # Moves low value up until it is greater than pivot value (OR PASSES HIGH VALUE)
        while low <= high and array[low] <= pivot:
            low = low + 1
        # If they didn't cross, they swap
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            # EXITS otherwise
            break
    
    # Swaps pivot value into proper final position
    array[start], array[high] = array[high], array[start]

    return high

# Recursive quicksort method
def quick_sort_rec(array, low, high):
    if low < high:
        # Does partition to current range
        pi = partition(array, low, high)
        # Fixes left of pivot element
        quick_sort_rec(array, low, pi - 1)
        # Fixes right of pivot element
        quick_sort_rec(array, pi + 1, high)

# Helper method
def quick_sort(array):
    quick_sort_rec(array, 0, len(array) - 1)


data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

quick_sort(data)

print('Sorted Array in Ascending Order:')
print(data)
```