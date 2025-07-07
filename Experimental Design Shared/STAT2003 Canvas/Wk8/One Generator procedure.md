1. Start with a $2^4$ design for factors $A, B, C, D.$
2. **Introduce E as a generator**:  
    Define E = ABCD.
3. **Build the Treatment Table**:
    - Calculate E as the product of A × B × C × D signs.
    - Even number of + signs → E = +.
    - Odd number of + signs → E = -.
4. This gives a $2^{5-1} = 16$ run design.
5. **Build the Defining Relation**:  
    $I = ABCDE$
6. **Work out the Aliasing Structure**:
    - Multiply each factor by the defining relation to find what it is aliased with. 
    - Can do this by TABLE or math
- **Example I=ABCDE.:**
    - A is aliased with BCDE
    - B is aliased with ACDE
    - C is aliased with ABDE
    - D is aliased with ABCE
    - E is aliased with ABCD