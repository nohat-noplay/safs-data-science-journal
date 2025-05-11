To re-order the equation so that the higher precedence operations (following BIMDAS) comes before the lower ones (including brackets)

1.      Create an empty stack

2.      Create an empty Postfix Queue

3.      Iterate through each term
		- IF term is ‘(‘ – push() onto stack
		- IF term is ‘)’ – if Top() of stack is not ‘(‘, pop() Top() off stack and enQueue it (and remove "(")
			
		- IF term is an operator (+ - / \*\): 
				- WHILE stack is not isempty() and Top() is not ‘(‘ and the precedence Top() of stack is greater or equal to our operator (current term): 
					- Pop() Top off stack and enQueue it in Postfix Queue. 
					- Repeat until while statement ends.
				- Push() current term onto Stack
		- If term is not brackets or operator (must be operand), enQueue term in Postfix Queue
		
4.      After iterations are completed, Pop() elements off stack and enQueue them in Postfix Queue

![[Pasted image 20240404151340.png]]

