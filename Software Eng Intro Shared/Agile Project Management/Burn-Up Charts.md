Show Planned vs Actual progress (Big Picture)
> They sometimes have a Scope line too to show extra work added midway through project

![[Pasted image 20240402184141.png]]

How to build in Excel (linking tables to graph above): 
1.      Find ‘estimated duration’ for each task ([[Estimate Duration of Tasks]])
2.      Find ‘sum of task durations’ by adding all Estimated Durations up
3.      Input’ Planned Project duration’ from AOA/AON graph
4.      ‘Planned progress per Day’ = ‘sum of task durations’ / Planned project durations
5.      Fill ‘actual finish’ time while project is progressing
		_(note: T1’s “Actual Finish” is the Calendar Day (not duration))_

Table 1 (T1)
![[Pasted image 20240402184534.png]]
6.      Make 2nd table and fill  “Time (Actual Day)’ with an appropriate interval
7.      Fill ‘planned progress (days)’ by it = “Time (Actual Day)’ * “planned progress per day’ ( from first table)
8.      Calculate “Actual Progress (days)’ (2nd table) by:
			- Find all tasks completed (“T1 Actual Finish”) before each “T2 Time (Actual Day)” row
			- Add the “T1 Estimated Duration (days)” of these tasks and put the total in “T2 Actual Progress”
			- Repeat but “T2 Actual Progress” is accumulative so also add total of row above to new row
2nd Table (T2)
![[Pasted image 20240402184736.png]]

What tables should look like (colours to match up cell links)
![[Pasted image 20240402184925.png]]