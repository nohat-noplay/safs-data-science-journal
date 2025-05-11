We will always want to remove the item with the highest priority so therefore always root node

Take a copy of root node (element[0])
Move last element( element[-1]) to replace root
new root is low priority item so TRICKLE DOWN... 
	- swap with child until child is not higher than this element
	- 2 children so each child must be compared and highest child to do swap

keep tricklingdown the node while: 
• The node still has children (ie: currIdx < count/2) AND
• Either children’s priority is higher than the node

Trickle down can be done iteratively or recursively...

