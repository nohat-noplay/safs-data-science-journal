After completing ANOVA for 2^3 factorial design (say A, B, C) - you could explore a reduced model (say A, C)
```
model <- aov(Y ~ factor(A) * factor(C), data = mydata)
summary(model)
```

**Convert into Regression Model

ANOVA:                    $Y_{ij} = \mu + a_i + c_i + (ac)_{ij} + \epsilon_{ij}$
REGRESSION:           $Y = \beta_\mu + \beta_A x_1 + \beta_C x_2 + \beta_{AC} x_1 x_2 + \epsilon$

```
reg_model <- lm(Y ~ A * C, data = mydata)
summary(reg_model)
```

see file:///C:/Users/safja/OneDrive/Desktop/2025%20Sem1%20Curtin%204/STAT2003%20Ana%20for%20Exp%20and%20Sim%20Data/Labs/Week7/STAT2003%20Analytics%20for%20Experimental%20and%20Simulated%20Data.html 
for matrix forms of ANOVA and regression comparison