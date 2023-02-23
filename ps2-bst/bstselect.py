import bstsize

class BST(bstsize.BST):
    """
    Adds select method to BST, starting with code from bstsize.   
    """
    
    def select(self, index):
        """
        Takes a 1-based index, and returns the element at that index,
        or None if the index is out-of-bounds. Starting at the root,
        the tree is searched by examining the size of the left-child
        tree, which gives the number of elements smaller than the
        current node.
        """
        # Get the size of the BST
        bst_size = bstsize.size(self.root)


        # If the index is invalid, return None
        if index <= 0 or index > bst_size:
            return None
        
        # Start at the root of the BST
        node = self.root
        
        # Search for the node containing the desired element
        while node is not None:
            left_size = bstsize.size(node.left) # Get the size of the left subtree
            
            # If the desired element is at this node, return the node
            if index == left_size + 1:
                return node
            
            # If the desired element is in the left subtree, search there
            elif index <= left_size:
                node = node.left
            
            # If the desired element is in the right subtree, search there
            else:
                index -= left_size + 1
                node = node.right
        
        # If the desired element was not found, return None
        return None

        
