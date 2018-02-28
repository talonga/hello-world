import unittest
import linkedlist
import stak
import que

class TestLinkedList(unittest.TestCase):
    
    def test_length(self):
        ll = linkedlist.LinkedList()
        ll.add("ABC")
        self.assertEqual(1, ll.length)
        ll.add("ABC")
        self.assertEqual(2, ll.length)
        ll.add("ABC")
        self.assertEqual(3, ll.length)
    
    def test_add(self):
        ll = linkedlist.LinkedList()
        ll.add("ABC")
        n = ll.find(1) #get first node
        self.assertIsNotNone(n)
        self.assertEqual(n.node.data, "ABC")
        
    def test_find(self):
        ll = linkedlist.LinkedList()
        ll.add("ABC")
        ll.add("BCD")
        n = ll.find(2) #get second node
        self.assertIsNotNone(n)
        self.assertEqual(n.node.data, "BCD")
    
    def test_findFail(self):
        ll = linkedlist.LinkedList()
        ll.add("ABC")
        n = ll.find(2) #get second node
        self.assertIsNone(n)
        
    def test_findVal(self):
        ll = linkedlist.LinkedList()
        ll.add("ABC")
        ll.add("BCD")
        n = ll.findVal("BCD") 
        self.assertIsNotNone(n)
        self.assertEqual(n.node.data, "BCD")
        
    def test_findValFail(self):
        ll = linkedlist.LinkedList()
        ll.add("ABC")
        ll.add("BCD")
        n = ll.findVal("CDE") 
        self.assertIsNone(n)
    
    def test_swap(self):
        ll = linkedlist.LinkedList()
        ll.add("ABC")
        ll.add("BCD")
        ll.swap(1, 2)
        n = ll.find(1) #should now be BCD
        self.assertIsNotNone(n)
        self.assertEqual(n.node.data, "BCD")
        
    def test_swapFail(self):
        ll = linkedlist.LinkedList()
        ll.add("ABC")
        ll.add("BCD")
        ll.swap(1, 3)
        n = ll.find(1) 
        self.assertIsNotNone(n)
        self.assertEqual(n.node.data, "ABC")
        
class TestStack(unittest.TestCase):
    
    def test_length(self):
        s = stak.Stack()
        s.push("ABC")
        self.assertEqual(1, s.length)
        s.push("ABC")
        self.assertEqual(2, s.length)
        s.push("ABC")
        self.assertEqual(3, s.length)
        
    def test_pushpop(self):
        s = stak.Stack()
        s.push("ABC")
        val = s.pop()
        self.assertEqual(val, "ABC")
        
    def test_pushpop2(self):
        s = stak.Stack()
        s.push("ABC")
        s.push("BCD")
        val = s.pop()
        self.assertEqual(val, "BCD")
        
    def test_pushpop3(self):
        s = stak.Stack()
        s.push("ABC")
        s.push("BCD")
        val = s.pop()
        val = s.pop()
        val = s.pop() #None
        self.assertIsNone(val)

class TestQueue(unittest.TestCase):
    
    def test_length(self):
        q = que.Queue()
        q.enQueue("ABC")
        self.assertEqual(1, q.length)
        q.enQueue("ABC")
        self.assertEqual(2, q.length)
        q.enQueue("ABC")
        self.assertEqual(3, q.length)
        
    def test_endequeue(self):
        q = que.Queue()
        q.enQueue("ABC")
        val = q.deQueue()
        self.assertEqual(val, "ABC")
    
    def test_endequeue2(self):
        q = que.Queue()
        q.enQueue("ABC")
        q.enQueue("BCD")
        val = q.deQueue()
        self.assertEqual(val, "ABC")    
    
    def test_endequeue3(self):
        q = que.Queue()
        q.enQueue("ABC")
        q.enQueue("BCD")
        val = q.deQueue()
        val = q.deQueue()
        val = q.deQueue()#None
        self.assertIsNone(val)
        
if __name__ == '__main__':
    unittest.main()