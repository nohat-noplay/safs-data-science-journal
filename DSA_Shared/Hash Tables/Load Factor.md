Load Factor is a measure of how full a hash table is:

LF = numItems / table capacity
	- this can determine frequency of collisions in open addressing (probing) approaches

### Open Addressing 
0.0 = 0% chance of collision (nothing to collide with)
1.0 = 100% chance of collision (all slots are full!)

Make sure hash isnt too full (below 0.6-0.7)
Make sure table isn't too big (wasted space)

Types: 

 <ins>Linear probing (vs other open addressing approaches): </ins>
 Simplest open addressing approach
 Will always find a free slot 
 Suffers from primary clustering • This can make insertion/accessing quite slow if it gets bad

<ins>Quadratic probing </ins>
 Largely eliminates primary clustering
 Suffers from secondary clustering 
 May fail to find free slots (eg: if there are only a few left) • … and so also can’t tell when to give up looking for a key!

<ins>Double Hashing: </ins>
 No problems with primary or secondary clustering 
 Will always find a free slot • … as long as the table size is prime 
 Needs a secondary hash function (extra complexity)

### Separate chaining
 ##### isn't is as badly affected (because linked lists can help with collisions and therefore not cause full). 
Access and Deletion time IS affected bevause more linked lists 
- Average Access time increases as LF increases O(LF)

<span style="color:#00b050">Separate chaining pros (vs open addressing methods)</span> 
 O(1) insertion regardless of how full the table is 
 No limit on number of items that can be stored • i.e., load factor can exceed 1.0 
 Performance is better with higher load factors 
 No need to specially mark slots with removed items • The linked list will automatically ‘close up’ the gap 

<span style="color:#ff0000">Separate chaining cons </span>
 More complicated data structure needed (array of linked lists) 
 Node pointer memory overhead for each element 
 Access time tends to be slower when load factor is low