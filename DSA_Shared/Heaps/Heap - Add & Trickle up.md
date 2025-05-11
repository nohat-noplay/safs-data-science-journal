
Add item to end of Array (In a Heap - this is to the right of the last added child)
Then TRICKLE UP = check parent and if parent is lower, swap with item - repeat until order is good

add() is essentially a loop that swaps the new node up the tree (trickle-up) while the following conditions hold true: 
• The new node has NOT made it to the root,AND 
• The parent’s priority is lower than the new node

Can be done iteratively or recursively....