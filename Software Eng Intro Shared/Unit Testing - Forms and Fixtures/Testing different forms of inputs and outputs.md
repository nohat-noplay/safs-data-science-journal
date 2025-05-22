
Other ways of to write test cases with different inputs and outputs

eg. output is printed to screen rather than returned (as values)

Other input types:
► Parameter values; ► User input; ► Fields (variables outside the method/function); ► Files on disk; ► Databases; ► The operating system; ► Other running programs on the same computer; ► Online services. ► …

This subject takes into account:
- input through keyboard
- output to screen
- reading text files
- write to text files
- generate exceptions
------ everything is a string ^^^^

All inputs are strings!
eg. 
V1 = input("Enter value 1)
V2 = input("Enter value 2)
eg. 
writing to file is a string!

keep in mind - New Line (\n) character is read in string



We don't want user interaction when we testing!
- instead of asking user to enter values - we simulate test cases by entering a string and pass it to the test code (simulated input)

sys.stdin is 
sys.stdout is standard way to print to terminal 

![[Pasted image 20240506122738.png]]

1. Production code will have ^
2. Test code 

