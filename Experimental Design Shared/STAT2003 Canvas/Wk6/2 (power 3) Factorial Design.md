
$Y_{ij} = \mu + a_i + b_j + (ab)_{ij} + (ac)_{ij} + (bc)_{ij} + (abc)_{ij} + \epsilon_{ij}$

- Study **3 factors**, each at **2 levels** (e.g. Low = -1, High = +1)
- Efficiently estimate:
    - **3 main effects**
    - **3 two-factor interactions**
    - **1 three-factor interaction**

- Number of treatment combinations: $2^3 = 8$
- Total observations: $8 \times n$ where $n$ = replicates per combination

```
model <- aov(Y ~ factor(A) * factor(B) * factor(C), data = mydata)
summary(model)
```

1. Assign Factors to A or B or C.       _eg. A = Fertilizer Type, B = Watering, C = sunlight_
2. Assign Levels in each Factor to + or -    _eg. A+ = Type X, B- = Type Y, +B = daily, -B = none _, C+ = high, C- = low
3. Make table of A, B, C combos and determine interaction signs for AB, AC, BC. ABC

| Run | A   | B   | C   | AB  | AC  | BC  | ABC | Treatment Combo | Mean Response |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------------- |
| 1   | −   | −   | −   | +   | +   | +   | −   | I               | $\bar{Y_1}$   |
| 2   | +   | −   | −   | −   | −   | +   | +   | a               | $\bar{Y_2}$   |
| 3   | −   | +   | −   | −   | +   | −   | +   | b               | $\bar{Y_3}$   |
| 4   | +   | +   | −   | +   | −   | −   | −   | ab              | $\bar{Y_4}$   |
| 5   | −   | −   | +   | +   | −   | −   | +   | c               | $\bar{Y_5}$   |
| 6   | +   | −   | +   | −   | +   | −   | −   | ac              | $\bar{Y_6}$   |
| 7   | −   | +   | +   | −   | −   | +   | −   | bc              | $\bar{Y_7}$   |
| 8   | +   | +   | +   | +   | +   | +   | +   | abc             | $\bar{Y_8}$   |
4. Compute Effects and Sum of Squares $$SS_{effect} = \frac{(contrast)^2}{8n}$$
where: 
- 8 is $2^3$ <- number of treatment combinations and $n$ is number of observations per treatment combination ("replicates") 
- contrast is linear combination of **treatment means** with +1/−1 signs from the sign table:
_eg. Contrast for A = $(−1)\bar{Y_1​}+(+1)\bar{Y_2}+(−1)\bar{Y_3}​+(+1)\bar{Y_4​}+(−1)\bar{Y_5​}+(+1)\bar{Y_6​}+(−1)\bar{Y_7​}+(+1)\bar{Y_8​}$​_
_which the coefficient term comes from following the A vertically down the table_

NOTE: Can only use table if design has same number of replicates and contains each treatment combination (use `aov` if not.)

**Degrees of Freedom:**
A, B, C, AB, AC, BC, ABC = 1 (7 total)
Error = $8(n - 1)$  
Total = $8n - 1$

