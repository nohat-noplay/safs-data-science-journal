
There are four possible scenarios for node insertion [[Methods|method]]: 

• The list is empty and we are inserting the first node 
<font style="color:green">def insertFirst() > newnode.setvalue() > if empty: self.head = newnode ((DL: self.tail = new node))</font>

• We are inserting before the head node 
<font style="color:green">def insertFirst() > newnode.setvalue() > if not empty:  newnode.setNext as self.head, ((DL: self.head.setPrev as new node), then make self.head = newnode</font>

• We are inserting after the tail of the list 
<font style="color:green">def insertLast() > newnode.setvalue() > if not empty:  self.tail.setNext to new node, ((DL: newnode.setPrev as self.tail), then make self.tail = newnode</font>

• We are inserting somewhere in the middle of the list
<i style="color:green">After old node 1 and before old node 2 (oldnode1.getNext)</font>
<font style="color:green">newnode.setvalue() > use Find() method >    oldNode1.setNext as new node, ((oldNode2.setPrev as new node)), then make newNode.setNext as old node 2</font>

[[Methods|Find() Method]]
[[Single Linked List]]
DL = [[Doubly-Linked List]]