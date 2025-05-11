
Options: 

OpenAddressing: Upon a collision, jump forward (‘probe’) a set amount to a new index and try again -  If the new index is also used, repeat the probe until an empty index is found 
	1. Linear Probing – probe by step size of one every time ((causes primary clustering which slow down access time))
	2. Quadratic Probing – probe forward by (probeNum)2  -  i.e., probe first by 1, then 4, then 9, 16, 25, 36, 49, … ((causes secondary clusters where may follow exact same path as initial collider and cant guarantee it will visit all slots))
	3. Double Hashing – use a secondary (different) hash function on the key to generate the probe step length 
		 - define maximum step size and make that the modulo - use prime number so empty slot is guaranteed since no common divisor between table length and any step size!

Separate Chaining: Key-value pairs are added to a linked list anchored at the colliding hash index