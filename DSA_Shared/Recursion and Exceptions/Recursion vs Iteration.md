<ins>Advantages of Recursion: </ins>
 Some algorithms are much simpler using [[Recursion]]
[[Towers of Hanoi]]

<ins>Disadvantages of Recursion:</ins>
 The [[Recursion Error (python) or Stack Overflow (java)|call stack]] limits the number of recursive ‘iterations’ that can be performed 
	•No more than a few thousand iterations before stack overflow
  Usually slower due to method call overhead 
	 • Every time a method is called, a few instructions are needed to set up the method call (e.g., allocate space for local vars, etc.) 
	 • For small recursive methods (a few lines or less), this call overhead will become a significant factor of the processing

<ins>When to use Recursion:</ins>
The overheads of method calls are small and little chance of [[Recursion Error (python) or Stack Overflow (java)]]:
<span style="color:#00b050">Tower's of Hanoi, Merge Sort, Quick Sort, Binary Trees</span> 