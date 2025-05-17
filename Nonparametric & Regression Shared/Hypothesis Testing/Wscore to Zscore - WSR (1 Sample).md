
1.Wscore plus or minus 0.5 = $W^+$ for Continuity Correction 
	-  if $H_1$ is greater than $H_0$ then minus 0.5 (closer to median)
	- if $H_1$ is less than $H_0$ (or not equal) then plus 0.5 (closer to median)
2.Work out mean of $W^+$ ($mu_W^+$) REMEMBER: $n$ = n-ties
$\mu_{W^+} =\frac{n(n+1)}{4}$
3.Work out the Standard Deviation $\sigma_{W^+} = \sqrt{\frac{n(n+1)(2n+1)}{24}}.$
4.Work out Zscore from $W^+(\pm0.5)$, $\mu_W^+$, $\sigma_W^+$ $z=\frac{((W^+ \pm 0.5) - \mu_{W^+})}{\sigma_{W^+}}.$
5.`pnorm(z)` (if lower.tail is FALSE: `1-pnorm(z)`) (if two.sided: `2*pnorm(z)`)

