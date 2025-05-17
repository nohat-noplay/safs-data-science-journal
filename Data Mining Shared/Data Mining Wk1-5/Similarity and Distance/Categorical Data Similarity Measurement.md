
**Overall Similarity Frequency**
$$Sim(\bar{X}, \bar{Y}) = \sum S(x_i, y_i)$$ Put records $\bar{X}$ and $\bar{Y}$ side by side and add 1 for every item[i] that matches item[i]. 
![[Pasted image 20240815134036.png]]
`Sim = 5`

**Inverse Occurrence Frequency**
- Weight down the similarity of attribute values that are frequent
- Weight up the similarity attributes that are infrequent
$$S(x_i, y_i) = \frac{1}{p_k(x_i)^2}\text{    if }  x_i = y_i$$
$x_i$ = 1 for every match (0 for no match so ignore)
$p_k(x_i)$: fraction of the $k$-th attribute having value $x_i$

eg. $$\bar{X} = (a, b, c, c, a, d, b, c),$$$$\bar{Y} = (a, b, a, c, d, d, a, c)$$
Probability:$$p(a) = 0.1, p(b) = 0.2, p(c) = 0.4, \text{  and  } p(d) = 0.3$$
With "inverse occurrence frequency":
$S(a, a) = \frac{1}{0.1^2}\text{    if }  a = a$
$= 100$
$S(b, b) = \frac{1}{0.2^2}\text{    if }  b = b$ 
$= 25$
$S(c, c) = \frac{1}{0.4^2}\text{    if }  c = c$ 
$= 6.25$
$S(d, d) = \frac{1}{0.3^2}\text{    if }  d = d$ 
$= 11.11$
$S(c, c) = \frac{1}{0.4^2}\text{    if }  c = c$ 
$= 6.25$
$Sim(\bar{X},\bar{Y})$   =   100+25+6.25+11.11+6.25     =   148.61