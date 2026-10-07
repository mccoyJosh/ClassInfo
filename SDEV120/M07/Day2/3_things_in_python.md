# Arrays (to make your list of numbers) 

So, the way we explained arrays earlier is how arrays work in MOST
programming languages.
Some of these rules are NOT the same in python!

The background in python, the list data types are known as dynamic arrays!
These are arrays which can change in size...

Here is how you do it:

- show off list
  - mutable
  - CAN increase size of list... so not really an array
  - does allow multiple types, so, again, different
  - initialized and accessed the same tho

### ALSO, go through 3_x05_lists.md, like, not terribly in depth but an overview


# For Loops with Arrays

- show off for loop walking through each value in array
- maybe do example adding up each value
- maybe do example looking for a specific value
- walk through loop determining if each value meets some sort of qualification, perhaps being POSITIVE/NEGATIVE

Iterate through list with for loop and using in keyword to check if variable is inside of list
ALSO just like a string, you can use the 'in' keyword to iterate through a list with a for loop
AND check if an item is in a list

```python
list_1 = [100, 200, 300, 400, 455, 555, 123, "last"]
for i in list_1:
    print(i)
    print("Is 500 in list_1:", 500 in list_1)
```