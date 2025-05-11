Calling a method repeatedly where within that method, it calls itself.

Dividing the problem into sub problem which is a simpler version of the same problem (until it reaches a terminating condition)

**Base Cases** can be terminating condition (or it could be infinite and there is a [[Recursion Error (python) or Stack Overflow (java)]]) and crash – memory limit exceeds)

##### Necessary properties of a recursive algorithm: 
1) Decomposable into a simpler version of the same form 
			<span style="color:#00b050">N! is easy to calculate if (N-1)! is known </span>
2) One or more base case(s) exists (and is not recursive) 
		<span style="color:#00b050">When n=0, no factorial is needed – just return 1</span>
		 The base case is the terminating condition of the recursion: 
		 • Thus every recursive method has an ‘if’ check for base case(s)
3) Base case must be reached 
		• This requires a parameter (e.g., n) that MUST be changed during every recursive call (changing the value towards the base case)... Otherwise the recursion will never end!
![[Pasted image 20240404130819.png]]

Recursive Algorithms:
[[Factorial n!]]
[[Fibonacci Sequence]]
[[Towers of Hanoi]]
