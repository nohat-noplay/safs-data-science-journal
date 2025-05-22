A use case are a detailed way of showing how the software system will interact with the outside world. Each Use Case describes a [[Week 3 Functional Requirements|Functional Requirement]]


[[Actors]] - an entity that interacts with the system being created. Can be human or not-human. 
[[Goals]] - of Primary Actor to be achieved by end users of the system.
System - the Software
Stakeholders - people who are interested in the completion of the product and who is affected by it

Trigger Event - An event that starts the Use Case's Flow of Events
<i style="color:green">User action, time of day</font>
Preconditions - If False, prevents use case from starting even with trigger 
<i style="color:green">User must be logged on</font>
Flow of events - Steps such as interactions by [[Actors]] (not with each other), or initiated by system 
<i style="color:green">System receives uploaded file</font>
Extensions - Describes flow of events if something specific goes wrong (or differently) at that point 
<i style="color:green">2A: The uploaded file is not a valid format</font>
<i style="color:green">1. The system asks the uploader to choose another file.<br>
2. The use case resumes at step 1.</font>



![[Pasted image 20240402165009.png]]



###### Use Case Representation:
Can be textual or graphical. They are NOT Flow charts

Use Case (Textual): 
![[Pasted image 20240402165350.png]]


###### Before writing a Use Case description
 May create 
 - a simple actor-goal list (see Task Level Goals in [[Goals]])
-  a [[UML Case Diagram]] 




