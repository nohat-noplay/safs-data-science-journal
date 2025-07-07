When you have **limited runs**, and full factorial or CCD is too large, **optimality criteria** help you select the **best subset** of points to fit your model well.  
This is **more flexible** than fractional factorial designs because it can choose **any subset** from the candidate design space.  
Implemented in R using `optFederov()` from the **`AlgDesign`** package.

| Criterion | Goal                                            | What                                                     | Best for                                       | Good             |
| --------- | ----------------------------------------------- | -------------------------------------------------------- | ---------------------------------------------- | ---------------- |
| D-Optimal | Minimises joint variance of parameter estimates | Maximises $det(X^T X)$                                   | Most efficient use of points                   | Bigger = better  |
| A-Optimal | Minimises average variance of coefficients      | Minimises $trace((X^T X)^{-1})$                          | Best average precision across all coefficients | Smaller = better |
| G-Optimal | Minimises worst-case prediction error           | Minimises $max(x^T(X^TX)^{-1}x)$ where $x$ is each point | Ensures all predictions are accurate           | Smaller = better |
