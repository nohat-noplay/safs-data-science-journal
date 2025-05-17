
1. Determine Absolute Support of each item and itemset (occurences of each item) for k=1, k=2...k=n
2. If prescribed minSup is an Absolute number - check each item and itemset if pass or fail for k=1, k=2...k=n
3. Convert each minSup pass into [[Relative Support]] - ([[Example of MinSup Table]])
4. For passed itemsets, state each way the implication between items can happen (consequent always only 1 item)
	(eg. a, b, c = a, b $\to$ b  OR a, c $\to$ b OR b, c $\to$ a )
5. Calculate [[Curtin 3/Data Mining/Data Mining Wk1-5/DM MidSem Test/Confidence]] of each implication using Relative support:
6. Check if implication meets prescribed MinConf and MinSup
7. Write statement *"if $A$ is present in a transaction, there is an {conf}% chance that $B$ will also be present in that transaction."
