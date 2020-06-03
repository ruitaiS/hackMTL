#Calculates the number of possible S strings for a 2^n by 2^n matrix
#Original question asks for n = 4
def q1(n):
    if n == 0: return 2
    else: return (q1(n-1))**4
def q1Alt(n):
    return 2**(2**(2*n))

for i in range(0, 5):
    print(q1(i))
    print(q1Alt(i))

#def q3(s):
    
