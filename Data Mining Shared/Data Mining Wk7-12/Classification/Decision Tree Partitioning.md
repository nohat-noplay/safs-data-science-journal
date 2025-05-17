• If a size threshold of 6 and a purity threshold of 0.9 are required, determine if further splits are needed. If so, suggest the splits (by drawing dashed lines) and complete the decision tree.
• Indicate the purity and size at the leaf nodes of the final tree.
![[Pasted image 20240910103041.png|]]


--------
Decision Tree on current partitioning scheme: 
$x1 \gt 3$:
	$x2 \le 4$: Circle (Purity = 13/17 (0.76))
	$x2 \gt 4$:
		$x1 \le 5.5$: Triangle (Purity = 7/7 (1))
		$x1 \gt 5.5$: Square (Purity = 12/17 (0.71))
$x1 \le 3$: Square (Purity = 22/24 (0.91))
(4 nodes)

Further partitioning to get 0.9 purity, min amount of nodes is 6 (size threshold)

$x1 \gt 3$:
	$x2 \le 4$: 
		$x1 \le 8$: Circle	(Purity = 11/12 (0.92))
		$x2 \lt 8$: Mixed leaf - Circle or Square purity of 2/5
	$x2 \gt 4$:
		$x1 \le 5.5$: Triangle (Purity = 7/7 (1))
		$x1 \gt 5.5$: 
			$x2 \gt 5.5$: Square (Purity = 11/12 (0.92))
			$x2 \le 5.5$: Mixed leaf - Circle or Triangle purity of 2/5
$x1 \le 3$: Square (Purity = 22/24 (0.91), Size = 24)
(6 nodes) (This is size threshold)