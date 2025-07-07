BEFORE EXPERIMENT: Determine blocking to be confounded
```
library(FrF2)

# FrF2(no-of-runs, no-of-factors, default.levels = c("+", "-"), blocks=c("block-to-be-confounded"),randomize = FALSE)

confoundABCD <- FrF2(16,4, default.levels = c("+", "-"), blocks=c("ABCD"),randomize = FALSE)
confoundABCD
```
Then add Block column assigning the block designation to data (ie. 1or 2) - ready for ANOVA

```
Q2data <- read.csv('Question7.2.csv', colClasses = c(rep('factor', 4), 'numeric', 'factor'))
# View(Q2data)
str(Q2data)

# ANOVA of full model with assigned Blocks (confounded ABCD) - no p values as there is no residuals?
# Must do it long way (instead of 'A * B * C * D + Block') to remove confounding factor

fullmodelq2 <- aov(Response ~ A + B + C + D + A:B + A:C + A:D + B:C + B:D + C:D + A:B:C + A:B:D + A:C:D + B:C:D + Block, data=Q2data)
summary(fullmodelq2)

# Due to no p values:
# use DanielPlot to see which Effects are significant (those furtherest away from 0 (the ones labelled))

library(FrF2)
DanielPlot(fullmodelq2, alpha=0.05)
```

![[Pasted image 20250414133808.png]]

```
# then perform ANOVA on only the effects that are significant

reducedmodel <- aov(Response ~ A + C + D + A:D + A:C + Block, data = Q2data)
summary(reducedmodel)

# Checking ANOVA assumptions
opar <- par(mfrow = c(2, 2), cex = .8)
plot(reducedmodel)

# Homoscedacity and Normality look fine but just double checking normality 
shapiro.test(residuals(reducedmodel))

# Checking interactions to see relationships (particularly how we can decrease formalahyde (C) in the mixture but still produce high filtration rate)
library(phia)
plot(interactionMeans(reducedmodel))
```

![[Pasted image 20250414133900.png]]

## Conclusion?

