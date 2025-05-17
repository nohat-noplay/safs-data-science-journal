Use Reservoir Sampling for large continuous streams of data:
- inserts incoming item with the probability
$$\frac{\text{no. of items in subset}}{\text{no. of items in data}}$$
- eject old item in subset at random