# Stack

Another simple data structure is the Stack! 
This one works like, well, a stack.

This data structure considered "Last In First Out" aka "LIFO".
This just means that whatever was the last thing placed on the stack is the next thing to be retrieved.

This is an essential data structure and is used everywhere! (Thing of recursive calls -> creates stack of method calls).

Anytime a previous "state" or reference points needs to be recorded, a stack is a good idea to use!

```python

class Node:
    def __init__(self, value):
        self.value = value
        self.ptr : 'Node' = None



class Stack:
    def __init__(self):
        self.size = 0
        self.top : Node = None

    def push(self, value):
        new_node = Node(value)
        new_node.ptr = self.top
        self.top = new_node
        self.size += 1
    
    def pop(self):
        if self.size <= 0:
            print("ERROR: ATTEMPTED TO POP VALUE FROM EMPTY STACK")
        value = self.top_value()
        self.top = self.top.ptr
        self.size -= 1
        return value
        

    def top_value(self):
        if self.size <= 0:
            print("ERROR: ATTEMPTED TO GET VALUE FROM EMPTY STACK")
        return self.top.value


st = Stack()
st.push(88)
st.push(66)
st.push(22)

print(f'Top value: {st.top_value()}\n')

for _ in range(st.size):
    print(st.pop())
```



ALSO, note you could just easily represent a stack using a list or linked list.

Data structures can be built using other data structures if need be, but it is typically better off if you build them with simpler
structures.

