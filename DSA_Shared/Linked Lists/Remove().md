There are four possible scenarios for node remove [[Methods|method]]: 

• Removing the head ListNode 
<font style="color:green">def removeFirst() > self.head = self.head.getNext() > ((DL: self.head.setPrev to none))</font>

• Removing the tail ListNode
<font style="color:green">def removeFirst() > self.tail = self.tail.getPrev() > self.tail.setNext to None</font>

• Removing solo remaining ListNode in list 
<font style="color:green">def removeLast, if self.head.getNext == None > self.head = None, self.tail = None</font>

• We are removing ListNode somewhere in the middle of the list
<font style="color:green">use Find() method > (node.getPrev).setnext to node.getNext > ((DL: (node.getNext).setPrev to node.getPrev))</font>

[[Methods|Find() Method]]
[[Single Linked List]]
DL = [[Doubly-Linked List]]