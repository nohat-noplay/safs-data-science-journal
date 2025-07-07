![[Pasted image 20250317133719.png]]
$$Y_{ijk} = \mu + \tau_i + \rho_j + \gamma_k + \epsilon_{ijk}$$

- $Y_{ijk}$ The response when the $i$th treatment is applied to the $j$th row and $k$th column.
- $\mu$ The overall (grand) mean.
- $\tau_i$ The effect of the $i$th treatment.
- $\rho_j$ The effect of the $j$th row/block (1st nuisance factor)
- $\gamma_k$ The effect of the $k$th column/block (2nd nuisance factor)
- $\epsilon_{ij}$ The random error term, assumed to be independently and identically distributed as $N(0, \sigma^2)$

$$SS_T = SS_{Treatment} + SS_{Rows} + SS_{Columns} + SSE$$
or
$$SSE = SS_T - ( SS_{\text{Treatment}} + SS_{\text{Rows}} + SS_{\text{Columns}})$$
where generalised Sum of Squares is: 
$$\sum (x_i - \bar{x_g})^2$$
`aov_LSD = aov(Y ~ treatment + factor(block1) + factor(block2), data=data)`
`summary(aov_LSD)`

