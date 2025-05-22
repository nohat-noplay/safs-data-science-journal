A couple ways to create this:
1. State that the software must enable users to have a certain degree of efficiency.  
2. State that the software’s [[User Interface (UI)]] must have certain characteristics.

Approach #1
**Require the software to enable users to have a certain degree of efficiency.**  
Specifying:  
	► How long it should take users to perform a given task.  
		-<font style="color:green">The payment system must allow customers to pay for their purchases within 30 seconds, on average. </font>
	► The maximum acceptable user error rate. 
		-<font style="color:green">The payment system must facilitate customers choosing the correct payment method at least 99% of the time.  </font> 
		
These are not performance or reliability requirements.  
We’re not requiring the software to be fast & reliable here. We’re requiring the software to help the <ins>user</ins> be fast and reliable

Testing Approach #1: 
Test with different customers/users, run several times, take measurements and take an average.


Approach #2
**The UI must have specific characteristics to help user be fast, minimal mistakes, minimal effort**
	-<font style="color:green">The payment system must show all payment fields and options on one screen.</font>
	-<font style="color:green">The payment system must allow the user to query their  
purchase history with at most 2 mouse clicks.</font>

Testing Approach #2: 
We can check whether the finished product meets these requirements without having any test users.  This is not stochastic! No need to average multiple  measurements to verify these requirements
