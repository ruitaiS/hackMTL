'''
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
'''

def q1(n):
    
