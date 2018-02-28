class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        
    def getData(self):
        return self.data
    def setData(self, d):
        self.data = d
    def getNext(self):
        return self.next
    def setNext(self, n):
        self.next = n
    def __str__(self):
        return str(self.data)
        
class Queue :
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def isEmpty(self):
        return self.length == 0
    
    def enQueue(self, val):
        n = Node(val)
        if(self.length == 0):
            self.head = n
            self.tail = n
        else:
            p = self.head
            for i in range(1, self.length):
                p = p.next
            p.next = n
            self.tail = n
        self.length += 1
    
    def deQueue(self):
        if(self.length == 0):
            print("nothing to dequeue")
            return None
        n = self.head
        self.head = n.next
        self.length -= 1
        return n.data    

    def __str__(self):
        n = self.head
        a = "["
        i = 0
        while(n != None):
            if a == "[":
                a = a + str(n.data)
            else:
                a = a + ", " + str(n.data)
#            print(n.data)
            i += 1
#            if(i > 10):
#                return
            n = n.next
        return a + "]"