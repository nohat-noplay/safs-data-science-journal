Parallel Lines = no interaction
Not parallel lines = interaction!

**Interaction:***
To determine if there is an Interaction between Factor 1 and Factor 2 - look at plot where Factor 1 is on x-axis and Response on y-axis...
IF Factor 2 shows it's levels as parallel lines: No Interaction
IF Factor 2 shows it's levels crossing over lines or not strictly parallel: Interaction!

```
# Interaction plot
interaction.plot(mydata$A, mydata$B, mydata$Y)

# Interaction plot with predicted means
library(phia)
plot(interactionMeans(anova_model))

# Interaction plot using effects 
plot(effect("A:C", anova_model), multiline=TRUE)
```
