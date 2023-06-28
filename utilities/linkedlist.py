class LinkedList:
    
    class node:   
        def __init__(self, data=None, nextVal=None):
            self.data = data
            self.next = nextVal
        
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def addFirst(self, data):
        newNode = self.node(data)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
    
    def printList(self):
        cur = newLinkedList.head
        while cur != None:
            print(cur.data)
            cur = cur.next
    
        
if __name__ == '__main__':
        newLinkedList = LinkedList()
        newLinkedList.addFirst(3)
        newLinkedList.addFirst(2)
        newLinkedList.addFirst(1)
        newLinkedList.printList()
        
        
        #print(newLinkedList.size)
        
        #print(cur.next.data)
        
        
        
        
        

        
         