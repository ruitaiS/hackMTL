## Question:
A set S is friendly if for every x in S, either x + 1 or x - 1 (at least one of them) is also in S.

For example, the set { 1, 2, 499, 500 } is friendly. How many friendly sets can be created with 5 members, where members can range from 1 to 100 ?

---
## Answer:
For a friendly set with five members, three general cases exist:

1) All five members are clustered together

2) There is a cluster of 2, followed by a cluster of 3

3) There is a cluster of 3, followed by a cluster of 2

#### Case 1:

If we start with the set [1,2,3,4,5] and iteratively increase the leading value by one until the last value is 100 (eg. until we have the reached set [96,97,98,99,100] ) we will have iterated through all possible instances of the first case. Since the first value iterates from 1 to 96, it's quite clear that there are 96 possible instances of the first case.

#### Case 2 / 3:

First we note that these two cases are symmetric to one another, so it will suffice to only consider a single case. However the python code does contain functions that will generate both cases separately.

Let's look at the cluster of 2, followed by a cluster of 3:

Starting with [1,2][4,5,6], we iterate on the second cluster, increasing its leading value by 1 until we reach [1,2][98,99,100]. Since the leading value goes from 4 to 98, we see that this steps through 95 possible instances. Next we increase the leading value of the 2-member cluster by 1, and repeat the process, iterating from [2,3][5,6,7] to [2,3][98,99,100]. As there is one less possible position for the 3-member cluster to move through, this time it will only iterate 94 times.

On subsequent runs, each time "nudging over" the 2-cluster by one, the 3-cluster will only have 93 positions to iterate through, followed by 92 positions, and for forth, until we've reached [95,96][98,99,100], where the 3-cluster will only have a single position it can occupy.

At this point we will have exhausted all possible instances of a 2-cluster followed by a 3-cluster. The number of possible friendly sets thus generated can be calculated using the summation formula for a sequence from 1 to 95:

<img src="https://render.githubusercontent.com/render/math?math=\sum_{i=1}^{i=95}i=\frac{95*96}{2}=4560"> 

---
In total therefore we have 96 + 4560 + 4560, or 9216 possible ways of generating five member friendly sets whose elements lie between 1 and 100 inclusively.
