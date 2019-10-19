#project 3; Data Structures 2302 - Adrian Lopez

import AVLtree
import RBtree

class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0

class BSTree:
    def __init__(self):
        self.root = None
    
    def BSTSearch(self, key):
        cur = self.root   
        while cur is not None:
            if key == cur.key:
                return cur #Found
            elif key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        return None #not found

    def BSTInsert(self, node):
        if self.root is None:
            self.root = node
            node.left = None
            node.right = None
        else:
            cur = self.root
            while cur is not None:
                if node.key < cur.key:
                    if cur.left is None:
                        cur.left = node
                        cur = None
                    else:
                        cur = cur.left
                else:
                    if cur.right is None:
                        cur.right = node
                        cur = None
                    else:
                        cur = cur.right       
            node.left = None
            node.right = None
    
    def BSTPrintInorder(self, node):
        if node is None:
            return                     

        self.BSTPrintInorder(node.left)   
        print(node)                    
        self.BSTPrintInorder(node.right)  
    
    #///////////////////////////////////////////////////////////////
    #AVL tree Implementation 
    #///////////////////////////////////////////////////////////////
    
    def AVLTreeUpdateHeight(self, node):

        leftHeight = -1
        if (node.left is not None):
            leftHeight = node.left.height
        rightHeight = -1
        if (node.right is not None):
            rightHeight = node.right.height
        node.height = max(leftHeight, rightHeight) + 1


    def AVLTreeSetChild(self, parent, whichChild, child):
        if (whichChild is not "left" and whichChild is not "right"):
            return False
        if (whichChild == "left"):
            parent.left = child
        else:
            parent.right = child
        if (child is not None):
            child.parent = parent

        self.AVLTreeUpdateHeight(parent)
        return True


    def AVLTreeReplaceChild(self, parent, currentChild, newChild):
        if (parent.left == currentChild):
            return self.AVLTreeSetChild(parent, "left", newChild)
        elif (parent.right == currentChild):
            return self.AVLTreeSetChild(parent, "right", newChild)
        return False


    def AVLTreeGetBalance(self, node):
        leftHeight = -1
        if (node.left is not None):
            leftHeight = node.left.height
        rightHeight = -1
        if (node.right is not None):
            rightHeight = node.right.height
        return leftHeight - rightHeight

    def AVLTreeRotateRight(self, node):
        leftRightChild = node.left.right
        if (node.parent is not None):
            self.AVLTreeReplaceChild(node.parent, node, node.left)
        else:  # node is root
            self.root = node.left
            self.root.parent = None
        self.AVLTreeSetChild(node.left, "right", node)
        self.AVLTreeSetChild(node, "left", leftRightChild)

    def AVLTreeRotateLeft(self, node):
        rightLeftChild = node.right.left
        if (node.parent is not None):
            self.AVLTreeReplaceChild(node.parent, node, node.right)
        else:  # node is root
            self.root = node.right
            self.root.parent = None
        self.AVLTreeSetChild(node.right, "left", node)
        self.AVLTreeSetChild(node, "right", rightLeftChild)

    def AVLTreeRebalance(self, node):
        self.AVLTreeUpdateHeight(node)  
            
        if self.AVLTreeGetBalance(node) == -2:
            if self.AVLTreeGetBalance(node.right) == 1:
                #Double rotation case.
                self.AVLTreeRotateRight(node.right)
            return self.AVLTreeRotateLeft(node)
        elif self.AVLTreeGetBalance(node) == 2:
            if self.AVLTreeGetBalance(node.left) == -1:
                #Double rotation case.
                self.AVLTreeRotateLeft(node.left)
            return self.AVLTreeRotateRight(node)     
        return node

    def AVLTreeInsert(self, node):
        if self.root is None:
            self.root = node
            node.parent = None
            return

        cur = self.root
        while cur is not None:
            if node.key < cur.key:
                if cur.left is None:
                    cur.left = node
                    node.parent = cur
                    cur = None
                else:
                    cur = cur.left
            else:
                if cur.right is None:
                    cur.right = node
                    node.parent = cur
                    cur = None
                else:
                    cur = cur.right

        node = node.parent
        while node is not None:
            self.AVLTreeRebalance(node)
            node = node.parent

    def AVLTreeRemoveNode(self, node):
        if node is None:
            return False
        
        #Parent needed for rebalancing
        parent = node.parent
            
        #Case 1: Internal node with 2 children
        if node.left is not None and node.right is not None:

            #Find successor
            succNode = node.right
            while succNode.left is not None:
                succNode = succNode.left
                
            #Copy the value from the node
            node = succNode
                
            #Recursively remove successor
            self.AVLTreeRemoveNode(succNode)
                
            #Nothing left to do since the recursive call will have rebalanced
            return True

        #Case 2: Root node (with 1 or 0 children)
        elif node is self.root:
            if node.left is not None:
                self.root = node.left
            else:
                self.root = node.right

            if self.root:
                self.root.parent = None

            return True

        #Case 3: Internal with left child only
        elif node.left is not None:
            self.AVLTreeReplaceChild(parent, node, node.left)
            
        #Case 4: Internal with right child only OR leaf
        else:
            self.AVLTreeReplaceChild(parent, node, node.right)
        
        #node is gone. Anything that was below node that has persisted is already correctly
        #balanced, but ancestors of node may need rebalancing.
        node = parent
        while node is not None:
            self.AVLTreeRebalance(node)            
            node = node.parent
        return True

    def AVLTreeRemoveKey(self, key):
        node = self.BSTSearch(key)
        return self.AVLTreeRemoveNode(node)

    #///////////////////////////////////////////////////////////////
    #RB tree Implementation 
    #///////////////////////////////////////////////////////////////

    def __len__(self):
        if self.root is None:
            return -1
        return self.root.count()
    
    def BSTRemove(self, key):
        par = None
        cur = self.root
        while cur is not None: # Search for node
            if cur.key == key: # Node found 
                if not cur.left and not cur.right:   # Remove leaf
                    if not par: # Node is root
                        self.root = None
                    elif par.left == cur:
                        par.left = None
                    else:
                        par.right = None
                elif cur.left and not cur.right:  # Remove node with only left child
                    if not par: # Node is root
                        self.root = cur.left
                    elif par.left == cur:
                        par.left = cur.left
                    else:
                        par.right = cur.left
        
                elif not cur.left and cur.right:   # Remove node with only right child
                    if not par: # Node is root
                        self.root = cur.right
                    elif par.left == cur:
                        par.left = cur.right
                    else:
                        par.right = cur.right
        
                else:                                  # Remove node with two children
                    # Find successor (leftmost child of right subtree)
                    suc = cur.right
                    while suc.left is not None:
                        suc = suc.left
                    successorData = suc.data
                    self.BSTRemove(suc.key)     # Remove successor
                    cur.data = successorData
        
                return # Node found and removed

            elif cur.key < key:  # Search right
                par = cur
                cur = cur.right

            else:               # Search left
                par = cur
                cur = cur.left

        return # Node not found
    
    def RBTreeSetChild(self, parent, whichChild, child):
        if whichChild is not "left" and whichChild is not "right":
            return False

        if whichChild == "left":
            parent.left = child
        else:
            parent.right = child
        if child is not None:
            child.parent = parent
        return True

    def RBTreeReplaceChild(self, parent, currentChild, newChild):
        if parent.left is currentChild:
            return self.RBTreeSetChild(parent, "left", newChild)
        elif parent.right is currentChild:
            return self.RBTreeSetChild(parent, "right", newChild)
        return False

    def RBTreeRotateLeft(self, node):
        rightLeftChild = node.right.left
        if node.parent is not None:
            self.RBTreeReplaceChild(node.parent, node, node.right)
        else: #node is root
            self.root = node.right
            self.root.parent = None
        self.RBTreeSetChild(node.right, "left", node)
        self.RBTreeSetChild(node, "right", rightLeftChild)

    def RBTreeRotateRight(self, node):
        leftRightChild = node.left.right
        if node.parent is not None:
            self.RBTreeReplaceChild(node.parent, node, node.left)
        else:  #node is root
            self.root = node.left
            self.root.parent = None

        self.RBTreeSetChild(node.left, "right", node)
        self.RBTreeSetChild(node, "left", leftRightChild)

    def RBTreeInsert(self, node):
        self.BSTInsert(node)
        node.color = "red"
        self.RBTreeBalance(node)

    def RBTreeGetGrandparent(self, node):
        if node.parent == None:
            return None
        return node.parent.parent

    def RBTreeGetUncle(self, node):
        grandparent = None
        if node.parent is not None:
            grandparent = node.parent.parent
        if grandparent is None:
            return None
        if grandparent.left == node.parent:
            return grandparent.right
        else:
            return grandparent.left

    def RBTreeBalance(self, node):
        if node.parent is None:
            node.color = "black"
            return

        if node.parent.color is "black":
            return
        parent = node.parent
        grandparent = self.RBTreeGetGrandparent(node)
        uncle = self.RBTreeGetUncle(node)
        if uncle is not None and uncle.color == "red":
            parent.color = uncle.color = "black"
            grandparent.color = "red"
            self.RBTreeBalance(grandparent)
            return

        if node == parent.right and parent == grandparent.left:
            self.RBTreeRotateLeft(parent)
            node = parent
            parent = node.parent
        elif node == parent.left and parent == grandparent.right:
            self.RBTreeRotateRight(parent)
            node = parent
            parent = node.parent

        parent.color = "black"
        grandparent.color = "red"
        if node == parent.left:
            self.RBTreeRotateRight(grandparent)
        else:
            self.RBTreeRotateLeft(grandparent)

    def RBTreeRemove(self, key):
        node = self.BSTSearch(key)
        if node is not None:
            self.RBTreeRemoveNode(node)

    def RBTreeRemoveNode(self, node):
        if node.left is not None and node.right is not None:
            predecessorNode = self.RBTreeGetPredecessor(node)        
            predecessorKey = predecessorNode.key
            self.RBTreeRemoveNode(predecessorNode)
            node.key = predecessorKey
            return

        if node.color == "black":
            self.RBTreePrepareForRemoval(node)
        self.BSTRemove(node.key)

    def RBTreeGetPredecessor(self, node):
        node = node.left
        while node.right is not None:
            node = node.right
        return node

    def RBTreeGetSibling(self, node):
        if node.parent is not None:
            if (node == node.parent.left):
                return node.parent.right
            return node.parent.left
        return None

    def RBTreeIsNonNullAndRed(self, node):
        if node is None:
            return False
        return node.color == "red"

    def RBTreeIsNullOrBlack(self, node):
        if node is None:
            return True
        return node.color == "black"

    def RBTreeAreBothChildrenBlack(self, node):
        if node.left is not None and node.left.color == "red":
            return False
        if node.right is not None and node.right.color == "red":
            return False
        return True

    def RBTreePrepareForRemoval(self, node):
        # if RBTreeTryCase1(tree,node):
        #     return

        sibling = self.RBTreeGetSibling(node)
        # if RBTreeTryCase2(tree, node, sibling):
        #     sibling = RBTreeGetSibling(node)
        # if RBTreeTryCase3(tree, node, sibling):
        #     return
        # if RBTreeTryCase4(tree, node, sibling):
        #     return
        # if RBTreeTryCase5(tree, node, sibling):
        #     sibling = RBTreeGetSibling(node)
        # if RBTreeTryCase6(tree, node, sibling):
        #     sibling = RBTreeGetSibling(node)

        sibling.color = node.parent.color
        node.parent.color = "black"
        if node == node.parent.left:
            sibling.right.color = "black"
            self.RBTreeRotateLeft(node.parent)
        else:
            sibling.left.color = "black"
            self.RBTreeRotateRight(node.parent)
        return

#///////////////////////////////////////////////////////////////

#///////////////////////////////////////////////////////////////
    
def main():

    avl_tree = BSTree()
    rb_tree = BSTree()

    
    print("What type of Binary Tree would you like to use?")
    print("Enter 0 for: AVL")
    print("Enter 1 for: Red Black")

    user_input = input()

    if user_input == '0':
        print("Hi")
        with open('glove.txt', 'r') as f:
         avl_tree = [line.strip() for line in f]
        print("Reached1")
        for nodes in avl_tree:
            avl_tree.AVLTreeInsert(nodes)
        print("Reached2")
        
    elif user_input == '1':
        with open('glove.txt', 'r') as f:
         rb_tree = [line.strip() for line in f]
        print("Reached1")
        for nodes in rb_tree:
            rb_tree.RBTreeInsert(nodes)
        print("Reached2")

    return

if __name__ == "__main__":
    main()
