Consider the example below. Classify a data point (F,T,4) using Naive Bayes.
![[Pasted image 20240910103151.png|100]]
1. Split rows into target classes and calculate probability
P(Y) = 4/9
P(N) = 5/9
2. Consider class Y - calculate probability of each categorical and numerical column that results in Y:
	Categorical:
	P(a1 = F) = 1/4
	P(a2 = T) = 1/2

	Numerical:
	Find mean and standard deviation of all Y: 5.25, 1.71 ($\sqrt{\frac{\sum(\bar{x} - x)^2}{n-1}}$)
	f(a3 = 4.0|Y) = $\frac{1}{sd} \cdot e^{(-\frac{(x - \bar{x})^2}{2 \cdot sd^2})}$
				= $\frac{1}{1.71} \cdot e^{(-\frac{(4 - {5.25})^2}{2 \cdot 1.71^2})}$ = 0.448
				
	P(Y|x) = P(a1 = F) $\cdot$ P(a2 = T) $\cdot$ f(a3 = 4|Y) $\cdot$ P(Y) = $0.25 \cdot 0.5 \cdot 0.448 \cdot 0.444 = 0.025$

3. Consider class N - calculate probability of each categorical and numerical column that results in N:
	P(a1 = F) = 4/5
	P(a2 = T) = 3/5
	P(a3 = 4.0) = Find mean and standard deviation of all N: 5, 2.45 ($\sqrt{\frac{\sum(\bar{x} - x)^2}{n}}$)
		f(a3 = 4.0|N) = $\frac{1}{sd} \cdot e^{(-\frac{(x - \bar{x})^2}{2 \cdot sd^2})}$
					= $\frac{1}{2.45} \cdot e^{(-\frac{(4 - {5})^2}{2 \cdot 2.45^2})}$ = 0.333
	
	P(N|x) = P(a1 = F) $\cdot$ P(a2 = T) $\cdot$ f(a3 = 4|N) $\cdot$ P(N) = $0.8 \cdot 0.6 \cdot 0.333 \cdot 0.55 = 0.088$

4. Which class has the higher probability? $0.088 \gt 0.025 = N \gt Y$
The data point (F, T, 4.0) is in class N!