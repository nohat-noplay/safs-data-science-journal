Density-Based Spatial Clustering of Applications with Noise
**Epsilon (ε)** - the radius around a point used to define its neighborhood.
- **Impact**: A larger ε means points farther from each other may still be clustered together, creating larger clusters. A smaller ε requires points to be closer for clustering, creating more compact clusters.
**MinPts** - the minimum number of points required within the ε-radius for a point to be considered a “core point.”
    - Core Point: If a point has at least MinPts neighbors within the ε-radius, 
    - Border Point: If it has fewer than MinPts neighbors but is within the ε-radius of a core point, 
    - Outlier: Points with fewer than MinPts neighbors that are not within any core point’s ε-radius are classified as **noise** (outliers).
- **Impact**: Higher MinPts values make clusters more dense, as each core point needs more neighbors to form a cluster.