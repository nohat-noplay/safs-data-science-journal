##### Sampling from Static Data
- Without replacement: no duplicates possible
- With replacement: duplicates possible
- Biased sampling: emphasizes some part of data
- Stratified sampling: minority class is present, e.g. SMOTE
##### Sampling from Dynamic Data
Data streams of continuous incoming data means can only cache a small subset of data.
*Reservoir sampling:* 
	$k$ = number of items in subset, $n$ = number of items in data
	1. Insert the $nth$ incoming stream data point into the reservoir with probability $\frac{k}{n}$.
	2. If the newly incoming data point was inserted, then eject one of the old $k$ data points
	at random to make room for the newly arriving point.