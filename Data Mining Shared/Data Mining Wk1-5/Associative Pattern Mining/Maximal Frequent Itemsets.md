If an itemset meets the minSup threshold but it a subset of another itemset that also meets the minSup threshold, then the subset it not counted, only the superset. The super set is the Maximal Frequent Itemset. 

Example: 
Consider a transaction dataset with the following items: $\{A\}, \{B\}, \{C\}, \{D\}$  and assume minSup is set at 50%.
1. Suppose the itemset $\{A, B\}$ has a support of 60%, meaning it is frequent.
2. if $\{A, B, C\}$ also had a support of 60%, it would be frequent, and $\{A, B\}$ would no longer be maximal because it has a frequent superset.