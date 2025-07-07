```
data <- read.csv("data.csv", colClasses = c("factor", "factor", "numeric"))
str(data)
summary(data)
boxplot(data$Y ~ data$X, col=c("yellow", "red", "blue"))

```