1. Start with a $2^4$ design for factors $A, B, C, D.$
2. **Introduce E and F as generators**:  
    Define E = ABC (I = ABCE)
	Define F = BCD (I = BCDF)
3. Multiple generator identities (I) together to find all defining relations:
$I = ABCE \times BCDF = ADEF$
4.  **Build the Treatment Table**:
    - Calculate E as the product of A × B × C signs.
    - Calculate F as the product of B × C × D signs.
    - Assign E and F levels (+ or -) accordingly for each run.
5. This gives a $2^{6-2} = 16$-run design.
6. **Build the Full Defining Relation**:
    $I = ABCE = BCDF = ADEF$
- **Work Out the Aliasing Structure**:
    - For each factor (A, B, C, D, E, F), multiply it by each part of the defining relation to find all aliasing (what it is confounded with).
	- EXAMPLE: 
	- Now we can determine which factor is aliased with what by multiplying each factor with the defining relation (remove any squared terms). So:
			$A$ can be aliased with: 
			- $A \times ABCE = BCE$
			- $A \times BCDF = ABCDF$
			- $A \times ADEF = DEF$
			- $\therefore$ A = BCE = ABCDF = DEF