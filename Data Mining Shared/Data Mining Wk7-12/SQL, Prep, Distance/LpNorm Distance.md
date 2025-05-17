$L_p norm$:  distance is difference between 2 points (how dissimilar they are)

With weights (Domain specific relevance): 
$$Dist(\bar{X}, \bar{Y}) = (\sum w_i|x_i - y_i|^p)^{1/p}$$
$$=(w_i \times(|x_1 - y_1|^p)+...+w_d\times(|x_d - y_d|^p)^{1/p}$$
$p= 1$: Manhattan distance - sum of absolute distances
$p = 2$: Euclidean distance - straight line distance between 2 points
$p= \infty$: Chebyshev distance - the greatest of their differences (only largest feature matters):  
	$max(|x_i - y_i|, ..., |x_d, y_d|)$

Issues with LpNorm:
- 'Curse of dimensionality' - $L_p$ distance less effective when dimensionality increases
- Feature Irrelevance - feature relevant to 1 group but not to others
- Larger $p$ tends to emphasize irrelevant features
- Data distribution influences distance by Density & Orientation