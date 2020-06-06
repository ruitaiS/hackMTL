## Question:
In how many ways can you place a 2 member subset of the set {1, 2 , ..., 10} on the remaining 3 vertices of a square such that two adjacent vertices have exactly one common member and non-adjacent vertices have no common members.
For this question: one of vertices of square holds {1, 2}.

---
## Answer:

Since the first vertex is already given to us, we can write a function that will generate the remaining vertices of the square based on where we place our second vertex. I've included a sketch showing how this is done.

From there I took the brute force approach of generating all possible squares with x and y within {1, ... 10}, and then culling that list for squares with vertices outside of that range, or with opposite / adjacent vertices which did not fulfill the requirements listed above.

There's no doubt a smarter / more elegant way to go about doing this, but hey, a computer is basically a giant calculator and I may as well use it, right? :)
