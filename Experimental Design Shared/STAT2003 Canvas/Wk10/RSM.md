- $FO: y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \varepsilon$
- SO: $y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_{11}x_1^2 + \beta_{22}x_2^2 + \beta_{12}x_1x_2 + \varepsilon$

1. If factorial design shows non-linearity/curvature: add 4 centre (encode 1 variable as 0 at a time) and 4 axial points (encode 1 variable as $\sqrt{2}$ at a time) _for rotatability_.

| x1         | x2         |           |
| ---------- | ---------- | --------- |
| -1         | -1         | Factorial |
| 1          | -1         | Factorial |
| -1         | 1          | Factorial |
| 1          | 1          | Factorial |
| 0          | 0          | centre    |
| 0          | 0          | centre    |
| 0          | 0          | centre    |
| 0          | 0          | centre    |
| $\sqrt{2}$ | 0          | axial     |
| $\sqrt{2}$ | 0          | axial     |
| 0          | $\sqrt{2}$ | axial     |
| 0          | $\sqrt{2}$ | axial     |

2. Fit FO linear model `lm(response ~ x1 + x2 + I(x1 * x2)` 
3. Predict centre points `predict(model_linear, newdata = data.frame(x1 = 0, x2 = 0))`
4. Compare predicted vs actual centre points. If the responses are significantly different to predicted ones - there is curvature and quadratic model needed. 
5. Optional: run lack of fit test with anova() for replicate centre points. 
6. Use axial points to fit quadratic (polynomial) model 
`lm(Response ~ x1 + x2 + I(x1*x2) + I(x1^2) + I(x2^2)` <- this is a Central Composite Design model (CCD). Note: You need at least 3 points to fit quadratic (-1, 0, 1 (or use axial))
7. Check assumptions and transform if needed