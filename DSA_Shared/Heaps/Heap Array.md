Heaps can represented as an Array and allows us to CALCULATE how to go up and down the tree
Root is element[0]
Siblings are beside eachother

Thus if we are at node [currIdx], then:
leftChildIdx = (currIdx * 2) + 1 
rightChildIdx = (currIdx * 2) + 2 
parentIdx = (currIdx - 1) / 2

![[Pasted image 20240427093917.png]]