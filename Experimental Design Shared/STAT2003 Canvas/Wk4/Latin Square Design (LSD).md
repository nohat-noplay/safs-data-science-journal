- Controls for **two known sources of variability** (blocking factors) — often **rows** and **columns**
- Each treatment appears **once per row** and **once per column**
- Ideal when it's difficult or expensive to replicate many times
- Use when the number of treatments = number of rows = number of columns (must form a square)

We analyse LSD with [[3-way ANOVA Table]]  
$Y_{ijk}$: Observation from **treatment $i$, row (block) $j$**, and column (block) $k$
$$
\begin{array}{c|ccc}
\textbf{Row / Column} & \textbf{Column 1} & \textbf{Column 2} & \textbf{Column 3} \\
\hline
\textbf{Row 1} & T_1 : Y_{111} & T_2 : Y_{122} & T_3 : Y_{133} \\
\textbf{Row 2} & T_2 : Y_{213} & T_3 : Y_{231} & T_1 : Y_{223} \\
\textbf{Row 3} & T_3 : Y_{312} & T_1 : Y_{321} & T_2 : Y_{333} \\
\end{array}
$$

_an example of this using tomato plants_
$$
\begin{array}{c|ccc}
\textbf{watering freq / sunlight} & \textbf{8hr sun} & \textbf{2hr sun} & \textbf{no sun} \\
\hline
\textbf{heavy watering} & Fertilizer_1 : Y_{111} & Fertilizer_2 : Y_{122} & Fertilizer_3 : Y_{133} \\
\textbf{medium watering } & Fertilizer_2 : Y_{213} & Fertilizer_3 : Y_{231} & Fertilizer_1 : Y_{223} \\
\textbf{low watering } & Fertilizer_3 : Y_{312} & Fertilizer_1 : Y_{321} & Fertilizer_2 : Y_{333} \\
\end{array}
$$

We analyse LSD with [[3-way ANOVA Table]]:
$$Y_{ijk} = \mu + \tau_i + \rho_j + \gamma_k + \epsilon_{ijk}$$

Assumptions:
-  no interactions between rows, columns, treatments
- no additive effects (one blocking does not effect the other blocking)
- normal ANOVA assumptions

