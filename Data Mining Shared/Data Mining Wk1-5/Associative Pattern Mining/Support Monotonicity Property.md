$$sup(J) \ge sup(I) \ \forall J\subseteq I$$
Consider an itemset $I = \{A, B\}$  and its subsets $J_1 = \{A\}$ and $J_2 = \{B\}$. If $\{A, B\}$ appears in 5 transactions, then $\{A\}$ and $\{B\}$ must appear in <ins>at least</ins> those 5 transactions. 

This is useful because if an itemset $I$ does not meet the minimum support threshold (i.e., it is not frequent), then none of its supersets can be frequent either. Eg. If $\{A, B\}$ is found to be infrequent, then $\{A, B, C\}, \{A, B, D\}$, etc., do not need to be checked, as they cannot be frequent.