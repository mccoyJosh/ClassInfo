# Sorting Data

# Why

Sorting data is not only important because it makes our data more digestible for us humans, but also gives
the computer what it needs to solve a variety of problems dealing with sets of data:

- allows for quicker searching of data i.e. binary searching
- easily find the median (middle value)
- more easily find the mode (only needs to record current highest count and what it is and not all counts)
- can be sorted by shared group to group common fields together.

# How

We have previously discussed sorting data already.
We are going to properly look at the bubble sort algorithm. 
It is pretty simple compared to other ones.

The bubble sort algoritm relies on SWAPPING.

SWAPPING is the act of replacing the 2 variables with the other one's values, i.e. swapping their values.

Since we don't want to create a whole new array for sorting, we just swap the values currently existing in our array


### BRIEFLY show how to swap

```not_python
def swap(*int var1, *int var2):
    int temp = *var1
    *var1 = *var2
    *var2 = *var1 
```

# Properly Showing Bubble Sort

## Example:

Per book:
> **Bubble Sort**: a sorting algorithm in which list elements are arranged in ascending or descending order by comparing items in pairs and swapping them when they are out of order.

With each pass of the list being sorted, the smallest values will rise to the top (front) of the list **LIKE BUBBLES**, and the
largest values will sink to the bottom (end) of the list like INVERTED BUBBLES!

Here is a visualization to show off this.

https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/visualize/

## Psuedocode:

So, with this in mind, how do we actually code it?

> ALSO, HOW DO WE DEAL WITH DATA OF VARIABLE SIZE?????

![bubble_sort_de_book.png](assets/bubble_sort_de_book.png)

This is an inefficient algorithm already, but this particular code is inefficient in a few
areas already!

## Python:

Here is a similar piece of code but in python;
example taken from https://www.geeksforgeeks.org/python/python-program-for-bubble-sort/

```python
def bubble_sort(arr):
  
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):
        
        # Initialize swapped to track if any swaps occur
        swapped = False  

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:
              
                # Swap elements if they are in the wrong order
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                
                # Mark that a swap has occurred
                swapped = True
        
        # If no swaps occurred, the list is already sorted
        if not swapped:
            break


# Sample list to be sorted
arr = [6,6,2]
print("Unsorted list is:")
print(arr)

bubble_sort(arr)

print("Sorted list is:")
print(arr)
```


## Ascending VS Descending (show descending example)

Per the book:
> **Ascending Order**: describes the arrangement of data items from the lowest value to highest.

> **Descending Order** : describes the arrangement of data items from the highest value to lowest.

Changing the code to be an ascending vs descending order is as easy as changing the boolean check in the code.
For example, in the psuedocode, you would just need to change 
```scores[x] > scores[x + 1]?```
to
```scores[x] < scores[x + 1]?```

This just makes it do the swap in the opposite order!

TRY THIS WITH THE PYTHON PIECE OF CODE!

# Other Sorting Algorithms

Here is a website which shows off other sorting algorithms along with the one we saw today. We can see
how some of these are faster than others.

https://www.sortvisualizer.com/bubblesort/

