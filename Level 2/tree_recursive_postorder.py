post_ordered_list = []
class BinaryTree:
 
    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def postorder(self):
        post_ordered_list.insert(0, self.get_root_val())
        if self.get_right_child():
            self.get_right_child().postorder()
        if self.get_left_child():
            self.get_left_child().postorder()

            
        
    

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data