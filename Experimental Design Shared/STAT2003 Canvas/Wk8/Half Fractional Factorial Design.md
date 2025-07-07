
- A full $2^k$ factorial design quickly becomes **infeasible** as $k$ increases.
- Fractional factorials reduce the number of runs by assuming **higher-order interactions are negligible**.
- They can also screen for key factors (eliminate insignificant factors)
- We lose 'resolution' - ability to distinguish between main (1 factor) and interaction effects (combination of factors). 

Basic Structure of $2^{k-p}$ Designs
- $k$: Number of factors
- $p$: Number of defining contrasts (generators)
- $2^{k-p}$: Number of treatment combinations (i.e. runs)

EXAMPLE:
$2^4$ factorial would be 16 runs (A, B, C, D). 
$\leftarrow$ While $2^{4-1}$ 'half fractional factorial' is 8 runs (A, B, C, D=AB). 
- this creates aliasing:
	- D is aliased with the interaction AB

**How Aliasing Arises**:
When using a fractional factorial:
- **Generators** are chosen (e.g., D = AB).
- A **defining relation** is built (e.g., I=ABD).
- **Aliasing structure** is determined by multiplying each factor with the defining relation.
    > This shows exactly **which effects are confounded** with each other.
    > If the confounded interaction (e.g., AB) is **negligible**, it is safe to interpret the main effect (e.g., D) as significant.
    > If not, **we cannot tell** whether the main effect or the interaction caused the observed effect.

  



