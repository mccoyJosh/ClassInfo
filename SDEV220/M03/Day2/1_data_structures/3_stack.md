# Stack

Another simple data structure is the Stack! 
This one works like, well, a stack.

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