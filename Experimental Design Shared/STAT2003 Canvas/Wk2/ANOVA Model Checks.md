Use `plot(model)` in R

1. **Normality of Residuals**
	- **Shapiro-Wilk Test**→ $p \gt 0.01$ → OK
		 `shapiro.test(residuals(model))`
	- **Q-Q Plot** → Points along line
	- **Histogram of residuals** - to show normal PDF

2. **Homoscedasticity (Equal Variance)**
	- **Levene's Test** (`leveneTest`) → $p \gt 0.05$ → equal variances
		 `library(car) leveneTest(response ~ factor, data = mydata)`
	- **Bartlett’s Test** (more sensitive)
		`bartlett.test(response ~ factor, data = mydata)`
	- **Residuals vs Fitted Plot** → No funnel shape
	- Scale-Location Plot → No cone shape

3. **Independence**
	- **Durbin-Watson Test** → For time series
		`library(lmtest) dwtest(model)` 
	- **Residuals vs Order** → No patterns or trends
		`plot(residuals(model), type = "l")`

F-test is robust: small violations OK.