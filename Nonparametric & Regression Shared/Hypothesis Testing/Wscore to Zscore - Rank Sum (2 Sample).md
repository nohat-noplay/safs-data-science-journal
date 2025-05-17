
1.Calculate the mean ($\mu_W$)  $\mu_W = \frac{n_1(N+1)}{2}$
2.Calculate standard deviation ($\sigma_W$) of $W$ for the smaller $W$ $\sigma_W = \sqrt{\frac{n_1n_2(N+1)}{12}}$$
3.Calculate Z Test Statistic ($z$) $\pm$ 0.5 = $W^+$ for Continuity Correction 
	-  if $H_1$ is greater than $H_0$ then minus 0.5 (closer to median)
	- if $H_1$ is less than $H_0$ (or not equal) then plus 0.5 (closer to median)
$z = \frac{(W \pm 0.5) - \mu_W}{\sigma_W}$
4. `pnorm(z)` (if lower.tail is FALSE: `1-pnorm(z)`) (if two.sided: `2*pnorm(z)`)