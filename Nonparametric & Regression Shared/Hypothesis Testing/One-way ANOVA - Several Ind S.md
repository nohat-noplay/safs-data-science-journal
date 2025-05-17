FIRST: Conduct [[Levene Test]] OR (Test: largest sd of a group is no more than twice size of smallest sd of a group) to check assumption of Equal Variance (required for One Way ANOVA)

Analysis of Variance F Test
Tests for difference between the means of several populations ($> 2$)
$F_o$ Test Statistic: $\frac{MSG}{MSE}$
$MSG$ = Mean Square for Groups *(Step 1)*
$MSE$ = Mean Square for Error ($S_p^2$ : pooled standard deviation) *(Step 2)*

1.Find MSG (Mean Sum of Squares among group): $\frac{\sum n_g(\bar{x_g} - \overline{\overline{x}})^2}{K-1}$
	- $n_g$ is number of items in group
	- $\bar{x_g}$ is the group mean
	- $\overline{\overline{x}}$ is the overall mean
	- $K$ is number of groups ($K-1$ is the Degrees of Freedom $df_1$)
2.Find MSE (Mean Sum of Squares within group) for each group: $\frac{\sum (x_i - \bar{x_g})^2}{N-K}$
	- $x_i$ is for each item in the group
	- $\bar{x_g}$ is for the group mean
	- $N - K$ (Degrees of Freedom $df_2$) is overall number of items $N$ minus number of groups $K$ 
3.Find F statistic by $F_o$ Test Statistic: $\frac{MSG}{MSE}$
p-value: `pf(Fstat, df_1, df_2)`