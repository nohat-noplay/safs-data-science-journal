Referred to as Peer Review...
A collection of techniques to allow rest of team to understand each others work, improve code quality, to find faults in that work. 

Different techniques:  
	► Formal Inspection – formal group-based fault-detection process,  
	► Walkthrough – informal meeting to understand the code,  
	► Pair Programming – programmers write all code in pairs, with one reviewing the other’s work in real-time. (And roles swapping as needed.)  
	► Over-the-shoulder – show our code to a colleague


##### Pull Request
Triggers a Code Review. Another team member will look through your code in detail and find defects for you to fix. Note: The reviewer does NOT fix faults, just reports them.

##### Testing and/or Review
Testing and Review finds different kinds of faults

Testing
	► Automated (once the test cases are written).  
	► Only applicable to executable things (i.e. code).  
	► Finds failures – extra effort required to isolate faults.
	
Review
	► Manual – human effort required all the way through.  
	► Applicable to anything – code, documentation, use cases, design diagrams, etc.  
	► Finds faults directly, not failures.

##### Checklists
Each checklist item should be a yes/no question
Python example: <font style="color:red">There is no dead code</font>


