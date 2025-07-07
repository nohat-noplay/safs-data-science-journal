When running a fractional factorial design, you save time and money by running a smaller experiment but some effects get mixed together. Its important to know which effects get mixed (confounded) when interpreting the results. You can work out which effects are mixed by building an Alias structure. 

| Step                            | Meaning                                                                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. Choose Generators            | Defines which effects get mixed.                                                                                                                                     |
| 2. Build Defining Relation      | Find I = (generators and their products).                                                                                                                            |
| 3. Find Aliases for Each Factor | By multiplying the factor with each term in the defining relation.                                                                                                   |
| 4. Read Results Carefully       | Understand that main effect A is mixed with BCE and DEF.                                                                                                             |
| 5. Declare assumption           | Its generally safe to say that higher orders interactions are negligible so it safe to conclude the lower order is significant if its confounded with higher orders. |

**EXAMPLE with $2^{3-1}$**
Higher order interactions tend to be small so to choose a fractional factorial. 
- To construct the fraction, we select the block where ABC = +1.
- Once this is done - some columns will have same sign sequence (and therefore confounded). This is means they can be aliased. 

![[Pasted image 20250428112003.png]]

1. Separate highest order into blocks (ABC). 
2. Choose only rows where highest order is +1
3. Identify which columns have the same +1,-1, this is called aliasing (in this example A & BC are aliased, B & AC are aliased and C & AB are aliased)


**Larger scale - EXAMPLE: $2^{6-2}$ = 16 runs**
- **See [[Two Generator Procedure]]





