# Delete a Binary Tree
# Given a binary tree, write an efficient algorithm to delete the entire binary tree. The algorithm should deallocate every single node present in the tree, not just change the root node’s reference to null.

# Recursive solution
# Perform post-order traversal and delete the left and right subtree of each node, before deleting the node itself
from node import Node

def deleteBinaryTree(root: Node) -> None:
    if not root:
        return None
    
    # Delete left subtree
    deleteBinaryTree(root.left)

    # Delete right subtree
    deleteBinaryTree(root.right)

    # Delete node itself
    root.left = None
    root.right = None
    root = None

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

    # Delete tree
    root = deleteBinaryTree(root)
    print(root)