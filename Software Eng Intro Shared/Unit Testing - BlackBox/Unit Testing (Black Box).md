
There are many phases of testing:
► <span style="color:#00b050">Unit testing (small-scale) – most of this lecture;</span>
► Integration testing (medium-scale); 
► System testing (large-scale); 
► Function testing, 
► Performance testing, 
► Acceptance testing, 
► Installation testing;
► Regression testing (after modification).


#### Unit Testing Concepts

Unit testing is the process of testing individual components of a software.
We must 
1. <span style="color:#00b050">design,</span> 
2.<span style="color:#00b050"> implement and </span>
3. <span style="color:#00b050">execute test cases.</span>

Testing is about finding logic errors – code that is syntactically correct, but logically wrong.
Logic Errors - the compiler won't stop you because it doesn't know you meant something else
Testing should trigger as many failures as possible.

<span style="color:#ffea00">Don't worry about syntax errors</span>

#### Test Case
<span style="color:#00b050">A test case is a separate piece of code designed and implemented to test a component of a software. </span>

A test case is one way the code could be wrong (need to think of all possibly scenarios and build that many test cases)
It is a separate submodule apart from the actual sub module we are testing.

Test Code verifies the real code (Production Code) works - never put them in the same file

Test Cases MUST be Repeatable: A test case must have the same outcome every time, until you change the software


#### Test Design – General Concept
*Tests must be designed before they can be coded:

1. <span style="color:#00b050">List your test cases. </span>
	► Production code usually has different logic for different situations. We want to test all of it. ► Each test case should cover a different situation.
	
2. <span style="color:#00b050">Pick test data (for each test case)</span>. 
	► That thing you’re testing? It (probably) needs some sort of input or import data. 
	► To test it, you have to give it some data. 
	► Choose the test data so that you’re testing the “right thing”. 
	
3. <span style="color:#00b050">Calculate expected results (for each test case).</span> 
	► A particular test data should give you a particular result. 
	► What should that result be? (If you don’t know, you can’t verify it!)

<span style="color:#ffea00">test code is in a seperate file to production code</span>
#### Black Box vs White Box

Black Box Tests are designed based on the submodule specification alone (don't need to see code)
White Box / Clear Box - Tests are designed by analysing the “paths” through the production code.


#### Equivalence Partitioning

<span style="color:#00b050"><span style="color:#00b050">Identify categories of behaviour</span></span> (eg. input number is negative, positive or 0)
<span style="color:#00b050">Then come up with an input for each category</span> (-5, 0, 5)
<span style="color:#00b050">Put into a Table</span> - example: 
![[Pasted image 20240429155852.png]]
Another example: 
![[Pasted image 20240429160013.png]]
Can be multiple imports - example: 
![[Pasted image 20240429160111.png]]

**Categories and Expected Results must be clear!

Corner Cases: 
- Special characters in strings/arrays
- Strings or Arrays could be empty eg. ""
- Null or None
- sometimes "0"


<span style="color:#00b050">Properties of Categories: </span>
1. Categories must be complete: Every possible import value must fit into a category.
		eg. For categories “x < 5” and “x > 5”, where does 5 go?
	All possibilities must fit into a category (so if there is two imports - it will have more possibilities!)

2. Categories should not be joined with an “OR”.
		eg. Don’t have a combined “x < 0 or x ≥ 100” category.

3. Categories should not overlap - they must be mutually exclusive
		eg. “x < 0” and “x < 100” can’t be two separate categories.

4. Don't try to test syntax errors: This is not about error handling! 
		We aren't testing things that won't even compile

<span style="color:#ffea00">Don't overlap categories</span>

#### BVA - Boundary Value Analysis
<span style="color:#00b050">Only applies to numerical imports</span>
► A “boundary value” is one step away from being in a different category.

A upper limit and lower limit for each boundary - this tests the +1 and -1 for each limit

This can be difficult with real numbers because it could be to many decimal points so just chose a number close to the edge of a boundary on either side
	eg. Boundary: Temperature < 25.5, and temperature ≥ 25.5. 
	Answer:  About 25.499999 (close enough), and also 25.5 exactly


#### Test Code

Our Test Code (Test Suite): 
1. Call the production code method, and pass it the test data. 
2. Receive the actual result from the production code. 
3. Compare the expected and actual results.
		► If they’re equal, the test passes. Otherwise, it fails. 
4. Repeat, for each different test case. 
		► Each test method will often run through several test cases

###### Use Assertion Statements
- Use: "assert"
	`assert condition, "message"`
	
- Condition: Checks if something is True or False by checking for equality
		`assert apples == oranges, "apples"`

	Checking Equality in Conditions
	- To compare everything except real numbers in Python, use “= =”: 
	- For Booleans, we can also just assert the value directly, 
				`"assert x"` 
					or 
				`"assert not y"` 	
				
	Checking Real numbers: use a tolerance value. 
		`assert abs(x - y) < 0.000001`

- Messages
	When a test fails, the message should help you understand which test failed.
	If True - then code did what expected - NOTHING HAPPENS
	if False - code has a bug - PROGRAM CRASHES


EXAMPLES OF IMPLEMENTING TEST CODE

1. Test Cases > Implementation

![[Pasted image 20240429162456.png]]


2. Implementation of all 3 findMax cases: 
![[Pasted image 20240429163818.png]]

3. If you had lots of test cases - put into a loop
![[Pasted image 20240429163924.png]]

4. Testing Suite example - overview look
![[Pasted image 20240429164052.png|400]]



![[Pasted image 20240506121338.png]]

Why does nothing print to screen when it is right? 
Only prints first incorrect test....
Answer: This is supposed to happen. Test Cases need to be fixed one by one so it one fails - it halts the test run code. 


#### Unit Test Frameworks (OPTIONAL)

Using built-in methods
Python: the standard “unittest” module.
https://docs.python.org/3/library/unittest.html


Advantages: 
- All tests run, even if one fails
- More meaningful error messages

Example: 
`file name : test_MyUtils.py` 
`import MyUtils # Our production code import` 
`unittest # The test framework` 
`Class MyUtilsTest(unittest.TestCase):` 
	`def testMax(self): ...` 
	`def testPalindrome(self): ...` 
	`def testFormatTime(self): ...`

For comparison: 

Non - Unit Test Framework:
`def testMax(): 
	`assert 20 == MyUtils.max(10, 20), "value1 < value2"` 
	`assert 10 == MyUtils.max(10, 5), "value1 = value2"`
	`assert 10 == MyUtils.max(10, 10), "value1 > value2“`

With Python's Unit-Test Framework: 
`def testMax(self):`
	`self.assertEqual(20, MyUtils.max(10, 20), "value1 < value2“)` 
	`self.assertEqual(10, MyUtils.max(10, 5), "value1 = value2" )` 
	`self.assertEqual(10, MyUtils.max(10, 10), "value1 > value2“)`
