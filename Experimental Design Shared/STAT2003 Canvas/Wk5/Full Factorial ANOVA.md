$Y_{ij} = \mu + a_i + b_j + (ab)_{ij} + \epsilon_{ij}$

- $\mu$: Overall mean
- $a_i, b_j$: Main effects of factors A and B
- $(ab)_{ij}$: Interaction effects
- $\epsilon_{ij}$: Experimental error, normally distributed $N(0, \sigma^2)$

**Hypothesis:
$H_0 : \tau_1 = \tau_2 = ... \tau_n = 0$
$H_1 : \text{at least one } \tau \neq 0$
![[Pasted image 20250324085849.png|400]]

IN R: 
Use ANOVA to determine:
- Does **factor A** affect the response?
- Does **factor B** affect the response?
- Do **A and B interact**?

```
# Two-factor factorial design (includes interaction term)
model <- aov(Y ~ A * B, data = mydata)
summary(model)


```







