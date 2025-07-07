1. Determine and state: Factors and their levels

| Factor      | +   | -   |
| ----------- | --- | --- |
| A: Reactant | 25% | 15% |
| B: Catalyst | 2lb | 1lb |

2. Determine Randomisation

assumed the Factors were randomly chosen within each block

3. Determine Replications and therefore runs

Factorial $\times$ _"replicated 3 times"
$2^2 \times 3 = 12 \ runs$

3. Determine Blocking

_"only four experimental trials can be made from a single batch of raw material. Therefore, three batches of raw material will be required to run all three replicates of this design"_

Batches require blocking to control unwanted variability between batches

4. Set up Treatment table 

|Treatment|Block 1|Block 2|Block 3|
|---|---|---|---|
|I|28|25|27|
|a|36|32|32|
|b|18|19|23|
|ab|31|30|29|

------------

1. Import Data (this data has already been converted to 1 and -1 for levels of A and B with columns: A, B, Block, Response)

```
# import data and turn Factors (1, -1) in factors, Blocks (1, 2, 3) into factors and response into numeric data type.

data <- read.csv('data.csv', colClasses = c(rep('factor', 3), 'numeric'))

# check column types
str(Q1data)
```
![[Pasted image 20250414110038.png]]

2. Fit ANOVA to full factorial model with a + b + a:b + Block (make sure block column is called "Block")

```
fullmodel <- aov(response ~ A+B+A:B+Block, data= data)
summary(fullmodel)
```

![[Pasted image 20250414110241.png]]
Interpretation: 
- A and B (Main Effects) have a significant effect on response (Pr(>F) < 0.05) _you can see this in the original data comparing numbers in Factor A and B_
- Blocking factor did not significantly reduce variance (influence outcome) _you can see this in the original data comparing numbers in columns_
- The interaction between A and B is not significant

3. Visualise interactions
```
library(phia)
plot(interactionMeans(fullmodel))
```
![[Pasted image 20250414113537.png]]

4. Check Assumptions 
- check plots first and if normality of variance looks off - check them with shapiro or/and levenes
```
#Underlying assumptions
opar <- par(mfrow=c(2,2),cex=.8)
plot(fullmodel)

#normality
shapiro.test(residuals(fullmodel))

#homoscedacity to be done separately
leveneTest(residuals(fullmodel) ~ A, data = Q1data)
leveneTest(residuals(fullmodel) ~ B, data = Q1data)
leveneTest(residuals(fullmodel) ~ Block, data = Q1data)
```
![[Pasted image 20250414113823.png]]

