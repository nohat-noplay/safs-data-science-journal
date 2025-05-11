Also LinkedList could have find():
	def findNode(self, node):
		current = self.head
		while current is not None:
			if current.getValue() == node:
				print("FOUND NODE!")
			else: 
				current = current.getNext()
		print("Node with value", node, "does not exist")

Big-O for Find():
	Worst Case: O(N) - goes through every [[Nodes|Node]] in the list and last match
	Average Case O(N/2) - finds the Node around the halfway mark (statistically)