import math

class BinaryTree:
 
    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

  
    def inorder_iterative(self):
        inorder_list = []
        inorder_list.append(self.get_root_val())
        left = self.get_left_child()
        right = self.get_right_child()
        while right != None:
            inorder_list.append(right)
            if right.get_left_child() != None:
                inorder_list.insert(0, right.get_left_child())
            right = right.get_right_child()
        while left != None:
            inorder_list.append(left)
            if left.get_right_child() != None:
                inorder_list.insert(0, left.get_right_child())
            left = left.get_left_child()
            
        inorder_list = inorder_list[::-1]
        
        l = int(math.floor(len(inorder_list)/2))
        length = len(inorder_list) - 1
        
        if(length > 1):
            inorder_list[length-l], inorder_list[length] = inorder_list[length], inorder_list[length-l]
        
        
        return inorder_list 
     


    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data