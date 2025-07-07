No overlap in information between contrasts — they’re statistically independent 

Make **multiple independent comparisons** between treatments means in a structured and statistically efficient way

Doing multiple t-tests can inflate Type 1 error () but this does not. 
**Type 1 Error**: You conclude at least one mean is different (**reject $H_0$​**), but in reality, all means are actually equal. (false positive)

Compare 2 C's to see if they are independent:
Contrast 1: [1, -0.5, -0.5] (comparing A against B and C)
Contrast 2: [0, 1, -1] (comparing B and C)
$$\sum \frac{c_i d_i}{n} = \frac{(1 \cdot 0) + (-0.5 \cdot 1) + (-0.5 \cdot -1)}{n} = 0$$
0 means it's orthogonal (independent)




