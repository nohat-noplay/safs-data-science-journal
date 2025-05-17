$L_p norm$: Minkowski distance is difference between 2 points (how dissimilar they are)

Without weights: 
$$Dist(\bar{X}, \bar{Y}) = (\sum |x_i - y_i|^p)^{1/p}$$
$$=(|x_1 - y_1|^p+...+|x_d - y_d|^p)^{1/p}$$
With weights (Domain specific relevance): 
$$Dist(\bar{X}, \bar{Y}) = (\sum w_i|x_i - y_i|^p)^{1/p}$$
$$=(w_i \times(|x_1 - y_1|^p)+...+w_d\times(|x_d - y_d|^p)^{1/p}$$
$p= 1$: Manhattan distance - sum of absolute distances
$p = 2$: Euclidean distance - straight line distance between 2 points
$p= \infty$: Chebyshev distance - the greatest of their differences (only largest feature matters):  
	$max(|x_i - y_i|, ..., |x_d, y_d|)$

Note:
- 'Curse of dimensionality' - $L_p$ distance less effective when dimensionality increases
- Feature Irrelevance - feature relevant to 1 group but not to others
- Larger $p$ tends to emphasize irrelevant features
- Data distribution influences distance by two types:
	- Type 1 - Density: High data density can indicate significant differences
	- Type 2 - Orientation: Point to point jumps can follow curved data. 
	
	
For Non-Linear distributions:
Intrinsic dimension (much smaller than raw data dimension)
Manifold learning (techniques to reveal the non-linear structure of data)
Geodesic distance (instead of of Euclidean distance)
ISOMAP embedding (for learning data manifold)

	ISOMAP
	1. Use k-nearest neighbour graph G to describe how data points are
	distributed
	2. Distance defined as shortest path between the corresponding nodes in G
