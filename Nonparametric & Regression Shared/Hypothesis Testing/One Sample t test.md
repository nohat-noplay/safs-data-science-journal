Find $\bar{x}$ (the sample mean)
Find s by $s = \sqrt{\frac{\sum{(x_i - \bar{x})^2}}{n-1}}$
Do t-test: $t = \frac{\bar{x} - \mu}{(\frac{s}{\sqrt{n}})}$, df = n - 1 
`t.test(data, alternative = "two.sided"\"greater", mu = __)`
