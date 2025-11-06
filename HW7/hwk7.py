# Name:  - Olohi
# Peers:  - ``N/A'' 
# References:  - URL of resources used <br>
from collections import deque # type: ignore

# Assumption: A BST has no duplicates 
# Assumption/Challenge 2: 
    # I'm unsure as to whether to return True or False if removing an element from a single-element tree.
    # This is because we do not return the new root and to print the contents of the tree, using inOrder we'll need to pass in a root
    # So I've just always passed in the previous root, which works well for cases where we didn't have to update the root
    # It also works well for cases where we updated the root with the data of a descendant node
    # But we CAN'T do this if the root is the only element of the tree
    # As such, I just set root to root.left which is essentially None
    # If I could return the new root, I'd just return root.left which is same as deleting the Tree, so I assume I can adapt this code that way
    # And return True even when the node to remove is the only element in the tree


#### DO NOT EDIT - START ####
def POL_helper():
    print("File Imported")

class BTNode:
    def __init__(self, data:int):
        self.left:BTNode|None = None
        self.right:BTNode|None = None
        self.data:int = data
#### DO NOT EDIT - END ####

# Part 1: Traversal
def inOrderWalk(root:BTNode|None) -> list[int]|None:
    """
    Returns a list of the nodes in a tree in in-order

    @param root: (BTNode|None) the root of the tree
    @return: (list|None) the list of nodes in the tree in in-order

    >>> some_node:BTNode = BTNode(2)
    >>> some_node.left = BTNode(1)
    >>> some_node.right = BTNode(3)
    >>> inOrderWalk(some_node)
    [1,2,3]
    """
   
    # checks if the tree is empty and returns None if it is
    if not root:
        return None
    # call the function on the left child of root
    left:list[int]|None = inOrderWalk(root.left)
    # enqueue the root's data
    array:list[int] = [root.data]
    # call the function on the right child of the root
    right:list[int]|None = inOrderWalk(root.right)
    # avoiad list concatenation with None by setting None returns to an empty list
    if left is None:
        left = []
    if right is None:
        right = []
    return left + array + right


# Part 2: LT2BST    
def listToTree(tree_as_list:list[int]) -> BTNode|None:
    """
    Converts a list to a BST

    @param tree_as_list: (list) a list of integers to convert to a tree
    @return root: (BTNode|None) the root of the created tree or None if an empty tree is passed

    >>> listToTree([1,2,3]).data
    2
    """
    # base case: list is empty
    if tree_as_list == []:
        return None
    # slice the list into two parts:
    # left = the part before the middle node; right = the part after the middle node
    mid:int = len(tree_as_list)//2
    left:list[int] = tree_as_list[:mid]
    right:list[int] = tree_as_list[mid+1:]
    # create a tree node for the middle element
    root:BTNode = BTNode(tree_as_list[mid])
    root.left = listToTree(left)
    root.right = listToTree(right)
    return root


# Part 3: BT2BST
def fixTree(root:BTNode|None) -> BTNode|None:
    """
    Coverts a binary tree to a BST with minimum height
    
    @param root: (BTNode) the root of the binary tree
    @return new_root: (BTNode|None) the root of the created BST or None if an empty tree is passed

    >>> some_node:BTNode = BTNode(1)
    >>> some_node.left = BTNode(2)
    >>> some_node.right = BTNode(3)
    >>> fixTree(some_node).data 
    2  
    """
    if root is None:
        return 
    # populate the data of nodes of the tree in a list 
    list_version:list[int] = inOrderWalk(root) # type: ignore
    # sort the list
    list_version.sort()
    # call listToTree on the list to convert it to a BST
    new_root:BTNode|None = listToTree(list_version)
    return new_root


