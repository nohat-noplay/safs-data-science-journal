
<span style="color:#ffea00">SORTING</span>
1. Selection Sort - MIN
Iterates through list to find “minimum” element and once it gets to end of list, _selects_ that minimum element and SWAPS it with the left most unsorted element. Repeat.
[[Selection Sort]]
2. Insertion Sort - INSERTS BETWEEN
Pulls out element and checks each element to the left of original place to check if it’s higher or lower. _Inserts_ the element in between two elements where one is lower and the other in higher. (Can be visualised as sitting between two elements when comparing element to its left every time)
(Start with element 1 so plays with second element in list)
[[Insertion Sort]]

BUBBLESORT 
Comparing two elements next to eachother and sorting the two from lowest to highest. Then moving 1 element up and repeating. "Bubbling up"

<span style="color:#ffea00">RECURSION</span>
A recursive algorithm has 3 components: 
1. Must be able to be split into smaller identical problems of the same form
2. Must have Base Cases that terminates the function without using recursion
3. The algorithm must progress towards Base Cases with every recursive call (or it would result in an infinite loop)

PROs of Recursion: 
- Some Algorithms are simpler eg. Towers of Hanoi, Merge Sort, Binary Trees

CONs of Recursion: 
- Call Stack limits number of recursive iterations before stack overflow issue
- Time used for calling a method



<span style="color:#ffea00">REVERSE LIST</span>
1. Create empty temporary Stack
2. While Queue (List) is not empty: DeQueue each item and Push it onto the Stack
3. While Stack is not empty: Pop each item off Stack and Enqueue it
1 2 3 4 5 > 5 4 3 2 1

<span style="color:#ffea00">LINKED LISTS</span>
Advantages of Double-Ended Linked List: 
- Allows for efficient DeQueue operation
- Allows for efficient "InsertLast" & "PeekLast"

NO Advantage for RemoveLast() as you need to get to the second last node - to make this the new tail. So it's a similar BigO. A Doubly Linked List can make this easier as there is a node.prev (previous node) pointer. 

In code: "Head" refers to the first element (even though its drawn as a separate element)
Therefore: 
		newNd = ListNode(20), newNd.next = head, head = newNd
	means
		newNd is now the first in the list (next points to the old first)
Therefore: 
		head.next is the second element in a list (not the first element)

Pros for Linked Lists (compared to Arrays):
- Grows and Shrinks with data 
- No limit on size (Arrays need to know during inilialisation how much space to use)
- Easy to Insert anywhere (Arrays only easy to insert at end)
- Elements can be anywhere in memory

Cons of Linked Lists (compared to Arrays):
- Time to access an element (O(Number of elements in entire LL)) (Array is only 1 step O(N))
- Next reference point of node is memory usage overhead


<span style="color:#ffea00">INFIX/POSTFIX</span>
To turn INFIX into POSTFIX: 
[[InfixtoPostfix.jpg]] < I made a flow chart
Note: 
 1. If element is operator - while stack is not empty, top of stack is not open bracket and top of stack is greater or equal to the operator - pop off stack and enqueue. Otherwise push new operator onto stack
 2. If element is closed bracket - pop off operators in stack until get to open bracket. Remove open bracket from stack


<span style="color:#ffea00">TREES</span>
 Pre-order Traversal: ------------Parents First
 Root, Left Child (now is root (recursion)), Right Child (now is root(recursion))
 <span style="color:#00b050">Can test this - This can recreate the tree as is. </span>
 
In-order Traversal: -------------Zig Zag
Zig Zag from most Left Child branch, to its parent, to that parents Right Child
<span style="color:#00b050">Can test this - output is in sorted order</span>

Post-order Traversal: ------------Leaf Delete
Children first 
-all children in left branch of root, followed by all parents in left branch of node (lower to higher). 
-repeat for right branch of root
-then root
<span style="color:#00b050">Can test this - if it deleted as it travelled, it would be deleting only leaf nodes</span> 

Deleting Options:
Leaf node: Just delete
Node has one Child:  Move child to where node is
Node has 2 Children:  Replace Node with minimum node within Right branch

If keys are inserted in sorted order it would create a Degenerate Tree. 
A fully Degenerate Tree is just a Linked List and does not have the efficiency a Binary Search Tree can offer when searching for a Node. 


<span style="color:#ffea00">GRAPHS</span>
[[Adjacency List]] 
PROS: traversing edgelist and require less memory,  
CONS: finding/adding/removing edge

[[Adjacency Matrix]] 
PROS: good at usability, finding/adding/removing edge,
CONS: bad at required memory and traversing edgelists

[[Depth-First Search]]
[[Breadth-First Search]]


