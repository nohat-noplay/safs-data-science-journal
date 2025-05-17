1. Check data for normality using [[Shapiro-Wilk Test for Normality]]
2. Define Function for calculating mean of resamples: 
```{r}
theta <- function(data,indices) {
  d <- data[indices]
  mean(d)
}
```
3. Load boot library and use set.seed to reproduce the same generated samples (use 10 resamples for example) - to see resample means type at the top `{r echo=TRUE, eval=TRUE}`
```{r}
# load boot library
require(boot)

# Generate bootstrap distribution
set.seed(1234) #this is for randomisation (can use any 4 digit number)
data.boot1 <- boot(data, theta, 10) # 10 resampling 
data.boot1  # output of bootstrapping
``
![[Pasted image 20240826121226.png|300]]
4. Create matrix of resampling and then get summary statistics OR plot histogram. Check if normal
```{r}
{r}
data.boot1$t ## a matrix consists of the statistics from n resampling, n=1,...10 bootstrap sample means b=1,2,...,10
summary(data.boot1$t) ## summary statistics from B=10
data.boot1$t0 ## the original sample mean
```
5. Confidence Interval (boot)
_The_ $t$-interval relies on the central limit theorem and hence is symmetric about the sample mean; no such restriction is required for the bootstrap interval.
```{r}
# mean and 95% bootstrap confidence interval
mean(data.boot1)
quantile(data.boot1, c(0.025, 0.975))
```
