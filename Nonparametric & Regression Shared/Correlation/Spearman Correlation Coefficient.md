1 numeric variable and 1 categorical (ordinal) variable. 
(or Pearson's assumptions can not be met)
1. Assign ranks to all $x_i$ (ranks are $u_i$) and assign ranks to all $y_i$ (ranks are $v_i$)
2. Calculate $d_i$ = $u_i - v_i$ then square all the $d_i$'s and sum together
3. if no rank ties, use this formula: $$ r_S = 1 - \frac{6\cdot \sum_{i=1}^n {d_i}^2}{n \left( n^2 - 1 \right)}  $$
	if ties, use this formula:
$$ r_S = \frac{ \sum_{i=1}^n \left( u_i - \bar{u} \right) \left( v_i - \bar{v} \right) }{ \sqrt{ \left( \sum_{i=1}^n \left( u_i - \bar{u} \right)^2 \right) \left( \sum_{i=1}^n \left( v_i - \bar{v} \right)^2 \right) } } $$
where:
- $u = \text{rank} \left( x \right)$;
- $v = \text{rank} \left( y \right)$;
- $u_i$ is the $i$th observation of $u$;
- $v_i$ is the $i$th observation of $v$;
- $\bar{u}$ is the mean of $u$; and
- $\bar{v}$ is the mean of $v$.
