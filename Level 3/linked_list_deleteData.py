class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
                      
    #method for deleting a node having a certain data        
    def delete(self,data):
        current = self.head
        if self.head == None:
            return None 
        else:
            if self.head.getData() == data:
                self.head = self.head.getNext()
            else:
                while (current.getData() != data):
                    previous = current
                    current = current.getNext()
                if current.getData() == data:
                    previous.setNext(current.getNext())
                else:
                    return None

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