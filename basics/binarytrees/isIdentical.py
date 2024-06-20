# Problem description
# Check if 2 binary trees are identical
# Write an efficient algorithm to check if two binary trees are identical or not. Two binary trees are identical if they have identical structure and their contents are also the same.

from collections import deque
from node import Node

# Recursive solution
def isIdenticalRecursive(x: Node, y: Node) -> bool:
    # If both trees are empty return True
    if not x and not y:
        return True
    
    return (x is not None and y is not None and x.val == y.val and \
            isIdenticalRecursive(x.left, y.left) and isIdenticalRecursive(x.right, y.right))


# Iterative solution
# Use a stack similar to the implicit recursive stack
def isIdenticalIterative(x: Node, y: Node) -> bool:
    # If both trees are empty return True
    if not x and not y:
        return True
    
    # If one of them is empty return False
    if (not x and y) or (x and not y):
        return False

    stack = deque()
    stack.append((x, y))

    while stack:
        # Pop the top pair and compare their values
        x, y = stack.pop()

        if x.val != y.val:
            return False
            
        # if the left subtree of both x and y exists, push their addresses
        # to stack; otherwise, return false if only one left child exists
        if x.left and y.left:
            stack.append((x.left, y.left))
        elif x.left or y.left:
            return False
        
        if x.right and y.right:
            stack.append((x.right, y.right))
        elif x.right or y.right:
            return False
    
    return True


if __name__ == '__main__':
 
    # construct the first tree
    x = Node(15)
    x.left = Node(10)
    x.right = Node(20)
    x.left.left = Node(8)
    x.left.right = Node(12)
    x.right.left = Node(16)
    x.right.right = Node(25)
 
    # construct the second tree
    y = Node(15)
    y.left = Node(10)
    y.right = Node(20)
    y.left.left = Node(8)
    y.left.right = Node(12)
    y.right.left = Node(16)
    y.right.right = Node(25)
 
    if isIdenticalRecursive(x, y):
        print('Recursive: The given binary trees are identical')
    else:
        print('Recursive: The given binary trees are not identical')
    
    if isIdenticalIterative(x, y):
        print('Iterative: The given binary trees are identical')
    else:
        print('Iterative: The given binary trees are not identical')
 