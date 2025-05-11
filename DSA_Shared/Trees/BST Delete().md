Delete scenarios:
       
Scenario 1: [[BST Delete() - Node has no children|Node has no children]] (node is a leaf) and therefore does not affect tree - base case
```
parentofnodetodelete.setLeft(None)
parentofnodetodelete.setRight(None)
```
 
Scenario 2: [[BST Delete() - Node has 1 Child|Node has 1 child]] - child to take node's place
```
#eg. if parentofnodetodelete.getLeft() == nodetodelete:
parentofnodetodelete.setLeft(nodetodelete.getLeft())
```

Scenario 3: [[BST Delete() - Node has 2 children|Node has 2 children]] - copy value of MIN() in right child (left most leaf of right side), replace Node and delete duplicate (call Scenario 1)

```
#eg. if parentofnodetodelete.getLeft() == nodetodelete:
		successor = self._minRec(nodetodelete.getRight()) 
		self.deleteRec(successor.getKey())
		successor.setLeft(nodetodelete.getLeft())
		successor.setRight(nodetodelete.getRight())
		parentofnodetodelete.setLeft(successor)
```
                        
Scenario 4: Node doesn't exist
```
try:
	if self._findRec(key, self._root, None) is None: 
		raise ValueError("Can not delete node that doesn't exist")
except ValueError as err:
	print("Invalid!", err)
```

Scenario 5: Node is root node! (SubScenarios are 1, 2, 3)
```
		self._root = None
```