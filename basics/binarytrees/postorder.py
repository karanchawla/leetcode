# Post-order tree traversal
# For traversing a tree in post-order fashion, we must do three things for every node `n` starting from tree's root node
# 1. Recursively traverse it's left subtree. When this step is finished, we are back at `n` again
# 2. Recursively traverse it's right subtree. When this step is finished, we are back at `n` again.
# 3. Process `n` itself.
from node import Node
from collections import deque

def postOrderRecursive(root: Node) -> None:
    if root is None:
        return
    
    # Traverse left subtree
    postOrderRecursive(root.left)

    # Traverse right subtree
    postOrderRecursive(root.right)

    # Process node itself
    print(root.val, end=' ')


def postOrderIterative(root: Node) -> None:
    if root is None:
        return
    
    stack = deque()
    stack.append(root)

    # Create another stack to store post-order traversal
    output = deque()

    while stack:
        node = stack.pop()
        output.append(node.val)

        if node.left:
            stack.append(node.left)
        
        if node.right:
            stack.append(node.right)
    
    while output:
        print(output.pop(), end=' ')

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
    postOrderRecursive(root)
    
    print('\n')
    
    # Iterative
    postOrderIterative(root)