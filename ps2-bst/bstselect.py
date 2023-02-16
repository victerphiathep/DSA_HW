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

        node = self.root
        
        return None
