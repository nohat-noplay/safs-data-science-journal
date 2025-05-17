Compute the Gini index for Past Trend
![[Pasted image 20241030150852.png|300]]
2 class problem:
1. Identify ID Variable to compute Gini Index for, number of instances, number of 1 and number of 0
$n$ = Gini Index for Past Trend, 10, 
ID Variable = Past Trend (Positive = 1, Negative = 0)
$N_1$ = Positive: 6
$N_0$ = Negative: 4

2. Identify Target Variable and how many each in ID Variable for each in Target
Target Variable: Return (Up = 1, Down = 0)

Past Trend: Positive (1) and Return: Up (1)= 4
Past Trend: Positive (1) and Return: Down (0)= 2
Past Trend: Negative (0) and Return: Up (1) = 0
Past Trend: Negative (0) and Return: Down (0)= 4

3. Calculate Gini Index for Each Value of ID Variable:
$Gini_{ID variable=1} = 1 - ((\frac{\text{ID Variable=1, Target = 1}}{N_1})^2 + (\frac{\text{ID Variable = 1, Target = 0}}{N_1})^2))$
$Gini_{\text{Past trend: Positive (1)}} = 1 - ((\frac{4}{6})^2 + (\frac{2}{6})^2) = 0.45$
$Gini_{ID variable=0} = 1 - ((\frac{\text{ID Variable=0, Target = 1}}{N_0})^2 + (\frac{\text{ID Variable = 0, Target = 0}}{N_0})^2)$$Gini_{\text{Past trend: Negative (1)}} = 1 - ((\frac{0}{4})^2 + (\frac{4}{4})^2) = 0$

4. Calculate Weighted Gini Index:
$WG = Gini_{ID variable=1} \times \frac{N_1}{n} + Gini_{ID variable=0} \times \frac{N_0}{n}$
$WG = 0.45 \times \frac{6}{10} + 0 \times \frac{4}{10} = 0.27$
