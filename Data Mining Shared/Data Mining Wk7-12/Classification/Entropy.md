Compute the Entropy for the portion of the data set with age at least 50. 
![[Pasted image 20240910103132.png|100]]
1. Filter data for rows of Age > 50
2. Count Donor classes: 5 Y, 1 N
3. P(Y) = 5/6, P(N) = 1/6
4. Compute entropy: $H = -(P(Y)log_2(P(Y)) + P(N)log_2(P(N)))$
note: $log2​(x)=\frac{ln(x)}{ln(2)}​$
