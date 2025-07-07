IF ANOVA analysis rejects NULL Hypothesis: 
Pairwise comparisons are used to figure out **which specific group means differ**.

| **Method**       | **Key Points**                                          | **R Code**                                             | **Output Summary**                           |
| ---------------- | ------------------------------------------------------- | ------------------------------------------------------ | -------------------------------------------- |
| **Fisher’s LSD** | Powerful, simple. Requires significant ANOVA first.     | `pairwise.t.test(..., p.adjust.method = "none")`       | Pairwise p-values (no adjustment)            |
| **Tukey’s HSD**  | Conservative. Controls FWER.                            | `TukeyHSD(aov_model)`                                  | Mean diff, CI bounds, adjusted p-values      |
| **Bonferroni**   | Popular. Adjusts \( \alpha \) by number of comparisons. | `pairwise.t.test(..., p.adjust.method = "bonferroni")` | Pairwise p-values with Bonferroni adjustment |
Written Output: If the **confidence interval** (lwr to upr) **does not include 0**, and the **adjusted p-value < 0.05**, the difference is **statistically significant**.
**Plot: comprehensive view of differences among all groups

note: emmeans can be used to look at contrasts, pairwise comparisons and also plot the comparisons:
```
# library(emmeans)
model_emm <- emmeans(model_aov, pairwise ~ X, adj="bonf")
plot(model_emm, comparisons = TRUE)
```
`adj = ` can be `bonf`, `tukey`, `scheffe`, `dunnett`
```
library(emmeans)
model_emm <- emmeans(model_aov, pairwise ~ X) #tukey is default
> pwpp(model_emm)
```
