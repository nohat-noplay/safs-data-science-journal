? 

## Approach 2: Item-based Approach

![[Pasted image 20241022100918.png|400]]

1. Compute the average rating of all other users (excluding the row of the user we need to predict):
![[Pasted image 20241022101034.png|400]]

2. Centralise ratings of row around the mean of that row ($x_i - \bar{x}$)
![[Pasted image 20241022101338.png|400]]

3. Compute the norms of the columns $\sqrt{\sum({y_i}^2)}$
![[Pasted image 20241022101514.png|400]]


4. Compute the adjusted cosine similarity between each column and the column with the missing value
$$\text{Cosine}(\bar{U}, \bar{V}) = \frac{u_1v_1 + ... + u_sv_s}{\sqrt{u_1^2 + ... + u_s^2}\cdot \sqrt{v_1^2 + ... + v_s^2}}$$
$\frac{R2C1 \times R2C5 + R3C1 \times R3C5 + ...}{\text{norm of C1} \times \text{norm of C5}}$ 

5. Copy user rating for highest cosine column to be missing item rating 
eg. if highest cosine with column 5 is column 1, Assessor 1's App 5 rating is 4