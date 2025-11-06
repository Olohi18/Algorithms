# Name:  - your name (and your partners name) <br>
# Peers:  - names of CSC252 students who you consulted or ``N/A'' <br>
# References:  - URL of resources used <br>
# Assumption: BSTs can't have duplicates
from hwk7 import *


def getSmallTree() -> BTNode:
    root = BTNode(10)
    root.left = BTNode(34)
    root.right = BTNode(89)
    root.left.left = BTNode(45)
    root.left.right = BTNode(50)
    return root

def main():
    POL_helper()    #Test is hwk7.py imported correctly.
    # Regular Tree
    small_tree = getSmallTree()
    # Right-skewed tree
    node_right:BTNode = BTNode(1)
    node_right.right = BTNode(2)
    node_right.right.right = BTNode(3)
    node_right.right.right.right = BTNode(4)
    node_right.right.right.right.right = BTNode(5)
    ## Single node
    nodesingle:BTNode = BTNode(7)
    ## Left-skewed tree
    node_left:BTNode = BTNode(14)
    node_left.left = BTNode(12)
    node_left.left.left = BTNode(10)
    node_left.left.left.left = BTNode(8)
    node_left.left.left.left.left = BTNode(6)
    ## heavily unbalanced tree
    node_unbalanced:BTNode = BTNode(2)
    node_unbalanced.left = BTNode(1)
    node_unbalanced.right = BTNode(3)
    node_unbalanced.right = node_right
    ## regular tree
    node_regular:BTNode = BTNode(90)
    node_regular.left = BTNode(45)
    node_regular.left.right = BTNode(60)
    node_regular.left.left = BTNode(30)
    node_regular.right = BTNode(135)
    node_regular.right.left = BTNode(120)
    node_regular.right.right = BTNode(150)
    ## single tree
    node_single:BTNode = BTNode(8)

    print(f"-----------In-Order Walk----------")
    print(inOrderWalk(small_tree)) # [45, 34, 50, 10, 89]
    print(inOrderWalk(node_right)) # [1, 2, 3, 4, 5]
    print(inOrderWalk(nodesingle)) # [7]
    print(inOrderWalk(None)) # None
    print(inOrderWalk(node_left)) # [6, 8, 10, 12, 14]
    print(inOrderWalk(node_unbalanced)) # [1, 2, 1, 2, 3, 4, 5]
    node_right.right.right.right.right.left = None
    print()

    """Check further with the printTree method when you write it"""
    print(f"------------lst2BST-------------")
    print(listToTree([])) # empty list-> None
    print(listToTree([1,2,3,4,5]).data) # type: ignore 3
    print(listToTree([2,4,6,7,8,9,10,15]).data) # type: ignore 8 
    print()

    """Check further with the printTree method when you write it"""
    print(f"------------lst2BST-------------")
    print(fixTree(small_tree).data) # type: ignore 45
    print(fixTree(node_left).data) # type: ignore 10 
    print(fixTree(BTNode(7)).data) # type: ignore 7
    print()

    print("-----------addNodeBST---------------")
    ## regular case
    #print(addNodeBST(node_regular, 125)) # True
    ## adding to a skewed tree
    print(addNodeBST(node_left, 5)) # True
    print(addNodeBST(node_left, 7)) # True
    ## adding a duplicate
    print(addNodeBST(node_left, 5)) # False
    ## adding to an empty tree
    print(addNodeBST(None, 8)) # False
    ## adding to a single-element tree
    print(addNodeBST(BTNode(8), 2)) # True
    print()

    print("-----------removeNodeBST---------------")
    node_regular.right.right.left = BTNode(145)
    node_regular.right.right.right = BTNode(165)
    node_regular.left.left.left = BTNode(15)
    ## regular tree
    # remove node with next big != right
    print(f"Before {135} removed: {inOrderWalk(node_regular)}", end = ". ")
    print(removeNodeBST(node_regular, 135)) # True
    print(f"After {135} removed: {inOrderWalk(node_regular)}")
    # remove node with next big = right
    print(f"Before {150} removed: {inOrderWalk(node_regular)}", end = ". ")
    print(removeNodeBST(node_regular, 150)) # True
    print(f"After {150} removed: {inOrderWalk(node_regular)}")
    # remove leafs
    print(f"Before {60} removed: {inOrderWalk(node_regular)}", end = ". ")
    print(removeNodeBST(node_regular, 60)) # True
    print(f"After {60} removed: {inOrderWalk(node_regular)}")
    print(f"Before {165} removed: {inOrderWalk(node_regular)}", end = ". ")
    print(removeNodeBST(node_regular, 165)) # True
    print(f"After {165} removed: {inOrderWalk(node_regular)}")
    # remove node with no right children
    print(f"Before {30} removed: {inOrderWalk(node_regular)}", end = ". ")
    print(removeNodeBST(node_regular, 30)) # True
    print(f"After {30} removed: {inOrderWalk(node_regular)}")
    # remove root
    print(f"Before {90} removed: {inOrderWalk(node_regular)}", end = ". ")
    print(removeNodeBST(node_regular, 90)) # True
    print(f"After {90} removed: {inOrderWalk(node_regular)}")
    ## removing from a skewed tree
    print(f"Before {7} removed: {inOrderWalk(node_left)}", end = ". ")
    print(removeNodeBST(node_left, 7)) # True
    print(f"After {7} removed: {inOrderWalk(node_left)}")
    ## trying to remove an element not in the tree
    print(f"Before {7} attempted to be removed: {inOrderWalk(node_left)}", end = ". ")
    print(removeNodeBST(node_left, 7)) # False
    print(f"After {7} attempted and FAILED: {inOrderWalk(node_left)}")
    ## removing from an empty tree
    print(f"Before {8} attempted to be removed: {inOrderWalk(None)}", end = ". ")
    print(removeNodeBST(None, 8)) # False
    print(f"After {8} attempted and FAILED: {inOrderWalk(None)}")
    ## removing the root of a tree 
    print(f"Before {8} removed: {inOrderWalk(node_single)}", end = ". ")
    print(removeNodeBST(node_single, 8)) # True
    print(f"After {8} attempted and FAILED: {inOrderWalk(node_single)}")
    # print("------------removeBST-------------")
    # print(inOrderWalk(node_regular))
    # print(inOrderWalk(node_regular))
    # print(removeNodeBST(node_regular, 165))

    print(f"-----------isBalanced---------------")
    print(isBalanced(small_tree)) # True
    print(isBalanced(node_right)) # False
    print(isBalanced(node_left)) # False
    print(isBalanced(BTNode(7))) # True
    print(isBalanced(None)) # True
    specialImBalance:BTNode = BTNode(5)
    specialImBalance.left = BTNode(4)
    specialImBalance.left.left = BTNode(2)
    specialImBalance.left.right = BTNode(1)
    specialImBalance.right = BTNode(3)
    specialImBalance.right.right = BTNode(8)
    specialImBalance.right.left = BTNode(6)
    specialImBalance.right.left.left = BTNode(7)
    specialImBalance.right.left.right = BTNode(9)
    specialImBalance.right.left.left.left = BTNode(10)
    specialImBalance.right.left.right.right = BTNode(11)
    print(isBalanced(specialImBalance)) # False
    anotherImbalance:BTNode = BTNode(10)
    anotherImbalance.left = BTNode(9)
    anotherImbalance.left.left = BTNode(6)
    anotherImbalance.right = BTNode(7)
    anotherImbalance.right.left = BTNode(5)
    anotherImbalance.right.left.right = BTNode(2)
    anotherImbalance.right.left.right.left = BTNode(4)
    anotherImbalance.right.left.right.right = BTNode(3)
    print(isBalanced(anotherImbalance)) # False
    print()

    print(f"------------printTree-----------")
    some_node:BTNode = BTNode(2)
    some_node.left = BTNode(1)
    some_node.right = BTNode(3)
    printTree(some_node)  
    print()  
    printTree(small_tree)
    print()
    printTree(node_regular)
    print()
    print(inOrderWalk(node_regular))









    



if __name__ == "__main__":
    main()