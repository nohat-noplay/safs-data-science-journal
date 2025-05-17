How do we predict the missing rating?
![[Pasted image 20241022094035.png|400]]

## Approach 1: User Based similarity with ratings:

1. Compute average rating of each user (excluding the column of the item we need to predict)
![[Pasted image 20241022094315.png|400]]

2. Centralise ratings of row around the mean of that row ($x_i - \bar{x}$)
![[Pasted image 20241022094422.png|400]]

3. Compute the norm of the centralised ratings $\sqrt{\sum({x_i}^2)}$
![[Pasted image 20241022094719.png|400]]

4. Compute Pearson correlations between User with missing item and all other users (one by one)
$$\text{Pearson}(\bar{X}, \bar{Y}) = \frac{(x_1 - \bar{x})(y_1 - \bar{y})+...+(x_s - \bar{x})(y_s - \bar{y})}{\sqrt{(x_1 - \bar{x})^2 + ... + (x_s - \bar{x})^2} \cdot \sqrt{(y_1 - \bar{y})^2 + ... + (y_s - \bar{y})^2}}$$
	![[Pasted image 20241022095722.png|400]]
	Note: If there is a 0 in the column, no need to include it in the calculation (in the example; Assessor 1 has rated App 1 and App 3 as 0):

5. Pick highest correlation Assessor (Assessor 5) then compute predicted item"
	$\text{Average rating of Assessor 1} + (\text{Assessor 5's rating for missing column} - \text{Assessor 5's mean for all columns})$	![[Pasted image 20241022100513.png|400]]
