## Question:

How many subsets of { 1, 2 , ...10 } can have a total sum
that is divisible by 8 ?
---
## Answer:
There's the obvious brute force solution of just generating all the subsets and seeing if it is divisible by 8, but since I already did something inelegant for the squares problem, I thought it would be good to do this one in a more thoughtful way.

Each subset must be itself comprised of sets that add up to eight, otherwise the total sum won't be divisible by it). If we find the number of subsets of 1-10 that add up to 8, then our search is much simplified. Note however that we still need to ensure that none of our combined subsets will require the same member more than once.

For a set of size 1, only [8] has a sum of 8

Size 2:
    [1, 7], [2, 6], etc etc

Size 3:
    [1, 2, 5] [1, 3, 4] etc

And so forth.

Special cases:
    [10,6], [9,7]    
