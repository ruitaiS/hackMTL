## Question:
We have a 2^n × 2^n matrix that can only contain 0 and 1. The string S corresponding to matrix M is computed as follows:
If all the entries of M are 0 then S = 0
If all the entries of M are 1 then S =1

Otherwise, M is divided into 4 equal matrices: M1, M2, M3, M4 with S1, S2, S3, S4 as their corresponding strings. Then S is computed as follows:
S = 2 S1 S2 S3 S4

Q1. For a 16 x 16 matrix, how many corresponding S strings can we have?

Q2. Which one of the following is a valid S?
a) 2 0 1 0 2 1 0 2 1 0 1 0 1 0
b) 2 1 1 2 0 0 2 0 0 0 0 0 1
c) 2 0 2 2 1 1 1 0 1 1 1 1 1

Q3. Write a program that verifies if a string S is valid.

---
## Answers:

Q1: If we can prove that every unique binary square matrix of a given size 2^n has a unique mapping, then this question reduces to finding the number of possible binary square matrices of size 2^n.

#### Proof By Induction:
(Note that this is not a proof that for every S string there exists a unique matrix - this is easily disproven, as every zero matrix and every matrix of ones will be mapped to S = 1 and S = 0, respectively. Rather we are trying to show that for a given size 2^n, every possible binary matrix of that size will have a unique S string)

For n = 0, the matrix only has one element, 1 or 0, which is uniquely mapped to S = 1 or S = 0

For any matrix of size n, assuming that matrices of size 2^(n-1) have a unique mapping:
  * If the matrix is comprised of all 1's or 0's, then it will be uniquely mapped to S = 1 or S = 0, respectively
  * Otherwise the matrix will be mapped to S = 2 S1 S2 S3 S4, where S1-S4 are the unique mappings its component 2^(n-1) size submatrices. S1-S4 are unique mappings by assumption, and the ordering of them within S is unique, so therefore S itself must also be unique.
  
---






