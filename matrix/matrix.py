#Calculates the number of possible S strings for a 2^n by 2^n matrix
#Original question asks for n = 4
def q1(n):
    if n == 0: return 2
    else: return (q1(n-1))**4

print(q1(4))

def q3(s):
    s = s.replace(" ", "")
    count = 1;
    for c in s:
        if c == "2":
            count += 3
        elif (c == "1")or(c == "0"):
            count -= 1
        else:
            return False

    if count != 0: return False
    else: return True

print(q3("2 0 1 0 2 1 0 2 1 0 1 0 1 0"))
print(q3("2 1 1 2 0 0 2 0 0 0 0 0 1"))
print(q3("2 0 2 2 1 1 1 0 1 1 1 1 1"))
