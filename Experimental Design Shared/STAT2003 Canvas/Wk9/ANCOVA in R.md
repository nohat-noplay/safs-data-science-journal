1. Check ANCOVA assumption of "Homogeneity of slopes" with plotting
```
library(ggplot2)

ggplot(DATA, aes(x=COVAR, y=YVAR, col=FACTOR(XVAR))) + geom_point(aes(fill=FACTOR(XVAR))) + geom_smooth(method = "lm", se = FALSE)
```

2. **Fit linear Model including interaction:**  
```
# Modelling ANCOVA to determine if interaction  is significant
options(contrasts = c("contr.sum", "contr.poly")) # handle categorical variables
model1 <- lm(YVAR ~ FACTOR(XVAR) + COVAR + FACTOR(XVAR):COVAR, data=DATA)  # linear model
anova(model1) # F test - how significant each term is
```

IF INTERACTION TERM > 0.05 (which it must for ANCOVA - slopes are paralell)
4. **Fit Simpler linear model without interaction:**  
```
getOption("contrasts") # handle categorical variables
model2 <- lm(YVAR ~ FACTOR(XVAR) + COVAR, data=DATA)  # linear model
drop1(model2, ~., test="F") # F test - how significant each term is
```

4. Perform ANOVA
```
summary(aov(model2))
```


3. Show Linear Model to get coefficients in output to write lm formula
```
model2
```
Is treatment effect (variable) < 0.05? Significant evidence WITH covariate adjustment



5. Check Assumptions
```
par(mfrow=c(2,2))
plot(model2)
```
