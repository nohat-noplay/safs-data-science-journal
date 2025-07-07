
EXAMPLE: 

-----------------------------------------
A researcher studies the effect of two fertilizers (A and B) on plant growth.  
However, soil moisture varies and may affect growth, so soil moisture (%) is measured for each plant.  
The following summary statistics are given:

| Group        | Mean Growth (cm) | Mean Soil Moisture (%) | Sample Size (n) |
| ------------ | ---------------- | ---------------------- | --------------- |
| Fertilizer A | 20 cm            | 10%                    | 5               |
| Fertilizer B | 26 cm            | 12%                    | 5               |

Overall mean soil moisture = 11%
Assume:
- The relationship between soil moisture and growth is linear.
- Regression slope ($\beta$) for soil moisture = 1.5 (cm increase per 1% increase in moisture).
- The residual mean square (error variance) is known to be 2.
Test if fertilizer type affects plant growth after adjusting for soil moisture at $\alpha = 0.05$.
-------------------------------------------------

1. Write model and identify terms
$$Y_{ij} = \mu + \tau_i + \beta(X_{ij} - \bar{X}) + \epsilon_{ij}$$
	- $Y_{ij}$ = growth for plant j under fertilizer i
	- $X_{ij}$= soil moisture
	- $\bar{X} = 11\%$ = overall mean soil moisture
	- $\beta = 1.5$

2. Adjust treatment means

	Adjusted Group Mean = Raw Group Mean - $\beta$(Group Mean Covariate - Overall Covariate Mean)

Fertilizer A: 20 - 1.5(10 - 11) = 21.5
Fertilizer B: 26 - 1.5(12 -11) = 24.5

3. Compare Adjusted means and calculate overall adjusted mean
	- Fertilizer A: **21.5 cm**
	- Fertilizer B: **24.5 cm**
	Adjusted means are **different** → 

	Overall Adjusted Mean = $\frac{21.5 + 24.5}{2} = 23$

4. Calculate SST (Sum of Squares Treatment) & dfT, dfE:
	If sample sizes are equal (n observations per group):
	$SST = n \sum (\bar{Y}_i - \bar{Y})^2$
	If sample sizes are unequal:
	$SST = \sum n_i (\bar{Y}_i - \bar{Y})^2$
	
	$5(21.5 - 23)^2 + 5(24.5 - 23)^2 = 22.5$

	dfT = k -1 (k is number of groups) $\rightarrow$ 1
	dfE = N - k $\rightarrow$ 8

5. Calculate MST and MSE:
$MST = \frac{SST}{dfT} = 22.5$
$MSE = \frac{SSE}{dfE} = 2 (given)$

6. Calculate F Statistic: 
$F= \frac{MS_{Treatment}}{MS_{Error}​​} = \frac{22.5}{2} = 11.25$

7. Conclusion: 
- Compare $F(1,8)$ to critical value at $\alpha=0.05$ (use book: critical F around 5.32).
    
- $11.25 > 5.32 $ **Reject $H_0$​**

> "After adjusting for soil moisture, there is **significant evidence** that the fertilizers differ in plant growth, $F(1,8) = 11.25$,     $p < 0.05.$"