# Part 4: addNodeBST
def addNodeBST(root:BTNode|None, data:int) -> bool:
    """
    Adds a new node with value, data, if data not in BST already, to a BST

    @param root: (BTNode) the root of the BST
    @param data: (int) the value of the node to be added
    @return: (bool) T or F to show the success of the operation

    >>> some_node:BTNode = BTNode(2)
    >>> some_node.left = BTNode(1)
    >>> some_node.right = BTNode(3)
    >>> addNodeBST(some_node, 4)
    True
    >>> addNodeBST(some_node, 3)
    False
    """
    # return False if tree is empty
    if root is None:
        return False
    # traverse the left subtree if data is less than data stored by current root
    if data < root.data:
        if not root.left:
            root.left = BTNode(data)
            return True
        return addNodeBST(root.left, data)
        # traverse the right subtree if data is greater than data stored by current tree
    elif data > root.data:
        if not root.right:
            root.right = BTNode(data)
            return True
        return addNodeBST(root.right, data)
    return False

# Part 5: removeNodeBST
def removeNodeBST(root:BTNode|None, data:int) -> bool:
    """
    Removes a node, containing element, data, from a BST

    @param root: (BTNode) the root of the BST
    @param data: (int) the data of the element to be removed from the BST
    @return True or False: (bool) True indicates successful removal and False indicates otherwise

    >>> some_node:BTNode = BTNode(2)
    >>> some_node.left = BTNode(1)
    >>> some_node.right = BTNode(3)
    >>> removeNodeBST(some_node)
    True
    """
    # if root is None, return False
    if not root:
        return False
    
    ## Data is the right or left node of the current root
    # if root.left.data is data, update root.left's pointer to root.left.left
    if root.left and root.left.data == data:
        remove:BTNode = root.left
        ## Flawed: no longer flawed
        if not remove.right:
            root.left = root.left.left
            return True
        else:
            # store the left and right nodes of the element to be removed
            left = remove.left
            right = remove.right
            # get the node to replace remove with
            next_biggest = getNextBig(remove)
            # update root.left's pointer to the replacement
            root.left = next_biggest
            # set next_biggest.left to the previous left of the removed node
            next_biggest.left = left
            # set next_biggest.right to the previous right of removed node if next_biggest is not equal to right
            if next_biggest != right:
                while next_biggest.right:
                    next_biggest = next_biggest.right
                next_biggest.right = right
            return True

    # if root.right.data is data, update root.right's pointer to the leftmost node of root.right
    if root.right and root.right.data == data:
        remove:BTNode = root.right
        if not remove.right:
            root.right = root.right.left
            return True
        else:
            # store the left and right nodes of the element to be removed
            left = remove.left 
            right = remove.right
            # get the node to replace remove with
            next_biggest:BTNode = getNextBig(remove) # assured next_biggest!=None because it has a right subtree to get to this point
            # update root.right's pointer to the replacement 
            root.right = next_biggest
            # set next_biggest.left to the previous left of the removed node
            next_biggest.left = left 
            # set next_biggest.right to previous right of removed node if next_biggest is not equal to right
            if next_biggest != right:
                while next_biggest.right:
                    next_biggest = next_biggest.right
                next_biggest.right = right
            return True

    # Data is less than the current node
    if data < root.data:
        return removeNodeBST(root.left, data)
    
    # Data is more than the current node
    elif data > root.data:
        return removeNodeBST(root.right, data)
    
    # Data is the value of the current node (node must be the overall root of the tree)
    elif data == root.data:
        # if root has no right node, update the root pointer to its left node, which could be None
        if not root.right:
            root = root.left
            return True
        # if root has a right node
        else: 
            # store the element to be removed, root, its left and right nodes 
            remove = root
            left = remove.left
            right = remove.right
            # get the node to replace remove with
            next_biggest = getNextBig(remove)
            # update root to the replacement
            root.data = next_biggest.data
            """
            # set next_biggest.left to the previous left of the removed node
            next_biggest.left = left
            # set next_biggest.right to previous right of removed node if next_biggest is not equal to right
            if next_biggest != right:
                while next_biggest.right:
                    next_biggest = next_biggest.right
                next_biggest.right = right
            return True"""


    return False
            
def getNextBig(node:BTNode)->BTNode:
    """
    Returns the smallest element greater than node in the BST
    
    @param node: (BTNode) a node in the BST
    @return current: (BTNode) the smallest node greater than node in the BST

    >>> some_node:BTNode = BTNode(2)
    >>> some_node.left = BTNode(1)
    >>> some_node.right = BTNode(3)
    >>> getNextBig(some_node)
    3
    """
    # can return None if node is a leaf node
    # gets the next biggest node to node, which corresponds to the leftmost of node's right node
    current:BTNode = node.right #type: ignore
    while current and current.left:
        if not current.left.left:
            temp = current.left
            current.left = None
            current = temp
            break
        current = current.left
    return current



