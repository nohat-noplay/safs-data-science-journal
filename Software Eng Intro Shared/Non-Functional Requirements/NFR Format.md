                          
When writing NFR – it typically starts with “the system MUST…” and it is very specific.

They can also be written as [[User Stories]] as “as a …, I want …. So I can….”

NFRS are: 
1. Unambiguous
2. Doable
3. Verifiable
4. In-Scope
5. Are not "[[Week 3 Functional Requirements|Functional Requirements]]"

DO NOT MIX User Story option with MUST option.
Also: A NFR CAN NOT BE SENSIBLY EXPRESSED IN [[Use Cases|USE CASE]] FORM!

Proper NFRs have several properties: 

1. Unambiguous:
		Must be clear what’s being asked for.
			Example: 
			► BAD:<font style="color:red"> "The system must store temperature data in a spreadsheet file."</font>
			► GOOD:<font style="color:green"> "The system must store temperature data in an Excel-compatible CSV (comma-separated-value) file, with columns for the date (in YYYY-MM-DD format) and  degrees Celsius."</font>
			► BAD:<font style="color:red"> "The “colour enhance” function should take at most 250 ms to enhance a 10 megapixel image on an average PC."</font> < can't say "average PC"
			
		Note: you can say "Average User", but not "Average PC"
		
1. Doable (Implementable):
		Must be possible to implement the requirement.	
			Example: 
			► BAD:<font style="color:red"> "The system must process customer payments within  
	0.000000001 microseconds."</font> < This is impossible
3. Verifiable:
		Must be possible check afterwards that the  product meets the requirement.  
		NFR must be able to be observed/measured. 
		How to verify: 
		► Performance NFRs: measure the actual response time,  
		► Usability NFRs: measure the actions of test users.
		► Reliability NFRs: observe and time the system’s failures.
			Example: 
			► BAD:<font style="color:red"> "The system must work with all future web browsers"</font> < This is impossible to test
4. In-Scope: 
		Must be a requirement of the software itself.  You’re only making the software,  not everything and everyone around it.  Often users must follow “business rules”,  which can look like NFRs, but out of scope.  
			Example: 
			► BAD: <font style="color:red"> "Drivers can not run red lights"</font>
5. Non-Functional: 
		Must not be a functional requirement in disguise.  Ask yourself 2 Questions:
		1. Is it a characteristic of the system (NFR) or something the system must do (FR)?
		2. Can we write a use case flow of events? (this is a Functional Requirement if can)
			Example: 
				► BAD: <font style="color:red"> "The system must notify the uploader when one of their videos is reported for copyright infringement."</font> < (Functional)
				► GOOD: <font style="color:green"> "The system must deliver notifications to the uploader within 1hour of their being generated."</font> < (Non-functional)
				► BAD: <font style="color:red"> "Once restarted after a crash, the system should be able to recover unsaved images open at the time of the crash"</font> < (Functional)





![[Pasted image 20240402110829.png]]