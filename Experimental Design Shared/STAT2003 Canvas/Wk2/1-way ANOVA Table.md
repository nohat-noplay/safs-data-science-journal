1 way ANOVA is analysing the effect of a single factor _eg. fertilizer_ on a response _eg. tomato yield weight_
$$Y_ij = \mu + \tau_i + \epsilon_{ij}\sim N(0,\sigma^2)$$
```
aov_CRD <- aov(Y ~ treatment, data = data)
summary(aov_CRD)
```

| Source                        | Sum of Squares                                                  | Degrees of Freedom   | Mean Sum of Squares                    | F-Test Statistic       |
| ----------------------------- | --------------------------------------------------------------- | -------------------- | -------------------------------------- | ---------------------- |
| Treatments _(between groups)_ | $SS_{tre} = \sum n_g (\bar{x}_{g} - \overline{\overline{x}})^2$ | $df_{tre} = K - 1$   | $MS_{tre} = \frac{SS_{tre}}{df_{tre}}$ | $\frac{SS_{tre}}{SSE}$ |
| Errors _(within groups)_      | $SSE = \sum (x_i - \bar{x_g})^2$                                | $df_E = N - K$       | $MSE = \frac{SSE}{df_E}$               |                        |
| Total                         | $SS_{total} = SS_{tre} + SSE$                                   | $df_{total} = N - 1$ |                                        |                        |

- $x_i$ is for each observation (score) in the $g$th treatment group 
- $n_g$ is number of observations (teacher scores) in the $g$th treatment group
- $\bar{x_g}$ is the $g$th treatment group mean score
- $\overline{\overline{x}}$ is the overall mean score (all teacher scores of treatment groups)
- $K$ is number of treatment groups
- $N$ is the total number of observations (scores) across all groups

$F_0$ is  our test statistic. 
Use F-table to look up the **critical value** $F_{\alpha, df_1, df_2}$ for your chosen significance level (usually $\alpha = 0.05$)
- If $F_0 \gt F_{\alpha, df_1, df_2}$​​ → **Reject H_0 
    → At least one group mean is significantly different
- If $F_0 \le F_{\alpha, df_1, df_2}$ → **Fail to reject H_0​**  
    → No evidence of group differences