# Part 6: isBalance
def isBalanced(root:BTNode|None) -> bool:  
    """
    Checks if a binary tree is balanced

    @param root: (BTNode) the root of the tree
    @return True or False: (int) whether the tree is balanced or not

    >>> some_node:BTNode = BTNode(2)
    >>> some_node.left = BTNode(1)
    >>> some_node.right = BTNode(3)
    >>> isBalanced(some_node)
    True
    """
    # returns True if the tree is empty: an empty tree is balanced
    if not root:
        return True
    # gets the height of the left and right subtrees connected to the root of the tree
    left_height:int = getHeight(root.left)
    right_height:int = getHeight(root.right)
    # returns False if the difference in height is > 2, else returns True
    return abs(right_height - left_height) < 2

# Helper function for isBalance
def getHeight(root:BTNode|None) -> int:
    """
    Calculates the height of a binary tree
    
    @param root: (BTNode) the root of the tree
    @return: (int) the height of the tree starting at root

    >>> some_node:BTNode = BTNode(2)
    >>> some_node.left = BTNode(1)
    >>> some_node.right = BTNode(3)
    >>> getHeight(some_node) 
    2
    """
    # returns 0 if root is None
    if not root:
        return 0
    # recursively gets the height of the left and right subtrees of root
    left_height:int = 1 + getHeight(root.left)
    right_height:int = 1 + getHeight(root.right)
    return max(left_height, right_height)

# Part 7: printTree
def printTree(root:BTNode|None) -> None:
    """
    Prints the content of the tree -- currently doesn't work well for big entries

    @param root: (BTNode) the root of the tree to be printed
    >>> some_node:BTNode = BTNode(2)
    >>> some_node.left = BTNode(1)
    >>> some_node.right = BTNode(3)
    >>> printTree(some_node)
        02
    01      03
    """
    # get the height of the tree and the max number of elements in the tree
    height:int = getHeight(root)
    max_elements:int = (2**height) - 1
    # initialize level of iteration, number of elements at that level
    level:int = 0
    no_elements_at_level:int = 2**level
    # initialize a queue to store the elements of the tree
    queue:deque[BTNode|None] = deque()
    queue.appendleft(root)
    elements_visited:int = 0 # tracks element popped out of the queue

    # # iterate through queue while not empty and while elements_visited <= max_number of element
    # while queue and elements_visited <= max_elements:
        # get the spacing to apply before and after 
    space_size:int = (max_elements - no_elements_at_level)//2
    # iterate through the levels within the tree
    for i in range(height):
        if i == 0:
            print(f" ", end = "")
        # iterate through every element in a level, including '_'
        for j in range(no_elements_at_level):
            # print space of size, spacing
            if space_size == 0:
                space_size = 1
            print(f"{' ' * space_size}", end = "")
            # pop current element from queue
            popped:BTNode|None = queue.pop()
            # increment element visited
            elements_visited += 1
            # if popped is None
            if popped is None:
                if elements_visited < max_elements:
                    # push None to the queue twice and print a '_'
                    queue.appendleft(None)
                    queue.appendleft(None)
                    print(f"__", end = "")
            # else (popped is not None)
            else:
                # push its children to the queue
                queue.appendleft(popped.left)
                queue.appendleft(popped.right)
                # print the data at popped
                if popped.data < 10:
                    print(f"0{popped.data}", end = "")
                else:
                    print(f"{popped.data}", end = "")
            # print space of size, spacing
            #print(f"{' ' * space_size}", end = "")
            # if space_size == 0:
            #     print(f" ", end = "")
            # else:
            #     print(f"{' ' * (space_size)}", end = "")
        # print a new line
        print()
        # increment level tracker and update number of elements at that level
        # also update space size
        level += 1
        no_elements_at_level = 2**level
        space_size:int = (max_elements - no_elements_at_level)//2
        # print(f"elements visited are {elements_visited}")
        if elements_visited >= max_elements:
            break


