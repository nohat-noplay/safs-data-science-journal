- **Uses blocking** to control for known nuisance variability (factor) among experimental units
- Use when units differ in some known way (e.g., location, operator, time)
- Reduces error by separating out variation due to block
- Each treatment is applied **once within each block**


$Y_{ij}$: Observation from **treatment $i$ in block $j$**

| **Block** | Observations |              |               | **Block Total**   |
| --------- | ------------ | ------------ | ------------- | ----------------- |
| $B_1$     | $Y_{11}$     | $Y_{21}$     | $Y_{31}$      | $Y_{\cdot1}$      |
| $B_2$​    | $Y_{12}$​    | $Y_{22}$​    | $Y_{32}$      | $Y_{\cdot2}$      |
| $B_3$​    | $Y_{13}$​    | $Y_{23}$​    | $Y_{33}$      | $Y_{\cdot3}$      |
|           | $Y_{1\cdot}$ | $Y_{2\cdot}$ | $Y_{3\cdot}$​ | $Y_{\cdot\cdot}$​ |
We analyse RBD with [[2-way ANOVA Table]]  $$Y_{ij} = \mu + \tau_i + \beta_j + \epsilon_{ij}$$
_eg. 3 Fertilizers are Treatments (T1–T3), 3 Blocks represent different **sunlight zones**.  
Each treatment appears once in each block (row)._