# InOrder traversal
# For traversing a (non-empty) binary tree in an inorder fashion, we must do these three things for every node n starting from the tree’s root:
# (L) Recursively traverse its left subtree. When this step is finished, we are back at n again.
# (N) Process n itself.
# (R) Recursively traverse its right subtree. When this step is finished, we are back at n again.

from node import Node
from collections import deque

def inOrderRecursive(root: Node) -> None:
    if not root:
        return None
    # Process left subtree
    inOrderRecursive(root.left)
    # Process root itself
    print(root.val, end=' ')
    # Process right subtree
    inOrderRecursive(root.right)

def inorderIterative(root):
    # create an empty stack
    stack = deque()
    # start from the root node (set current node to the root node)
    curr = root 
    # if the current node is None and the stack is also empty, we are done
    while stack or curr:
        # if the current node exists, push it into the stack (defer it)
        # and move to its left child
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            # otherwise, if the current node is None, pop an element from the stack,
            # print it, and finally set the current node to its right child
            curr = stack.pop()
            print(curr.val, end=' ')
            curr = curr.right


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
    inOrderRecursive(root)
    print('\n')
    # Iterative
    inorderIterative(root)