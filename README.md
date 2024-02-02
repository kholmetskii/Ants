The main task of ants is to move between two points (to carry food back and forth).
I wrote a simple algorithm that optimizes their work. All ants are guided by each other's cries (the radius of the cry changes in the code).
Initially, all the ants move randomly, but over time they will begin to form paths. The ant has two counters (blue and yellow) that increase by one with each step.
Consider the algorithm when the ant is heading towards the blue point:
--If the ant finds itself on the blue point, it equates the blue counter to zero, shouts out information about its blue counter, and heads to the yellow point.
--If an ant finds itself on a yellow point, it equates the yellow counter to zero and shouts out information about its yellow counter.
--If an ant hears that another ant has a smaller blue counter, then it equates its blue counter and goes to this ant, shouting out updated information about its blue counter. For clarity, a line is drawn between the ants.
--If an ant hears that another ant has a smaller yellow counter, then it equates its yellow counter, shouting out updated information about its yellow counter. For clarity, a line is drawn between the ants.
--The ant takes a step.
When an ant is heading towards the yellow point, the symmetric algorithm is used.
