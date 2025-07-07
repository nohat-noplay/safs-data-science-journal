- A **space-filling design** used mostly for **computer experiments** or **simulations**.
- Ensures that each variable is **evenly sampled** across its range (a smarter random design)
- explore the space **uniformly** and avoid clustering of points.

| Criterion | Goal                                                     | Formula                                                                                              | Best                   |
| --------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------- |
| Maxmin    | Maximise the **minimum distance** between any two points | Compute all pairwise distances, find smallest one.                                                   | Biggest min distance   |
| Phi-p     | Penalise close pairs of points                           | Sum of inverse of distances raised to the power p $\phi_p = [\sum \sum \frac{1}{d^p}]^{\frac{1}{p}}$ | Smallest total penalty |
