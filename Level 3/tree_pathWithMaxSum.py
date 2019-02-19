class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node

    # All the necessary collection moduled have been already imported.
    def max_sum_path(self,root):
        holder = [0]
        self.helper(root, holder)
        return holder[0]
        
        
    def helper(self, root, holder):
        if root == None:
            return 0
        left_sum = self.helper(root.left_child, holder)
        right_sum = self.helper(root.right_child, holder)
        
        val = max(root.data + left_sum, root.data + right_sum)
        
        holder[0] = max(holder[0], left_sum + root.data + right_sum)
        
        return val
        
class TreeNode:
    def __init__(self, data,left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child