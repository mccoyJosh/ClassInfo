
## Arrays

Now, technically, we don't have arrays in python.
We do have tuples which are similar, but not exactly. 

How they work:
creates allocated space for a specific type of object. Whether that be an integer, string, or a CLASS that we made.

Whenever we ask for a value from the array, what we are doing is asking for the value at the address of that beginning 
of the array and have it offset by a particular index (this is why indices for data structures often start at 0, as the
offset of the first index is just at the given address, thus, an offset of 0). So something like arrray[1] would get the address
of the beginning of the array first, then get the value 1 unit forward, which is the second item in the array. It determines this unit based off of the size of the object store in the array. So, a 64 integer would be closer together when compared to something like a string.



Once they are made though, we cannot add on more space.
The computer has probably already added more information in the address next to it anyways.


If we wanted to make an array which grows in size, it would require us to make a class which detects when an
array is about to hit its limit, and if it is, create a new array with more space and copy the pre-existing
data into the new array. This is not only tedious, but can be slow if there is a LOT of pre-existing data.

So, how can we quickly add data to a structure, let it grow in size (be dynamic), and also be addressed like an array (indices) ---> a linked list
