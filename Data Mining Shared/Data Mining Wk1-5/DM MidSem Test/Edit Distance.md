The minimum-weight series of edit operations that transforms $a$ into $b$.
$$ Edit(i, j) = min \left\{ \begin{eqnarray} \text{Edit}(i - 1, j ) + \text{Deletion  Cost} \\   \text{Edit(i, j - 1) + Insertion Cost} \\ \text{Edit(i - 1, j - 1)} + \mathbb{I}(x_i \neq y_j) \text{ Replacement Cost} \end{eqnarray} \right. $$
