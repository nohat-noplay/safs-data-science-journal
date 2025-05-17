**Monotonicity**
If an item subset does not meet minimum support, then the item superset will not meet minimum support - allows for optimised the search for frequent itemsets
$$\text{item subset minSup} \ge \text{item superset minSup}$$

**Downward Closure**
The superset will have less or equal support as a subset
$$\text{item superset minSup} \le \text{item subset minSup}$$