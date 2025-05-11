![[Pasted image 20240404181408.png]]

Advantages of Double Ended Linked Lists (compared to [[Single Linked List]]): 

Allows for DeQueue

Reduces [[Time Complexity Analysis]] for:
- insertLast()
- peekLast()
- removeFirst()

It does NOT reduce Big-O for:
- removeLast() - you need to get to second last node to do this one 
		^^This can be fixed by [[Doubly-Linked List]]