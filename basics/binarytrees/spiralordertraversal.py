# Spiral order traversal
# Given a binary tree, print its nodes level by level in spiral order
# Odd levels should be printed from left to right, and even levels should be printed from right to left or vice versa.

from node import Node
from collections import deque

def spiralOrderTraversal(root: Node) -> None:
    if not root:
        return
    
    queue = deque()
    queue.append(root)
    flag = True

    while queue:
        # calculate the total number of nodes at the current level
        nodeCount = len(queue)
 
        # print left to right
        if flag:
            while nodeCount > 0:
                # pop from the front if `flag` is true
                curr = queue.popleft()
                print(curr.val, end=' ')
 
                if curr.left:
                    queue.append(curr.left)
 
                if curr.right:
                    queue.append(curr.right)
 
                nodeCount = nodeCount - 1
 
        # print right to left
        else:
            while nodeCount > 0:
                # it is important to pop from the back
                curr = queue.pop()
                print(curr.val, end=' ')
 
                if curr.right:
                    queue.appendleft(curr.right)
 
                if curr.left:
                    queue.appendleft(curr.left)
 
                nodeCount = nodeCount - 1
 
        # flip the flag for the next level
        flag = not flag
        print()



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
    
    
    spiralOrderTraversal(root)