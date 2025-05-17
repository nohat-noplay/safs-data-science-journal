
#### 1: Find Frequent Itemsets 
1. **Make or find table with Transaction ID and Itemsets
eg. 

| Transaction ID | Items                  |
| -------------- | ---------------------- |
| 1              | Burgers, Buns, Ketchup |
| 2              | Burgers, Buns          |
| 3              | Burgers, Coke, Chips   |
| 4              | Chips, Coke            |
| 5              | Chips, Ketchup         |
| 6              | Burgers, Coke, Chips   |
2. **Determine the total number of transactions**: 
eg. N=6

3. **Calculate the minimum support count**:
    - Minimum support count = prescribed minSup × N   *round up*
eg. 0.33×6 =2 (rounded up)\

4. **Count each time each item appears across all transactions**

| Item    | Frequency |
| ------- | --------- |
| Burgers | 4         |
| Buns    | 2         |
| Ketchup | 2         |
| Coke    | 3         |
| Chips   | 4         |
5. **Write Frequent Pattern Set L = with each item in order of frequency (if tied, write in lexicographic order)**
Frequent Pattern Set L = {(Burgers: 4), (Chips: 4), (Coke: 3), (Buns: 2), (Ketchup: 2)}

6. **Build Ordered Item set**: 

| Transaction ID | Items                  | Ordered Items          |
| -------------- | ---------------------- | ---------------------- |
| 1              | Burgers, Buns, Ketchup | Burgers, Buns, Ketchup |
| 2              | Burgers, Buns          | Burgers, Buns          |
| 3              | Burgers, Coke, Chips   | Burgers, Chips, Coke   |
| 4              | Chips, Coke            | Chips, Coke            |
| 5              | Chips, Ketchup         | Chips, Ketchup         |
| 6              | Burgers, Coke, Chips   | Burgers, Chips, Coke   |

7. **Build Frequent Pattern Tree**
Null or $\emptyset$ is root node, then create tree 
- Check if itemset shares prefix with some previously inserted path, if so follow that path
- Else create a new path and initialize the count to 1


![[Pasted image 20240824114914.png]]
