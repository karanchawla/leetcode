# Preorder traversal
# For traversing a binary tree in preorder fashion, we must do three things for each node `n`:
# 1. Process `n` itself.
# 2. Recursively traverse left subtree. When this step is finished, we are back at `n`.
# 3. Recursively traverse right subtree. When this step is finished, we are back at `n`.

from node import Node
from collections import deque

def preOrderRecursive(node: Node) -> None:
    if not node:
        return
    
    print(node.val, end=' ')

    # Process left subtree
    preOrderRecursive(node.left)
    
    # Process right subtree
    preOrderRecursive(node.right)


def preOrderIterative(node: Node) -> None:
    if not node:
        return
    
    stack = deque()
    stack.append(node)

    while stack:
        curr = stack.pop()
        print(curr.val, end=' ')

        # If right node
        if curr.right:
            stack.append(curr.right)
        
        # If left node
        if curr.left:
            stack.append(curr.left)

if __name__ == '__main__':
 
    ''' Construct the following tree
               1
             /   \
            /     \
           2       3
          /      /   \
         /      /     \
        4      5       6
              / \
             /   \
            7     8
    '''
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    
    # Recursive
    preOrderRecursive(root)
    
    print('\n')
    
    # Iterative
    preOrderIterative(root)