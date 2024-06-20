# Calculate the height of a binary tree
# Write an efficient algorithm to compute the binary tree’s height. The height or depth of a binary tree is the total number of nodes on the longest path from the root node to the leaf node.

from node import Node
from collections import deque

def height(node: Node) -> int:
    height = 0
    if not node:
        return height

    queue = deque()
    queue.append((node, 1))

    while queue:
        curr, level = queue.popleft()
        if curr.left:
            queue.append((curr.left, level + 1))
        if curr.right:
            queue.append((curr.right, level + 1))
        height = max(height, level)

    return height

if __name__ == '__main__':
 
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)

    print(height(root))