Code is redundant if performs a task that another piece of code is doing (bad)

Opposite of Redundancy is Reuse
<span style="color:#00b0f0">Re-use is good but increases coupling - so there must be a balance (consider carefully)</span>

Redundancy examples:
<span style="color:#ff0000">SuperSets</span>
<span style="color:#ff0000">Common Tasks</span> - make it it's own function instead of repeating

Example of Supersets:
► If modules A and B perform exactly the same task: 
 -  One should be deleted; e.g. B. 
► If module A is a superset of module B: 
- The duplication should be deleted from A. 
- Module A should instead use module B (rather than duplicate it).
► If modules A and B (and maybe even C, D, etc.) perform overlapping tasks: 
-  Identify the overlapping code. 
- Delete it from both A and B (and C, D, etc. if applicable). 
- Create a new module Z, containing the overlapping code. 
- Have the other modules use module Z.