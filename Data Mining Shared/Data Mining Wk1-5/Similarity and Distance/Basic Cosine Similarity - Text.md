**Basic cosine similarity for text data:**
$$cos(\bar{X}, \bar{Y}) = \frac{\sum x_i y_i}{\sqrt{\sum x_i^2}\sqrt{\sum y_i^2}}$$
$\sum x_i y_i$   Dot Product -> $(x_1 \cdot y_1) + (x_2 \cdot y_2) + ... + (x_n \cdot y_n)$
$\sum x_i^2$   Magnitude of $\bar{X}$  -> $\sqrt{(x_1^2) + (x_2^2) + ... + (x_n^2)}$
$\sum y_i^2$   Magnitude of $\bar{Y}$  -> $\sqrt{(y_1^2) + (y_2^2) + ... + (y_n^2)}$

1. ‘‘The sly fox jumped over the lazy dog.’’
2. ‘‘The dog jumped at the intruder.’’
Lexicon: {the sly fox jumped over lazy dog at intruder}

Sentence 1 ($x$): \[2, 1, 1, 1, 1, 1, 1, 0, 0]
Sentence 2 ($y$): \[2, 0, 0, 1, 0, 0, 1, 1, 1]

$= \frac{(4) + (1) + (1)}{\sqrt{4 + 1 + 1 + 1 +1 + 1 + 1}\sqrt{4 + 1 + 1 + 1 + 1}}$
$= \frac{6}{\sqrt{10}\sqrt{8}}$
$= \frac{6}{\sqrt{80}}$
$= 0.67$


More advanced text similarity techniques:
To be used to reduce common words like "the"