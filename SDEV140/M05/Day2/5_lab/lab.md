from functools import reducefrom functools import reduce

# Lab

----------

taken as number 9 from chapter 6

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


