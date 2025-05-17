1.Determine if each observation is + or - from median
2.Determine difference of observation from median and make it absolute value
3.Rank those Absolute values from smallest to largest (remove any 0 differences), 
4.Put + or - signs on rank (found at step 1.)
5.Sum all positive ranks together and then sum all negative ranks together - this your Wscore
##### Using Wscore to find p value:
`psignrank(Wscore, n)`
(if lower.tail is FALSE: `1-psignrank(Wscore, n)`) (if two.sided: `2*psignrank(Wscore, n)`)

OR [[Wscore to Zscore - WSR (1 Sample)]]