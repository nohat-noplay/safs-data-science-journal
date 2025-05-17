(tries every combination - so less computational efficient)
Search through all possible patterns (candidate itemsets), this equals to: $2^{|U|} - 1$ distinct subsets

Step 1: generate all candidate itemsets
Step 2: scan the database and count the number of occurrences
Step 3: select itemsets with support ≥ minimum support

Impractical if d = |U| is large