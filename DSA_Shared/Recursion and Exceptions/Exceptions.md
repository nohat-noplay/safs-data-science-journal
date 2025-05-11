Object Orientated languages solve error handling with exceptions
On an error, a method ‘throws’ an exception > The calling method can ‘catch’ the exception:
		• If caller doesn’t catch it:
			 the exception is thrown to the next-higher caller 
		• If no-one catches it:
			 the exception causes the program to crash

3 types of Errors:
-          Syntax Errors: Mistakes in use of language or Spelling/Grammar issues
-          Runtime Errors: Program doesn’t make sense or something is called but doesn’t exist
-          Logical Errors: Program not logical (eg. Indentation issue or wrong variable name)

Exceptions:
-          TypeError: raise it if a parameter is not the type we know how to handle
-          ValueError: raised if variable is right type but wrong value
-          NotImplementedError:

Catching Exceptions:
-          “try”: define the set of statements whose exceptions will all be handled by the catch block associated with this try
-          “except”: processing to do if an exception is thrown in the try
-          “finally”: processing to always do regardless of whether an exception occurs or not. This is optional but good for clean up (eg. closing open files)

Multiple Options to deal with Exceptions in Python: 

![[Pasted image 20240404124719.png]]