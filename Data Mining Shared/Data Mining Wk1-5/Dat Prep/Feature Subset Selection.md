Which features are relevant?
##### Unsupervised Feature Selection
Using Filter methods or/and Wrapper methods (w clustering algorithm)
Typically a minimum set of features is sought
##### Supervised Feature Selection
Filter methods:
- Evaluate features without using classification
- One feature or a subset of features at a time
- Ranking features according to some criteria: e.g. Fisher score (separation of classes), mutual information
Wrapper methods:
- Evaluate features with classification
- Involve subset search
- Mainly based on classification performance
Embedded methods (regularization)
- Pruning methods: e.g. recursive feature elimination (RFE)
- Decision tree methods: e.g. C4.5
- Regularization methods: e.g. Lasso