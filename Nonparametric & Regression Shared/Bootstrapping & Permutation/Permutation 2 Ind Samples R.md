```{r}
library(CarletonStats) #permutation package
set.seed(123) #makes it random
permTest(data$num_data, data$cat_data,  alternative = "greater"/"less")
