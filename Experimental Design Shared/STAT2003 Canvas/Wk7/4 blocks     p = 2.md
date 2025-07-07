- Conduct a $2^4 = 16$ factorial experiment
- Use **4 blocks** of **size 4**
- Confound effects: **ABC** and **ACD**
- We’ll use **mod-2 multiplication** to generate blocks

**Step 1: Choose Generators**
- Choose 2 effects to confound:
    $I = ABC, \quad I = ACD$
    
- Multiply the two to find the **third** confounded effect:
    $ABC \times ACD = A^2BC^2D = BD$
    
So the **complete defining relation** is:
    $I = ABC = ACD = BD$

**Step 2: Construct Principal Block
- Select 4 treatments where each has:
    - **No common letters**, or
    - **An even number of common letters** with ABC and ACD
    
- These will go into the **principal block** (Block 1)
Principal block
$$\text{Block 1} = \{ I, ac, bcd, abd \}$$

**Step 3: Generate Remaining Blocks by Multiplication**
Multiply each treatment in Block 1 by a new treatment not used yet to create other blocks:
Block 2 = Block 1 × a
$$a, c, abcd, bd$$

Block 3 = Block 1 × b
$$b, abc, cd, ab$$

Block 4 = Block 1 × d
$$d, acd, bc, ad$$

**Final Block Assignments:**

Block 1: I, ac, bcd, abd
Block 2: a, c, abcd, bd
Block 3: b, abc, cd, ab
Block 4: d, acd, bc, ad

- This confounds **ABC**, **ACD**, and **BD**
- You **cannot estimate** these effects
- All other main effects and two-way interactions are still **estimable**