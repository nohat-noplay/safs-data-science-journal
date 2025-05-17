![[Pasted image 20241021131334.png|400]]True Positive = sum of n pairs (same class, same cluster) of each cluster (N(N-1)/2 of each type)
Cluster 1: 
4 circles is 4(4-1)/2 = 6 pairs
1 triangle is 0 pairs
1 square is 0 pairs
-> 6 pairs

Cluster 2: 
3 squares is 3 pairs
2 triangles is 1 pair
1 circle is 0 pairs
-> 4 pairs

Cluster 3: 
2 squares is 1 pair
2 triangles is 1 pair
1 circle is 0 pairs
-> 2 pairs

True Positive = 12 pairs

False Positive = sum of n pairs (different class, same cluster) of each cluster (type a $\times$ type b)
Cluster 1:
4 circles $\times$ 1 square = 4 pairs
4 circles $\times$ 1 triangle = 4 pairs
1 square $\times$ 1 triangle = 1 pair
-> 9 pairs

Cluster 2:
1 circles $\times$ 3 square = 3 pairs
1 circles $\times$ 2 triangle = 2 pairs
3 square $\times$ 2 triangle = 6 pair
-> 11 pairs

Cluster 3: 
1 circles $\times$ 2 square = 2 pairs
1 circles $\times$ 2 triangle = 2 pairs
2 square $\times$ 2 triangle = 4 pairs
-> 8 pairs

False Positive = 28 pairs

False Negative = sum of n pairs (same class, different clusters) of each class (type a in cluster a $\times$ type a in cluster b)

Class Squares:
Cluster 1: 1 $\times$ Cluster 2: 3 = 3 pairs
Cluster 1: 1 $\times$ Cluster 3: 2 = 2 pairs
Cluster 2: 3 $\times$ Cluster 3: 2 = 6 pairs
-> 11 pairs

Class Triangles:
Cluster 1: 1 $\times$ Cluster 2: 2 = 2 pairs
Cluster 1: 1 $\times$ Cluster 3: 2 = 2 pairs
Cluster 2: 2 $\times$ Cluster 3: 2 = 4 pairs
-> 8 pairs

Class Circles:
Cluster 1: 4 $\times$ Cluster 2: 1 = 4 pairs
Cluster 1: 4 $\times$ Cluster 3: 1 = 4 pairs
Cluster 2: 1 $\times$ Cluster 3: 1 = 1 pair
-> 9 pairs

False Negative = 28 pairs

Total Pairs = N(N-1)/2 = 17(17-1)/2 = 136
True Negatives = 136 - (12 + 28 + 28) = 68