class BinaryTree:
    
    def __init__(self, root_node = None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node
    
    def find_min(self,root):
        # Return element should be of type TreeNode
        if (root == None):
            return None
        if (root.left_child == None):
            return root
        else:
            return self.find_min(root.left_child)
class TreeNode:
    def __init__(self, data,left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
    
    def __str__(self):
        return '%s' %self.data