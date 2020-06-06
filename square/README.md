## Question:
In how many ways can you place a 2 member subset of the set {1, 2 , ..., 10} on the remaining 3 vertices of a square such that two adjacent vertices have exactly one common member and non-adjacent vertices have no common members.
For this question: one of vertices of square holds {1, 2}.

---
## Answer:

* generate other points on the square as a function of where the second vertex is placed
* generate a list of possible squares, using all possible (x,y) where the second vertex might be
* cull the list for squares that have points outside of 1-10 range
* check fulfillment of constraints for adjacent / opposite points
