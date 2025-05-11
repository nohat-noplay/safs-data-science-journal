##### Adjacent
Two Vertices are adjacent if they are connected by an edge
[[Adjacency List]] [[Adjacency Matrix]]

##### Degree
The number of Edges a Vertex is connected to (int)
<span style="color:#00b050">d(A) = 3</span>
If the Graph is [[Direction|Directed]]:
		Outdegree is number of edges in which the Vertex is a Source for
		Indegree is number of edges in which the Vertex is a Sink for
		<span style="color:#00b050">ideg(F) = 3, odeg(F) = 0</span>
	
##### Path
A path from vertex v1 to v2 is a sequence of vertices that are connected by edges 
<span style="color:#00b050">D to E Path: (D, A, B, E)  </span>
<span style="color:#00b050">D to E Path Edges: (D,A), (A,B), (B,E)</span>

##### Circuit
A Path whose first and last vertices are the same

##### Cycle
A simple circuit if, except for the first (and last) vertex, no other vertex appears twice
<span style="color:#00b050">(</span><span style="color:#00b050">D,A,B,E,C,D)</span>

##### Cyclic
If some path contains the same Node twice

##### Acyclic
If some path does not contain the same Node twice 
<span style="color:#00b050">Linked Lists, Trees
</span>

##### Hamiltonian Cycle
A cycle that contains ALL of the Vertices in the Graph

##### Subgraph
A Graph that is part of a bigger Graph 
- where the Vertices are a subset of the bigger Graph Vertices
- where the Edges are a subset of the bigger Graph Edges

##### Connected Graph
If there is a Path from any Vertex to any other Vertex in the Graph
<span style="color:#ff0000">A Tree is an example of a Graph that does not contain a Cycle</span>
<span style="color:#ff0000">A Forest is a disjoint (not connected) union of Trees</span>

##### Spanning Tree
A Subgraph that is a Tree (no Cycles) that contains all the Vertices of the Graph
(Missing some Edges)
