to check for Equal Variances
Levene's test for homogeneity of variance tests the following hypotheses:
$H_0$: $\sigma_1 = \sigma_2 = ~...~ = \sigma_K$, where $K =~$ number of groups\
$H_A$: $\sigma_i \ne \sigma_j$ for some $i \ne j$
`library(car)`
`leveneTest(NUM.COL.NAME ~ CAT.COL.NAME, data=DATAFRAME.NAME)`
ptest needs to be close to 1 to use One Way ANOVA as it accepts NULL Hypothesis that variances are the same. 

(if reject Null - may need to do Welch ANOVA for unequal variance instead of F test)


The results of the ANOVA F test are approximately correct when the largest 
sample standard deviation is no more than twice as large as the smallest 
sample standard deviation. 