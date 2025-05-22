
Each module has 3 types of components:
- sequential tasks: task, then next task etc.
- decision making: if, else statements
- loops - while, for 

White Box testing - test cases are based on the paths through a function
A path is a possible way to get through a function start to end. 
There can be 1 or more paths
An extra path for each if else statement result

| Path                             | Test Data | Expected Result |
| -------------------------------- | --------- | --------------- |
| 1. Enter the if                  | n = -5    | 5               |
| 2. Do NOT enter the if (or else) | n = 10    | 10              |

*note that if print statement are strings*

###  Loop Paths
While and For Loops - paths

For loop doesn't create more paths, it just has two paths where it enters the loop and not enters the loop

If going into loop and doesn't exit without another input, your Test Data can look like this
input: "-5\\n10"
which means first input and then second input. 

### Exception Handling 
paths for exception handling...

### Nested Loops
