
- Use when **residuals are non-normal or variances are unequal**
- Transform using:
    $y' = \ln(y)$
- After transformation, ANOVA compares **means of log responses**
- Back-transformed means represent **geometric means**, not arithmetic means

Hypotheses on transformed scale:
- $H₀: \mu_{\ln(1)} = \mu_{\ln(2)} = \cdots = \mu_{\ln(6)}$ The **geometric means** of the percent error for all algorithms are equal.
- $H_A: \mu_{\ln(i)} \ne \mu_{\ln(j)} \text{ for some } i \ne j$ At least one algorithm has a different geometric mean percent error.
    
Interpreted on original scale:
 "There is no difference in **geometric mean percent error** between algorithms."