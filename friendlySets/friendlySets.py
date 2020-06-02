#How many friendly sets can be created with 5 members, where members range from 1 to 100?

#Case 1: All five are grouped together
#Case 2: A group of two, followed by a group of 3
#Case 3: A group of three, followed by a group of 2

def case1(n):
    ret = "["
    for i in range (4):
        ret = ret + str(n + i) + ","
    ret = ret + str(n+4) + "]"
    print(ret)
    if (n + 5)<101:
        return 1 + case1(n+1)
    else:
        return 1

def case2(n, g):
    ret = "[" + str(n) + str(n+1)
    for i in range(n+g+2, n+g+4):
        ret = ret + str(i) + ","
    ret = ret + str(n+g+5)+"]"
    print(ret)
    if (n+g+6)<101:
        return 1 + case2(n, g+1)
    elif (g != 1):
        return 1 + case2(n + 1, 1)
    else:
        return 1

print("Total for Case 1: " + str(case1(1)))
print("Total for Case 2: " + str(case2(1,1)))

