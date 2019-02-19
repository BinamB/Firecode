class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node

    def diameter(self,root):
        return self.diameter_helper(root, BinaryTree.Height())
        
        
    class Height:
        def __init__(self, h = 0):
            self.h = h
    
    def diameter_helper(self, root, height):
        left_height = BinaryTree.Height()
        right_height = BinaryTree.Height()
        if root == None:
            height.h = 0 
            return 0
        
        left_height.h += 1
        right_height.h += 1 
        
        ldiameter = self.diameter_helper(root.left_child, left_height)
        rdiameter = self.diameter_helper(root.right_child, right_height)
        
        height.h = max(left_height.h, right_height.h) + 1
        return max(left_height.h + right_height.h + 1, max(ldiameter, rdiameter))

class TreeNode:
    def __init__(self, data,left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child