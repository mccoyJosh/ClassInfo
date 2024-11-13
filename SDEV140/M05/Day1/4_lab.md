# Lab

-----

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