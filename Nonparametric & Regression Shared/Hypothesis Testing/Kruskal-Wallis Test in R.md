datatogether <- c($group_1, group_2, ... group_K$)
group <- factor(rep(1:K, c($n_1, n_2, ... n_K$)))
kruskal.test(datatogether, group)

$K$ is number of groups
$n$ is number of items in a group