ANCOVA is another strategy (other than Blocking) to remove unwanted variation that can hide treatment effects. You can't block continuous variables (eg. Temperature, humidity) so you measure that as a variable (a 'covariate') and then adjust for it during analysis (using ANCOVA)

ANCOVA = ANOVA + Regression adjustment for covariates
where;
- ANOVA compares treatment means
- Regression adjustment: models the linear effect of the covariate

$$Y_{ij} = \mu + \tau_i + \beta(X_{ij} - \bar{X}) + \epsilon_{ij}$$
Where:
- $Y_{ij}$ = Response for treatment i, unit j
- $\mu$ = Overall mean
- $\tau_i​$ = Treatment effect
- $\beta$ = Regression coefficient for the covariate
- $X_{ij}$ = Covariate value for unit j in treatment i
- $\bar{X}$ = Mean of covariate over all observations
- $\epsilon_{ij}$​ = Random error

ANCOVA assumptions:
$Y$ and $x$ is linearly related - scatter plot with lm line
$\beta$ needs to be constant (homogenuity of slopes) - lm lines are parallel

**ANCOVA Analysis Steps:**

1. Check ANCOVA assumption of "Homogeneity of slopes" with plotting
	Check lines are parallel, which means interaction is not significant (if it is, then assumption is violated and ANCOVA can not be performed).

2. **Fit linear Model including interaction:**  
    Fitted the linear model WITH interaction terms and test interaction using `drop1()`.
		- Is interaction term significant? (p < 0.05)
		- If not: "**homogeneity of slopes assumption holds**"

3. **Fit Simpler linear model without interaction:**     
	- If covariate variable significant - adjustment needed

4. Perform ANOVA  
	- If treatment effect (variable) p-value < 0.05: conclude significant evidence AFTER adjusting for covariate variable
	- If treatment effect (variable) p-value > 0.05: conclude no significant evidence AFTER adjusting for covariate variable 
5. **Write Linear Models for each treatment**:
	- R returns the coefficients for 1 model so we need to multiply the 
	

6. Check ANOVA assumptions
7. State conclusion
	"After adjusting for the effect of (covariate), we have significant evidence to conclude the..., F(df_x, df_error)= ##, P < 0.05"


NOTE: A model with interaction effect between a treatment and a covariate allows for different slopes 