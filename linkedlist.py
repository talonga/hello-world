import collections

nodeTuple = collections.namedtuple('nodeTuple', ['prev', 'node'])

class Node :
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
        
class LinkedList :
    
    def __init__(self):
        self.head = None
        self.length = 0
        
    def isEmpty(self):
        return self.head == None
    
    def add(self, val):
        if self.isEmpty():
            self.head = Node(val)
        else:
            n = self.head
            while(n.next != None):
                n = n.next
            n.next = Node(val)
        self.length += 1
    
    def remove(self, index):
        nt = self.find(index)
        if(nt == None):
            print("unable to remove")
            return
        print("removing element " + str(index) + " with value " + str(nt.n.data))
        if (nt.p == None):
            self.head = nt.node.next
        else:
            nt.prev.next = nt.node.next
        self.length -= 1
    
    def removeVal(self, val):
        nt = self.findVal(val)
        if (nt == None):
            print("element with value " + str(val) + " not found")
        else:
            if (nt.prev == None):
                self.head = nt.node.next
            else:
                nt.prev.next = nt.node.next
            print("removing element with value " + str(val))
        
    def findVal(self, val):
        n = self.head   
        p = None
        i = 1
        for i in range(1, self.length+1):
            if (n.data == val):
                return nodeTuple(p, n)
            p = n
            n = n.next
        return None
        
    def find(self, index):
        n = self.head   
        p = None
        i = 1
        if(index <= 0):
            print(str(index) + " is an invalid index to find")
            return None
        if(index > self.length):
            print(str(index) + " is larger than length of list")
            return None
        
        for i in range(1, index):
            p = n
            n = n.next
            i += 1
        return nodeTuple(p, n)
    
    def swap(self, a, b):
        if (a==b):
            return
        if (a > self.length or b > self.length):
            print("attempting to swap elements larger than length")
            return
        if (a<b):
            low = a
            high = b
        else:
            high = a
            low = b
            
        lowNode = self.find(low)
        highNode = self.find(high)
        
        if ((high-low) == 1): #only do 3 swaps
            if(low == 1):
                self.head, lowNode.node.next, highNode.node.next = highNode.node, highNode.node.next, lowNode.node
            else:
                lowNode.prev.next, lowNode.node.next, highNode.node.next = highNode.node, highNode.node.next, lowNode.node
        else : #do 4 swaps
            if(low == 1):
                self.head, lowNode.node.next, highNode.prev.next, highNode.node.next = highNode.node, highNode.node.next, lowNode.node, lowNode.node.next
            else:
                lowNode.prev.next, lowNode.node.next, highNode.prev.next, highNode.node.next = highNode.node, highNode.node.next, lowNode.node, lowNode.node.next
    
    def partition(self, low, high):
        nt = self.find(high) #use last element as a marker
        pivot = nt.node
        
        i = low-1
        for j in range(low, high):
            if self.find(j).node.data < pivot.data:
                i += 1
                self.swap(i, j)#shuffle largerelement up to "j", while "i" retains the index of smaller elements
        self.swap(i+1, high)#slot the marker between smaller and larger
        return i+1

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