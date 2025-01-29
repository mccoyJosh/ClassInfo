# Nodes

Before we can really talk about linked lists, we first need to talk about nodes.

> Simply put, a node is an object which has some sort of value, and TYPICALLY a pointer(s) to other node(s).

These are essential when understanding any advanced data structure.
Here is a simple node:

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.ptr : 'Node' = None
```

In this piece of code, the `self.value` is the value which is stored in this class.

The `self.ptr` is a pointer variable to another Node object. Initially, it is None as there is nothing to point to initially.
Depending on the data structure you are dealing with, the pointer will be utilized in different ways. In this
node we have a single pointer, but there are other Node varieties with more pointers (which we shall see later).

> NOTE: Sometimes, the node class for a data structure may be defined within the data structure class itself; this is merely ones preference though.


# Linked List
The first data structure we are going to talk about (which uses the above Node class) is a Linked List

- Why is it is good 
  - can grow in size
  - Is indexed list so things can be retrieved reliably from said locations
  - Simple to understand
- Why bad
  - SLOW TO GET INFORMATION and add information. For instance, in this currently implementation, you HAVE to walk though the entire list to get to the last index. If the list was ridiculously long, this could take a while.
  - There are ways to improve this implementation:
    - Add another pointer inside the Node class to the previous node instead of ONLY the next node
    - Add more pointers to the linked list class other than the head, such as TAIL, and MID, which would give us quicker access to the end, and middle of the linked list

```python

class Node:
    def __init__(self, value):
        self.value = value
        self.ptr : 'Node' = None



class LinkedList:

    def __init__(self):
        self.size = 0
        self.head : Node = None

    def push_value(self, value):
        self.insert_value(value, self.size)
    
    def pop_value(self):
        self.delete_value(self.size - 1)
        
    def top_value(self):
        return self.get_value(self.size-1)


    def insert_value(self, value, index):
        if index < 0 or index > self.size:
            print("ERROR: ATTEMPTED TO INSERT OUTSIDE OF RANGE")
            return
        new_node = Node(value)

        if index == 0:
            new_node.ptr = self.head
            self.head = new_node
        else:
            node_ref = self.head
            for _ in range(index-1):
                node_ref = node_ref.ptr
            if index != self.size:
                new_node.ptr = node_ref.ptr
            node_ref.ptr = new_node
        self.size += 1
    
    def delete_value(self, index):
        if index < 0 or index >= self.size:
            print("ERROR: ATTEMPTED TO DELETE OUTSIDE OF RANGE")
            return
        if index == 0:
            temp_node = self.head.ptr
            self.head.ptr = None # technically not necessary
            self.head = temp_node
        else:
            node_ref = self.head
            for _ in range(index-1):
                node_ref = node_ref.ptr
            temp_node = node_ref.ptr
            node_ref.ptr = node_ref.ptr.ptr
            temp_node.ptr = None # technically not necessary
        self.size -= 1
        
    
    def get_value(self, index):
        if index < 0 or index >= self.size:
            print("ERROR: ATTEMPTED TO GET OUTSIDE OF RANGE")
            return None
        node_ref = self.head
        for _ in range(index):
            node_ref = node_ref.ptr
        return node_ref.value

    def print_list(self):
        print(f'Size: {self.size}')
        for i in range(self.size):
            print(f"\tIndex {i}: {self.get_value(i)}")

li = LinkedList()
li.push_value(100)
li.push_value(900)
li.push_value(888)
li.push_value(124)
li.insert_value(532, 1)

li.print_list()

print('___________________')

li.delete_value(2)

li.print_list()
```


By using a linked list, we now have a dynamic data structure which can grow in size as much as we need.

Instead of being limited to the initial space initialized by an array, we create more space with nodes which
just take up the next available memory slot. This does cost the price of losing INSTANT access to every index (as we now
HAVE to travel through nodes to find the next, and next, and next nodes). 