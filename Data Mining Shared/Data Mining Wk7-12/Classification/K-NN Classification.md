Consider the following data set about the evaluated risk of different drivers
![[Pasted image 20240910102943.png|400]]

Using nearest neighbour classification with k = 1, predict the risk with the following drivers. State your assumptions and show your working out.
![[Pasted image 20240910103009.png|400]]

--------
1. Work out how many numerical variables and how many categorical variables
		*Numerical = 1/4 columns and Categorical = 3/4 columns
2. Calculate similarity between unclassed driver and EACH classed driver
	- For numerical similarity:
		- numdist = |Age of each classed driver - Age of unclassed driver | + ...
					(note: if more than 1 numerical variable, data needs to be normalised and num distance for each categorical variable of that row added together)
		- numSim = 		$\frac{1}{1 + \text{num dist}}$
		
		*Numerical similarity between No.1 and No. 10: $\frac{1}{1 + (|25 - 45|)}$  = 0.047
	- For categorical: 
		CatSim = Make it a 1 for every match in a categorical row between classed driver and unclassed driver and 0 if no match. Then divide answer by number of categorical rows
		
		*CatSim between No. 1 and No. 10 =  1 + 1 + 1 = 3, 3/3 = 1

	- Calculate overall similarity: $$\text{Overall Sim} = \frac{\text{No. of Num columns}}{\text{No. of columns}} \times \text{NumSim} + \frac{\text{No. of Cat columns}}{\text{No. of columns}} \times \text{CatSim}$$
		*Overall Sim between 1 and 10:* $\frac{1}{4} \times 0.047 + \frac{3}{4} \times 1 = 0.76$
		
	- REPEAT FOR EVERY CLASSED DRIVER AND DRIVER 10
	- REPEAT FOR EVERY CLASSED DRIVER AND DRIVER 11


3. Group each unclassed driver with k-number of classed drivers and then look at the majority in the target variable (eg. "Risk"). 

| Classed Driver | Unclassed Driver | NumSim | CatSim | Overall Sim |
| -------------- | ---------------- | ------ | ------ | ----------- |
| 1              | 10               | 0.048  | 1      | 0.762       |
| 2              | 10               | 0.167  | 0      | 0.042       |
| 3              | 10               | 0.041  | 0.33   | 0.258       |
| 4              | 10               | 0.056  | 0.33   | 0.261       |
| 5              | 10               | 0.083  | 0      | 0.083       |
| 6              | 10               | 0.038  | 0.33   | 0.257       |
| 7              | 10               | 0.083  | 0      | 0.021       |
| 8              | 10               | 0.333  | 0.66   | 0.578       |
| 9              | 10               | 0.167  | 0.66   | 0.5367      |
k=1, Driver 10 is the same Risk as Driver 1 which is H


DO THE SAME FOR DRIVER 11
