1)  **Identify Variables**:
    - **Count Numerical and Categorical Variables**: eg. Numerical = 1/4 and Categorical = 3/4
2) Add 3 columns to table that say "numSim", "CatSim" and "Overall Sim"
3) **Calculate Similarity** between each class instance and the unclassed instance (this is repeated n times!):
    - **Numerical Similarity**:
		- numDist = |value of classed instance - value of unclassed instance|
						(note: if more than 1 numerical variable, data needs to be normalised and num distance for each categorical variable of that row added together)
		- numSim = 		$\frac{1}{1 + \text{numDist}}$
    - **Categorical Similarity**:
        - CatSim = Make it a 1 for every match in a categorical row between classed driver and unclassed driver and 0 if no match. Then divide answer by number of categorical rows
        - $CatSim = \frac{\text{2 matches}}{\text{3 categorical rows}} = 0.66$
4)  **Overall Similarity Calculation** (for each classed instance): $$\text{Overall Sim} = \frac{\text{No. of Num columns}}{\text{No. of columns}} \times \text{NumSim} + \frac{\text{No. of Cat columns}}{\text{No. of columns}} \times \text{CatSim}$$
5)  **Determine Class of Unclassed Instance**:
    - With k=1, find the class of the nearest classed instance (the one with the highest overall similarity).
    - If k > 1, group with closest k number of instances and choose majority class
