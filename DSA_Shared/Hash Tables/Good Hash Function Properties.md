
A good hash function should:

1. Return indexes that fit within the size of the array • i.e., [0 .. arrayLength-1] 
	- Modulus of hashindex (table length)
	- Use prime number as they distribute keys most evenly
	- Use a prime number that is far from powers of 2 (769, 1543, 3079, 6151, 12289, 24593, 49157, 98317 etc.)
	- If user specifies max size of hash table - round up to nearest prime


2. Be fast to compute • The hash function is a critical factor in access time 
	- (speed of hash function) + (speed of array access)  <--Array access is O(1), so the hash function is the limiting factor
	- constant time O(1) regardless of N

3. Be repeatable (i.e., always return same index) for a given key 
	- avoid time varying values in the calculation of a hash function
	- due to table size used as modulo - if resizing table, all existing entries must be re-hashed

4. Distribute keys evenly over the full range of the array 
		• This is to minimise collisions, a major issue in hash tables (tough property to achieve)