![[bePceUMnSG-binary_search_gif.gif]]
It checks the half way element in a [[Sorting - Time Complexity|sorted]] list. If the element you are looking for is higher than the halfway element, it then checks halfway element in top half of list, and so on...

Average/Worse case = O(logN), 
Best case = O(1) (Element IS the halfway mark)

Binary search is faster than Linear Search (which is O(N)) however to sort the data pre-step is higher Big-O [[Time Complexity Analysis|Time Complexity]] (O(N log N))

A faster alternative to Linear Search < O(N) unless it's one search only - its probably better to just do Linear Search than sort the data to do Binary Search...

[[Sorting Algorithms and Big O]]