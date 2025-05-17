True Positives (TP)
Count pairs of points in same class and in  same cluster:
- For each cluster, count pairs within each class (e.g., circles, squares, triangles) using the formula:
    $\frac{n(n-1)}{2}$    where $n$ is the number of points of the same class within the cluster.
    eg. Cluster 1: 4 circles is 4(4-1)/2 = 6 pairs...
- Sum these counts across all clusters.

False Positives (FP)
Count pairs of points in same cluster but different class (type):
- For each cluster, calculate pairs between each pair of classes (e.g., circles and squares)
eg. Cluster 1: 4 circles $\times$ 1 square = 4 pairs
- Sum these across all clusters.

False Negatives (FN)
Count pairs of points belonging to same class but in different clusters:
- For each CLASS, compute pairs across clusters, multiplying the number of points of that class in one cluster by the number in another cluster (only do 2 clusters at a time - $C1 \times C2,  C1 \times C3, C2 \times C3$)
eg. Class Squares: Cluster 1: 1 $\times$ Cluster 2: 3 = 3 pairs
- Sum up all pairs of a class together. 

 True Negatives (TN)
- Calculate total pairs -> Total Pairs = N(N-1)/2 where N is number of points across all clusters
- TN = Total pairs - TP, FP, FN

