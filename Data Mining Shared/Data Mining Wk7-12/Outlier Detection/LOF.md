1.ID k and make table

| Point | Value | K-neighbours | RD (for all kNN) | RbD | LRD | LOF |
| ----- | ----- | ------------ | ---------------- | --- | --- | --- |
**For each point,** 
2.Identify k nearest neighbours (make list)
3.calculate Reach Distance (RD)= neighbour value - point value (so if k = 3 there would be 3 Reach Distances)
4.Reachbility Distance (RbD) = Sum up Reach Distances associated with that point
5.LRD(point) = $\frac{k}{RbD}$

**Once above completed for all points:** 
**For each point:** 
6.LOF(point) = $\frac{\sum \text{LRD of k neighbours of point}}{k~ \times \text{ LRD of point}}$

7.Identify which points are outliers (higher scores)