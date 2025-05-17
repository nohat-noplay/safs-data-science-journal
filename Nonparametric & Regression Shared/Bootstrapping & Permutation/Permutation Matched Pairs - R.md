
```{r}
library(CarletonStats) #permutation package
set.seed(123) #makes it random
permTestPaired(data$dataA, data$dataB,  alternative = "greater"/"less")
