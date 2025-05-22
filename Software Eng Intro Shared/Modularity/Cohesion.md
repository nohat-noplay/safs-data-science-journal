- single module - how well does one module do it's task. 
- high cohesion - function is doing its task very well
- low cohesion - not doing very well and doing lots of thing

<span style="color:#00b0f0">one function does one thing - good</span>
Forms of cohesion: 
1. <span style="color:#00b0f0">control flags: perform 1 distinct task</span>
2.<span style="color:#ff0000"> sequential task: doing several things in sequence is bad! (doing more than 1 thing)</span>
3.<span style="color:#ff0000"> different data: if data isn't related than it probably means function is doing more than 1 thing</span>

Even among methods that perform multiple tasks (bad), there is a degree of cohesion also:
► Completely unrelated – extremely low (essentially zero) cohesion. 
► Superficially related by name or some ad hoc category. 
► Related by time – the tasks must be performed at about the same time, perhaps in a particular order. 
► Related by data – the tasks all use the same data, perhaps data produced by each other.
