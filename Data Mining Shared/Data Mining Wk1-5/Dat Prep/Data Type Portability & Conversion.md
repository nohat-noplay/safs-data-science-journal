
**Numeric → Categorical**
Discretization: divides numeric value ranges into φ intervals
Example: [0-30] 7→ Low ([0-10]), Mid ([11-20]), and High ([21-30])
<span style="color:#00b050">Common choices for BINNING</span>
- Equi-width: linear <- eg. Data 1-100, 5 bins. Bin 1: 1-20, Bin 2: 21-40...etc
- Equi-depth: uniformly distributed (each bin has same amount of data) <- eg. Bin 1: 5 data points, Bin 2: 5 data points...etc
- Equi-log: logarithmic

**Categorical (Nominal)→ Numeric**
<span style="font-weight:; color:#00b050">Binarization: from one numeric attribute to multiple binary attributes</span>
Example: convert (L, M, H) to numeric
L → [0, 0, 1]
M → [0, 1, 0]
H → [1, 0, 0]

**Text → Numeric**
Vector representation: numeric, high-dimensional, and sparse
Latent semantic analysis (LSA)
- Reduces the dimensions
Singular value decomposition (SVD)
- Document-term matrix: collection of all documents with normalized word frequencies

**Time Series → Numeric**
Removes dependency between original time-series values
Common: discrete wavelet transformation
- Time series to multi-dimensional data
- Each dimension: wavelet coefficient
- Large coefficients: dimensionality reduction

**Discrete sequence → Numeric**
Step 1: convert each symbol to binary time series
Step 2: time series to numeric
Step 3: aggregate multi-dimensional sets of features

**Others**
Spatial to numeric
Graph to numeric
Any type to Graphs for similarity-based applications