1.Take the differences between the observations within the matched pairs $X_d = X_1 - X_2$ (if =0, drop obs and n=n-1
2.Rank the abs($X_d$)
3.Put signs from $X_d$ on Ranks
4.$W^+$ is sum of all positives, $W^-$ is sum of all negatives
      Use p-value from `Exact = TRUE` if:
-$n$ is less than 50, AND
-there are no ties
