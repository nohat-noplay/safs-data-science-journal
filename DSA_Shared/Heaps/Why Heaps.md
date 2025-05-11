use heaps to perform sorting 
1. Take an array of unsorted data 

2. Add all elements of the unsorted array into a heap, using the element value as the priority 
	• This will organise the elements into a heap 
	- Best: O(1), Average/Worst: O(log N)
	
3. Remove each element from the heap one at a time and place them back into the array 
	• Since a heap returns highest-priority first, the elements will come out in sorted order (or reverse sorted order)
	- All cases:  O(log N)

Heaps  = O(N log N)
Simple HeapSort not In Place (not reusing array) 
- Can be In Place with Heapify code 
HeapSort not Stable (will swap equal items)



Max Heap - largest value is highest priority 
	• Max-heaps will return larger values first,
	- loop from N…0 (max-heap)

Min Heap -smallest value is highest priority
	• Min-heaps will return smaller values first,
	- loop from 0…N (min-heap)








Create Heap as Array
