class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
                      
    def is_cyclic(self):
        slow = self.head.getNext()
        fast = self.head
        i = 0
        if(slow == None):
            return False
        while i<=0:
            if(slow.getNext() == None):
                return False
            if(slow.getData() == fast.getNext().getData()):
                return True
            i = i + 1
            
class Node:
    def __init__(self):
        self.data = None
        self.next = None
     
    def setData(self,data):
        self.data = data
      
    def getData(self):
        return self.data
     
    def setNext(self,next):
        self.next = next
     
    def getNext(self):
        return self.next
