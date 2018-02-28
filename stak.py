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
        
class Stack :
    
    def __init__(self):
        self.top = None
        self.length = 0
        
    def isEmpty(self):
        return self.length == 0
    
    def push(self, val):
        if(self.length == 0):
            self.top = Node(val)
        else:
            n = Node(val)
            n.next = self.top #new node points to old top
            self.top = n#new node is now new top
        self.length += 1
    
    def pop(self):
        if(self.length == 0):
            print("nothing to pop")
            return None
        n = self.top.data
        self.top = self.top.next
        self.length -= 1
        return n    

    def __str__(self):
        n = self.top
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