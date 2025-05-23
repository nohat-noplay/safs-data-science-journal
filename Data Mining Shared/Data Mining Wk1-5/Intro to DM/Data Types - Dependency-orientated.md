#### Dependency-orientated data

- explicit (obvious such as graphs) or implied (typically such as consecutive temperature readings) dependencies
- order important
- more challenging as dependencies need to incorporated into analytical process
- Subtypes: 

	**Time-Series Data**
	- Generated by measurements over time
	- Can be two types of attributes:
		- Contextual (eg. time stamps from sensors)
		- Behavioural (eg. temperature from sensors)
	- OR can be Multiple attributes
		- Multivariate time-series data

	**Discrete Sequences and Strings**
	- Categorical analog of time-series data (Categorical data with time stamp)
	- Event logs `Login Password Login Password Login Password`

	**Spatial Data**
	- May contain spatial and temporal (time) attributes 

	**Network and Graph Data**
	- Nodes in a network
	- Relationships between nodes represented by edges
	- $G = (N, A)$ where $N$: Set of Nodes, $A$: Set of Edges