The confidence of the rule $X \Rightarrow Y$ quantifies the likelihood that $Y$ is present in a transaction given that $X$ is present in that same transaction.

Let $X$ and $Y$ be two sets of items. 
$$\text{conf}(X \Rightarrow Y) = \frac{\text{sup}(X \cup Y)}{\text{sup}(X)}$$

- $sup(X \cup Y)$ : This is the proportion of transactions in the database that contain both $X$ and $Y$ together. 
-  $sup(X)$: This is the proportion of transactions that contain the itemset $X$. 

Example:
Suppose you have a database of transactions, and you are analyzing the rule $\{A\} \Rightarrow \{B\}$:

- Support of $\{A, B\}$: Suppose this is 0.4, meaning 40% of transactions contain both $A$ and $B$.
- Support of $\{A\}$: Suppose this is 0.5, meaning 50% of transactions contain $A$.
**Confidence**: The confidence of the rule  $A \Rightarrow B$ is calculated as:
$$\text{conf}(\{A\} \Rightarrow \{B\}) = \frac{\text{sup}(\{A, B\})}{\text{sup}(\{A\})} = \frac{0.4}{0.5} = 0.8$$

This means that if $A$ is present in a transaction, there is an 80% chance that $B$ will also be present in that transaction.
