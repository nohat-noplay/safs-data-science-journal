

```
cor.test(x=data$xvariable, y=data$yvariable,
        alternative="greater",  # H_A: true correlation is greater than zero
         method= c("pearson", "kendall", "spearman")
```