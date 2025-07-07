
```
library(FrF2)
confoundedDesign2 <- FrF2(16, 4, 
                          default.levels = c("+", "-"), 
                          blocks = c("ABC", "ACD"),
                          alias.block.2fis = TRUE,
                          randomize = FALSE)
confoundedDesign2
```
