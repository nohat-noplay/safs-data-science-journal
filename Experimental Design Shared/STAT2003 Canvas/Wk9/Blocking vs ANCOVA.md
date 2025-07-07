
| Blocking                                                                                             | ANCOVA                                                                                 |
| ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| You **physically group** similar experimental units together (blocks) before running the experiment. | You **statistically adjust** for a continuous variable **after** the experiment.       |
| The nuisance variable is **categorical** (e.g., different batches, different machines).              | The nuisance variable is **continuous** (e.g., humidity, initial weight, temperature). |
| Handled in the design phase (experimental layout).                                                   | Handled during the analysis phase (after data is collected).                           |
| Example: Blocking by "Machine 1" vs "Machine 2".                                                     | Example: Adjusting for measured ambient humidity.                                      |
| Uses ANOVA with blocks as an additional factor.                                                      | Uses ANCOVA (ANOVA + regression adjustment for covariates).                            |

