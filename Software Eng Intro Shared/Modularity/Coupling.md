Can be a metric - tightly coupled (highly reliable on each other) or loosely coupled (not reliable on each other)- 
Looser as possible is better. 

If two modules are too reliant on each other - means it's not modular and increases complexity. 
Forms of coupling: 
1.<span style="color:#00b0f0"> calls - good</span>
2. <span style="color:#00b0f0">calls w parameters and return values - good (but not too many parameters)</span>
		eg. def xyzfunction(unit,code, building, room, capacity, count, startT, endT, dept):
3. <span style="color:#f3f2f2"><span style="color:#f3f2f2"><span style="color:#ff0000">global variables - not good - can be seen by entire class - all methods can edit. increase</span> </span></span>complexity and get messy 
		eg. def square(): 
		global x 
		global xSq<span style="color:#f3f2f2">uared </span>
		xSquared = x * x
4. <span style="color:#ff0000">control flags - not good</span> - eg would be function that does two things and you send it a True or False to determine which thing it should do (if statement)
