_eg. Compare Organic (Group 1) vs. the average of Chemical and No Fertilizer (Groups 2 and 3)_
_Assume:
Factor: **Fertilizer Type**
- *Group 1: Organic    Group 2: Chemical    Group 3: No Fertilizer*
- *Equal sample size: $n_i=5$ plants per group*
- *Treatment means (average tomato weight per group):*
  *$\bar{Y}_1 = 450\text{g}, \quad \bar{Y}_2 = 390\text{g}, \quad \bar{Y}_3 = 300\text{g}$*
- *MSE from ANOVA: $MSE=900$*

 **Step 1: Set up the contrast**
$L= \bar{Y_1}- \frac{1}{2}​(\bar{Y_2}​+\bar{Y_3}​) \ ⇒ \ \ C = [1, -0.5, -0.5]$

**Step 2: Calculate the contrast estimate $\hat{L}$**
$\hat{L} = 1(450) - 0.5(390) - 0.5(300) = 450 - 195 - 150 = 105$

**Step 3: Compute the standard error**
$SE(\hat{L}) = \sqrt{MSE \cdot \sum \frac{c^2_i}n_i} = \sqrt{900 \cdot \left(\frac{1^2 + 0.5^2 + 0.5^2}{5}\right)} \approx 16.43$

**Step 4: Compute t-statistic**
$t = \frac{\hat{L}}{SE(\hat{L})} = \frac{105}{16.43} \approx 6.39$

 **Step 5: Compare to critical t-value**
Degrees of freedom: $df = N - K = 15 - 3 = 12$
At $\alpha = 0.05$ two-sided (so divide $\alpha$ by 2):
$t_{0.025, 12} \approx 2.18$
Since $6.39 > 2.18$
**reject $H_0$.

**Conclusion**:
> *"There is strong evidence that **Organic fertilizer yields significantly more tomatoes than the average of the other two types**."*