# Queues

Queues are considered First In First Out type data structures (FIFO).
They work like, well, queues work when you are in line at some place.
The first person to show up gets served first.

We can also make this data structure with the previous node structure, BUT, instead
we are going to use python's built in list (because it is more fun this way)!


```python
class Queue:
    def __init__(self):
        self.que = []
    
    def size(self):
        return len(self.que)
    
    def enqueue(self, value):
        self.que.insert(0, value) # Inserts at front 0
    
    def dequeue(self):
        return self.que.pop(self.size() - 1) # Removes from the end of the list

    def front(self):
        return self.que[self.size() - 1]

    
q = Queue()

q.enqueue('dog')
q.enqueue('cat')
q.enqueue('chicken')

init_size = q.size()
for x in range(init_size):
    print(f'Place in line [{x + 1}]: {q.dequeue()}')
```

There are plenty of situations to utilize queues. Anytime
we need to maintain order of the values we are using, queues are what you use.

Whether that be maintaining traffic to your website, or keeping track of variables to be reorganized in some way, queues are an option.


# Specialized Queues

Now this could be said for any data type, but there are specializations for queues as well:

> Priority Queues: Some values are bumped up into a higher place in the queue as they need to be dequeued sooner than other things

> Doubled ended queues: just as they sound, these are queues which both enqueue and dequeue from both ends 

This kinda gets into the more over arching idea of specialized data structures which are created exclusively for your problems

# Efficiency
When we are speaking of the effieciency of doing tasks like finding if an item is in the queue, it does take some time, and worst case scenario, it take going through the entire queue to find the item.

Otherwise, queues are very efficient in adding and removing items as there is usually a direct reference to the both the front and back and they can be instantly accessed (best and worst case).

The same can be said for stacks, as you have instant access to the the top of the stack for adding and removing items, but searching through the stack for locating something may require going through the ENTIRE stack.

So, if we wanted a data structure that was quicker to look through for data, what are we to do?

USE A TREE (Probably, maybe)
