Nonparametric test that tests if two continuous distributions, whether or not they have the same shape

1.Collect samples of size $n_1$ from pop 1, collect samples of size $n_2$ from pop 2. 
	$N = n_1 + n_2$
	
2.Rank all $N$ observations, keeping track which observation comes from which sample:
	eg. ![[Pasted image 20240805120916.png|350]]

3 Find Wilcoxon Rank Sum Statistic by adding ranks of  Sample 1 together this is $W_1$. Do the same for Sample 2, $W_2$. 

4. Calculate $\mu$ of the smallest W (either $W_1$ or $W_2$): $\mu_1 = W_1 - \frac{n_1(n_1 + 1)}{2}$
5. `pwilcox(mu, n_1 n_2)`
OR
[[Wscore to Zscore - Rank Sum (2 Sample)]]