# Binary Search Tree

Binary search trees are just like the trees that we defined before, BUT with some rules:

- each node only has 2 pointers (a left and a right pointer)
- every value on the left of the current node is LESS THAN the value of the current node
- every value on the right of the current node is GREATER THAN the value of the current node


---- 

Following these rules allow a few things:

- the tree will 'sort' itself (if you go inorder, which we will get to)
- GUARANTEES O(log N) search time (if tree is balanced). Is O(N) in worst case scenario.
- Also GUARANTEES a O(h) insert time, h being the height of the tree. For a balanced tree, the height will be log N.

# Show example of inserting list of values into the tree:

Here is a list of items [9, 2, 6, 1, 7, 3, 12, 84, 14, 10, 0]

```
            9
       /         \
      2          12
    /   \       /  \
   1     6     10   84
  /     / \         /
 0     3   7       14
```

# "Search" for a value. Show how the inherit structure of the tree itself means you can find things quicker compared to something like an array. ALSO, the tree grows dynamically!!!!

Each one gets puts in their spot one by one. This does mean if we try to place a sorted list, it ends up ruining our
structure entirely.

Here is the list of items we want to insert this time: [5, 8, 12, 63, 100, 124, 654]

Here is the resulting binary search tree:
```
5
 \
  8
   \
    12
     \
      63
       \
        100
         \
          124
            \ 
             654
```

We have essentially created a fancy linked list.... and we lost the efficiency of both searching and inserting as it is now
O(N) to walk through this line of items.

THIS IS WHY WE WANT TO TRY AND MAKE OUR TREES BALANCED

# What is a balanced tree:

For all nodes, the left and and right subtree's height differ by at most 1 node.

Here is a [Balanced Example](https://stackoverflow.com/questions/8015630/definition-of-a-balanced-tree)

THIS IS BALANCED:
```
     A
   /   \
  B     C  
 /     / \  
D     E   F  
     /  
    G  
```

THIS IS UNBALANCED
```
     A
   /   \
  B     C   <-- difference = 2
 /     /
D     E  
     /  
    G 
```

# Rotations (we are not getting super deep into them!!)

To balance a list, you simply make some rotations (depending on the situation) as time goes on.

Depending on the type of tree you are using, these rotations are done at different points.

See [AVL trees and Red Black Trees](https://www.geeksforgeeks.org/balanced-binary-tree/)

Regardless of the case, they result in a slight overhead when inserting, but results in a tree with assured 
O(log N) time


---

# Actual Code (non balancing tree)

Here is an [implementation](https://medium.com/the-modern-scientist/understanding-binary-search-trees-in-python-f49a5b7901e0):

```python

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        else:
            if key < node.key:
                node.left = self._insert(node.left, key)
            else:
                node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self._get_min_value(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        return node

    def _get_min_value(self, node):
        while node.left is not None:
            node = node.left
        return node

    def inorder_traversal(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node is not None:
            self._inorder_traversal(node.left)
            print(node.key, end=" ")
            self._inorder_traversal(node.right)
```