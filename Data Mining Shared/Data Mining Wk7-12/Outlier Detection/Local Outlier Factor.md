??

Question 6
Consider the following set of one-dimensional data points
![[Pasted image 20241022070124.png|500]]
• Compute the distance-based outlier scores for all data points using the distance-based algorithm
with k = 3.
• Which data point has the highest outlier score using LOF with k = 3?

------------

Distance-based algorithm:

| Point | Value | k_Neighbours | Outlier Score (k = 3)                           |
| ----- | ----- | ------------ | ----------------------------------------------- |
| A     | 10    | B, C, D      | 13 (furtherest neighbour value - point value  ) |
| B     | 21    | C, D, E      | 24 - 21 = 3                                     |
| C     | 22    | B, D, E      | 24 - 22 = 2                                     |
| D     | 23    | B, C, E      | 2                                               |
| E     | 24    | B, C, D      | 3                                               |
| F     | 100   | G, H, I      | 60                                              |
| G     | 120   | F, H, I      | 40                                              |
| H     | 140   | F, G, I      | 40                                              |
| I     | 160   | G, H, J      | 40                                              |
| J     | 190   | G, H, I      | 70                                              |








Local Outlier Factor: 

1. Compute k-distance of each point
2. Calculate the reachability distance
3. Compute local reachability density (LRD)
4. Calculate LOF


A -> 3 neighbours
k-reachability value -> 11 + 12 + 13 = 36 
k-reachability density = 3/36
neighbourhood density = 
LOF = 


------------
