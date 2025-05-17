1. Count each time an item occurs across all transactions
2.  **Write Frequent Pattern Set L = with each item in order of frequency (if tied, write in lexicographic order)**
eg. Frequent Pattern Set L = {(Burgers: 4), (Chips: 4), (Coke: 3), (Buns: 2), (Ketchup: 2)}
3. Re-write each transaction itemset using Frequent Pattern Set ordering
4. Build Frequent Pattern Tree:
	- Null or $\emptyset$ is root node, then create tree 
	- Check if itemset shares prefix with some previously inserted path, if so follow that path
	- Else create a new path and initialize the count to 1