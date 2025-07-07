2 blocks for $2^3$ Factorial:

1. Select highest order interaction to confound ie. _I = ABC_ (this is called a generator)
2. Go to contrast table and assign: 
	- Treatments where **ABC = +1** go into **Block 1** 
	  OR **odd** number of letters go into Block 1
	- Treatments where **ABC = −1** go into **Block 2**
		OR **even** number of letters go into Block 2 (including I)
- note: you will not be able to interpret ABC as the interaction is now confounded however main effects and two-factor interactions are still clean

|Treatment|A|B|C|ABC|Block|
|---|---|---|---|---|---|
|(1)|−|−|−|−|2|
|a|+|−|−|+|1|
|b|−|+|−|+|1|
|ab|+|+|−|−|2|
|c|−|−|+|+|1|
|ac|+|−|+|−|2|
|bc|−|+|+|−|2|
|abc|+|+|+|+|1|

eg. _Blocks could be 2 different scientists measuring weight_ 