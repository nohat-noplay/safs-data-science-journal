
If Separate Chaining: 
Just find the item to remove (same as accessing) and delete it from the linked list it resides in

If Open Addressing (eg. Double Hashing):

problem: 
Cant just probe to the item (same as accessing) and make the slot empty so that it is free for subsequent inserts - when accessing, we rely on finding empty slots to conclude that the key is not in the table and so abort probing BUT NOW we just removed an item that may have been in the middle of a chain of historical probes

solution: 
 mark a removed slot as “free-but-formerly-used” 
 • Tells access probes that the key it is looking for might be found further down due to the removal • Thus access probes can only stop once it encounters a “free-and-never-been used” slot
 
 Issue with solution: eventually all slots will be marked as "free but formerly used" and access time degenerates to O(N) - TIME TO REBUILD!