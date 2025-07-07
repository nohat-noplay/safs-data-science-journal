Contrasts are used to test a specific hypothesis about group differences 

1. **Compute the contrast estimate**:
$\hat{L} = \sum c_i \bar{Y}_i \ \ \ \ ⇒ \ L= \bar{Y_1}- \frac{1}{2}​(\bar{Y_2}​+\bar{Y_3}​) \ ⇒ \ \ C = [1, -0.5, -0.5]$
_$Y_1$ is the level being compared against $Y_2$ & $Y_3$

2. **Compute the standard error** (equal sample sizes):
$SE(\hat{L}) = \sqrt{MSE \cdot \sum \frac{c_i^2}{n_i}}$ where $c_i$ could be 1 or -0.5 or -0.5 and $n_i$ is sample size per group

3. **Compute the t-statistic**:
$t = \frac{\hat{L}}{SE(\hat{L})}$

4. Compare $t_{\alpha/2 , N-K}​$ from the **t-table**.
- $df=N−K$

Reject $H_0$ if $|t| > t_{\alpha/2}$
