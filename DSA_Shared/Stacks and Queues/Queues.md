   FIFO - First In, First Out
![[Pasted image 20240404145305.png]]

Enqueue() – add items to end of queue
Dequeue() – take items from the front of the queue
Peek() – check front item but don’t remove
isEmpty() – check queue is empty
isFull() – check is queue is full
count() – number of elements in queue

Also keep track of self.front and self.rear

<ins>Types of Queues:</ins> 
##### Shuffle
When front is deQueued, the rest shuffle forward. Slow O(N). 
![[Pasted image 20240404145513.png]]

##### Circular
![[Pasted image 20240404145937.png]]
Leave elements as is when deQueue, and change which element is the front
![[Pasted image 20240404145744.png]]
