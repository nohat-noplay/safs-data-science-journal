Determine if **Fertilizer Type (A)** and **Watering Frequency (B)** affect tomato yield, and whether they **interact**.

|Factor|Levels|Coding|
|---|---|---|
|A|Fertilizer: Low / High|−1 / +1|
|B|Watering: Daily / Alt. Day|−1 / +1|

| A (Fert.) | B (Water) | Rep 1 | Rep 2 | Treatment | Mean Response          |
| --------- | --------- | ----- | ----- | --------- | ---------------------- |
| −1        | −1        | 360   | 370   | I         | $\bar{y}_{(1)} = 365$  |
| +1        | −1        | 400   | 410   | a         | $\bar{y}_{a} = 405$    |
| −1        | +1        | 330   | 320   | b         | $\bar{y}_{b} = 325$    |
| +1        | +1        | 390   | 395   | ab        | $\bar{y}_{ab} = 392.5$ |

 **Step-by-Step: ANOVA by Hand Using Contrasts:

 Step 1: Compute Grand Mean
$\bar{y}_{\cdot\cdot} = \frac{360 + 370 + 400 + 410 + 330 + 320 + 390 + 395}{8} = \frac{2975}{8} = 371.875$

Step 2: Use Contrast Formulas for SS
$SS_A = \frac{(ab - b + a - I)^2}{4n} = \frac{(392.5 - 325 + 405 - 365)^2}{8} = \frac{(107.5)^2}{8} = \frac{11556.25}{8} = 1444.53$
$SS_B = \frac{(ab - a + b - I)^2}{4n} = \frac{(392.5 - 405 + 325 - 365)^2}{8} = \frac{(-52.5)^2}{8} = \frac{2756.25}{8} = 344.53$
$SS_{AB} = \frac{(ab - a - b + I)^2}{4n} = \frac{(392.5 - 405 - 325 + 365)^2}{8} = \frac{(27.5)^2}{8} = \frac{756.25}{8} = 94.53$

Step 3: Total Sum of Squares
$SS_T = \sum (Y_{ijk} - \bar{y}_{\cdot\cdot})^2 = (360 - 371.875)^2 + (370 - 371.875)^2 + \dots + (395 - 371.875)^2 = 866.88$

Step 4: Error Sum of Squares
$SS_E = SS_T - (SS_A + SS_B + SS_{AB}) = 866.88 - (1444.53 + 344.53 + 94.53) = -1016.71$
 — negative value! This tells us **SS_T was underestimated**. So instead, compute error directly:

Step 4 (alternative): Compute SS_E directly
Each treatment has 2 replicates, so:

$SS_E = \sum (Y_{ijk} - \bar{y}_{ij\cdot})^2$

- For I: $(360 - 365)^2 + (370 - 365)^2 = 25 + 25 = 50$
- For a: $(400 - 405)^2 + (410 - 405)^2 = 25 + 25 = 50$
- For b: $(330 - 325)^2 + (320 - 325)^2 = 25 + 25 = 50$
- For ab: $(390 - 392.5)^2 + (395 - 392.5)^2 = 6.25 + 6.25 = 12.5$
$SS_E = 50 + 50 + 50 + 12.5 = 162.5$

Step 5: Compute Correct Total SS
$SS_T = SS_A + SS_B + SS_{AB} + SS_E = 1444.53 + 344.53 + 94.53 + 162.5 = 2046.09$

Step 6: Final ANOVA Table

| Source      | SS      | df  | MS      | F                                      |
| ----------- | ------- | --- | ------- | -------------------------------------- |
| Factor A    | 1444.53 | 1   | 1444.53 | $F_A = \frac{1444.53}{40.625} = 35.55$ |
| Factor B    | 344.53  | 1   | 344.53  | $F_B = \frac{344.53}{40.625} = 8.48$   |
| Interaction | 94.53   | 1   | 94.53   | $F_{AB} = \frac{94.53}{40.625} = 2.33$ |
| Error       | 162.5   | 4   | 40.625  |                                        |
| Total       | 2046.09 | 7   |         |                                        |

Step 7: Conclusion (with F-table comparison):
Compare your F-values to critical values from the F-table with:
- df1 = 1 (numerator)
- df2 = 4 (denominator)
- α = 0.05

From F-table:
- $F_{0.05, 1, 4} = 7.71$
So:
- $F_A = 35.55 > 7.71$ → A **significant**
- $F_B = 8.48 > 7.71$ → B **significant**
- $F_{AB} = 2.33 < 7.71$ → **no significant interaction**