![[Pasted image 20250317132101.png]]
#### Two Way ANOVA
$$Y_{ij} = \mu + \tau_i + \beta_j + \epsilon_{ij}$$
- $Y_{ij}$ The response from the $j$th experimental unit receiving the $i$th treatment.
- $\mu$ The overall (grand) mean.
- $\tau_i$ The effect of the $i$th treatment.
- $\beta_j$ The effect of the $j$th block (accounting for known variability)
- $\epsilon_{ij}$ The random error term, assumed to be independently and identically distributed as $N(0, \sigma^2)$

`aov_RBD = aov(Y ~ treatment + block1, data=data)`
`summary(aov_RBD)`
