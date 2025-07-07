The contrast for an effect is a sum of weighted responses where the weights correspond to the assigned factor levels. Contrasts example involves 2 treatments ($A$ and $B$) where you assign a +1 or -1 to them 4 times (as Factorial $2^2$ = 4) _eg. if factor had "low" and "high" you would assign -1 to "low" and +1 to "high_

1. Assign Factors to A or B.       _eg. A = Fertilizer Type, B = Watering_
2. Assign Levels in each Factor to + or -    _eg. A+ = Type X, B- = Type Y, +B = daily, -B = none _
3. Make Table

| Run | Factor A | Factor B | Treatment Combo | Interaction of A & B |
| --- | -------- | -------- | --------------- | -------------------- |
| 1   | -1       | -1       | I               | +                    |
| 2   | +1       | -1       | a               | -                    |
| 3   | -1       | +1       | b               | -                    |
| 4   | +1       | +1       | ab              | +                    |

4. Find Treatment means for I, a, b, ab
5. Find Sum of Squares for $SS_A, SS_B, SS_{AB}$ using below formulas where $n$ is number of observations per treatment combination ("replicates") and  here we are also assuming $2^2$ Factorial
$$SS_A = \frac{[ab - b + a - I]^2}{2^2(n)}$$
$$SS_B = \frac{[ab - a + b - I]^2}{2^2(n)}$$
$$SS_{AB} = \frac{[ab - a - b + I]^2}{2^2(n)}$$
6. Compute $SS_T = \sum (Y_{ijk} - \bar{Y}_{\cdot\cdot\cdot})^2$ where $Y_{ijk}$ is  observation response value minus the Grand Mean then square it - do this for every observation and add them together
OR
Compute $SS_E = \sum(Y_{ijk} - \bar{y_{ij}})^2$ where  $Y_{ijk}$ is  observation response value minus mean mean for the mean for (a or b or ab or I) then square it - do this for every observation and add them together

7. Find Sum of Squares for $SS_E$ 
$SS_{Total} = SS_A + SS_B + SS_{AB} + SS_{Error}$   OR   $SS_E​ = SS_{Total} − (SS_{A} ​+ SS_B​ + SS_{AB}​)$