##### Call Stack 
- Each successive method call puts another stack frame on the stack
- This happens with all function/method calls, not just recursive calls
- When the method returns, the stack frame is popped off the call stack
- Python reserves a fixed amount of memory for the call stack - limiting its size!

##### Stack Overflow / Recursion Error
- When a call stack runs out of space - the program crashes!

![[stack.9c4ba62929cf 1.gif]]