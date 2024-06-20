# Level Order Traversal
# This it the breadth first search for binary trees where all the nodes at each level are process before moving to the next level deeper 
# in the tree

from node import Node
from collections import deque

def levelOrderTraversal(root: Node) -> None:
    if not root:
        return
    
    queue = deque()
    queue.append(root)

    while queue:
        curr = queue.popleft()
        print(curr.val, end=' ')

        if curr.left:
            queue.append(curr.left)
        
        if curr.right:
            queue.append(curr.right)

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

    # Level order traversal
    levelOrderTraversal(root)