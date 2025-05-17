1. **Start with a dataset of points**
2. **Choose k**: Decide on the number of clusters
3. **Initialize Centroids**: Randomly select k points from the dataset as initial centroids
4. **Assign Points to Clusters**: For each point, identify the nearest centroid and assign the point to that cluster
5. **Calculate New Centroids**: For each cluster, compute the mean of the points to find the new centroid
6. **Update Centroids**: Move each centroid to the new mean position of its cluster
7. **Repeat** steps 4–6 until centroids stabilize (no significant movement) or a maximum number of iterations is reached

eg. 
Iteration 1: 
Centroids at 1 and 2. 
Cluster 1: {1}
Cluster 2: {2, 3, 4, 5, 6, 7, 8, 9, 10}

Iteration 2: 
Centroids at 1 (mean of 1) and 6 (mean of {2, 3, 4, 5, 6, 7, 8, 9, 10})
Cluster 1: {1, 2, 3} 
Cluster 2: {4, 5, 6, 7, 8, 9, 10}

Iteration 3: 
Centroids at 2 (mean of {1, 2, 3}) and 7 (mean of {4, 5, 6, 7, 8, 9, 10})
Cluster 1: {1, 2, 3, 4}
Cluster 2: {5, 6, 7, 8, 9, 10}
