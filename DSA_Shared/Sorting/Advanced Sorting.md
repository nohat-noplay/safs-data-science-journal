
Time Complexity:
O(N) is the absolute lower limit for sorting - only happens when list is already in sorting order
Average case would be worse than O(N)

Unadvanced sorting is O(N^2) - bubblesort, insertionsort, selectionsort
These are all inplace sorting algorithms - requires less storage
Only Bubble and insertion sorts are Stable. 
Selection Sort is unstable - which means identically valued sort keys will swap during the sorting process

Advanced Sorting is O(NlogN)

### Merge Sort:

Split in half multiple times until there are only groups of 2. This is done recursively
Sort the two
then merge the halves back together and sort as you go. This is done recursively
This is not-in-place sort - a temp array is used
This is a stable sort.

![[Curtin 2/DSA/Sorting/Merge-sort-example-300px.gif]]



### Quick Sort

1. Seperate data into two subarrays with a partition (pivot element)
2. Organise data so left subarray is less than pivot, right side is more than pivot

 ![[Curtin 2/DSA/Sorting/Quicksort-example.gif]]

How to select a good pivot:
- choose one that divides the array into equal halves - ensuring a minimum number of splits

Efficiency:
If pivot chosen well, Log2N in the splits
O(NlogN) as each level does average O(N) compares

if pivot chosen badly:
O(N^2) - pivot is either smallest or largest number

Pivot selection strategies:
- Choose the middle, if the data is random, average chance of being an average pivot, if the data is semi-ordered - then choosing an outside one is definitely going to be bad
- Choose a random pivot, average pivot will be common and worst case is unlikely (similar to choosing middle)
- Choose the median out of three elements. Either pick left most, right most and middle and then take the median out of those. OR choose three randoms and choose the median out of those. - this is the best representation of the data and guarantees a split of atleast one element!


