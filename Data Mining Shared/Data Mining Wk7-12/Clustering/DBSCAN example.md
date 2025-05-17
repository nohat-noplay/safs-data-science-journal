
A data set consists of seven 2-dimensional data points shown in the figure below. Suppose that the
DBSCAN method is used. Identify core points, border points, and noise/outlier points in the following
cases
• minpts = 2, ε = 1
• minpts = 2, ε = 2
• minpts = 2, ε = 3
• minpts = 3, ε = 3
![[Pasted image 20241021131310.png|400]]

--------
- $\epsilon$  neighbourhood radius (length)
- $MinPts$ number of points that define a threshold for core points

• minpts = 2, ε = 1
Boundary: 
Core: 
Outlier: A, B, C, D, E, F, G

• minpts = 2, ε = 2
Boundary: B, F, G
Core: A, D, E
Outlier: C

• minpts = 2, ε = 3
Boundary: B, F
Core: A, C, D, E, G
Outlier:

• minpts = 3, ε = 3
Boundary: B, C, F
Core: A, D, E
Outlier: