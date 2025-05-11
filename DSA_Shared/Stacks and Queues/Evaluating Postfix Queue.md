1. Create an empty Operand Stack

2. Iterate through each element in Postfix Queue:

- IF element isn’t an operator:
		- push() element onto stack and DeQueue
- IF element is an operator:
	- deQueue, pop() off stack and call it Operand1
	- pop() off stack and call it Operand2. 
	- Operand2, operator, Operand1 = subanswer. 
	- Push() subanswer onto stack.

3. Once iterations completed, final answer is the element left on the stack (accumulation of subanswers).

![[Pasted image 20240404151751.png]]