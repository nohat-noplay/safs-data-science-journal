(prunes candidate itemsets so only tries combinations that could be successful - computationally efficient)

Exploiting the downward closure property
- *if an itemset $I$ does not meet the minimum support threshold (i.e., it is not frequent), then none of its supersets can be frequent either*
 - ignore supersets of a failed candidate itemset

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
eg. 0.33×6 =2 (rounded up)

4.  **Generate Candidate Itemsets**:
    - Start with single-item itemsets and then generate higher-order itemsets based on the frequent itemsets found.
    - Build k-itemset (3-itemset) using each of the unique items that passed the (k-1)-itemset (2-itemset) stage minus the (k-1)-itemsets  (2-itemset) that did not pass (k-1)-itemset (2-itemset) stage. 
    
eg. 
**Single-Item Itemsets:
- **Count occurrences of each item :****

| Item Set | Count | Support ≥ 2? |
| -------- | ----- | ------------ |
| Burger   | 4     | YES          |
| Buns     | 2     | YES          |
| Ketchup  | 2     | YES          |
| Coke     | 3     | YES          |
| Chips    | 4     | YES          |

**2-Itemsets**

| Item Set             | Count | Support ≥ 2? |
| -------------------- | ----- | ------------ |
| Burger, Buns         | 2     | Yes          |
| ~~Burgers, Ketchup~~ | ~~1~~ | ~~No~~       |
| Burgers, Coke        | 2     | Yes          |
| Burgers, Chips       | 2     | Yes          |
| ~~Buns, Ketchup~~    | ~~1~~ | ~~No~~       |
| ~~Buns, Coke~~       | ~~0~~ | ~~No~~       |
| ~~Buns, Chips~~      | ~~0~~ | ~~No~~       |
| ~~Ketchup, Coke~~    | ~~0~~ | ~~No~~       |
| ~~Ketchup, Chips~~   | ~~1~~ | ~~No~~       |
| Coke, Chips          | 3     | Yes          |

**3-Itemsets** 
**Build this item set using each of the unique items that passed the 2-itemset stage minus the 2-itemsets that did not pass 2-itemset stage.** 
Unique items: {Burgers}, {Buns}, {Coke}, {Chips}.
2-items that did not pass Stage2: {Buns, Coke}, {Buns, Chips}
This leads to only one 3-itemset

| Item Set             | Count | Support ≥ 2? |
| -------------------- | ----- | ------------ |
| Burgers, Coke, Chips | 2     | YES          |

#### 2: Calculate MinSup and MinConf

1. Create Table with items that passed for each k and calculate minsup: 
$\text{Support }(X)=\frac{\text{Number of transactions containing } X}{\text{Total number of transactions}}$

| Pass (k) | Support | Frequent k-itemsets   | minsup     |
| -------- | ------- | --------------------- | ---------- |
| k = 1    | 4       | Burgers               |            |
|          | 2       | Buns                  |            |
|          | 2       | Ketchup               |            |
|          | 3       | Coke                  |            |
|          | 4       | Chips                 |            |
| k = 2    | 2       | {Burger, Buns}        | 2/6 = 0.33 |
|          | 2       | {Burger, Coke}        | 2/6 = 0.33 |
|          | 2       | {Burger, Chips}       | 2/6 = 0.33 |
|          | 3       | {Coke, Chips}         | 3/6 = 0.5  |
| k = 3    | 2       | {Burger, Coke, Chips} | 2/6 = 0.33 |

2. Write about Associations and state minsup and calculate minconf for all K = 2 + that passed minsup. 

Prescribed Confidence Threshold is 60%
$$\text{conf}(\{A\} \Rightarrow \{B\}) = \frac{\text{sup}(\{A, B\})}{\text{sup}(\{A\})} = \frac{0.4}{0.5} = 0.8$$
X $\rightarrow$ Y (minsup, minconf) = Does it Pass or Fail MinSup and MinConf??

Burgers $\rightarrow$ Buns (0.33, $\frac{\text{sup(Burgers, Buns)}}{\text{(sup(Burgers)}} = \frac{2}{4}$  = 0.5 ) - FAIL 
Buns $\rightarrow$ Burgers (0.33, $\frac{\text{sup(Burgers, Buns)}}{\text{(sup(Buns)}} = \frac{2}{2}$  = 1 ) - PASS
Burgers $\rightarrow$ Coke (0.33, $\frac{\text{sup(Burgers, Coke)}}{\text{(sup(Burgers)}} = \frac{2}{4}$  = 0.5 ) - FAIL 
Coke $\rightarrow$ Burgers (0.33, $\frac{\text{sup(Coke, Burgers)}}{\text{(sup(Coke)}} = \frac{2}{3}$  = 0.66 ) - PASS
Burgers $\rightarrow$ Chips (0.33, $\frac{\text{sup(Burgers, Chips)}}{\text{(sup(Burgers)}} = \frac{2}{4}$  = 0.5 ) - FAIL 
Chips $\rightarrow$ Burgers (0.33, $\frac{\text{sup(Burgers, Chips)}}{\text{(sup(Chips)}} = \frac{2}{4}$  = 0.5 ) - FAIL 
...
Burgers, Coke $\to$ Chips (0.33, $\frac{\text{sup(Burgers,Coke Chips)}}{\text{(sup(Burgers, Coke)}} = \frac{2}{2}$ = 1 ) - PASS
Burgers, Chips $\to$ Coke (0.33, $\frac{\text{sup(Burgers,Chips, Coke)}}{\text{(sup(Burgers,  Chips)}} = \frac{2}{2}$ = 1 ) - PASS
Chips, Coke $\to$ Burgers (0.33, $\frac{\text{sup(Coke, Chips, Burgers)}}{\text{(sup(Chips, Coke)}} = \frac{2}{3}$ = 0.66) - PASS