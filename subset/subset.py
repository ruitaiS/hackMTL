def twoMember():
    res = ([10,6], [9,7])
    for i in range (1, 8):
        res += (i, 8-i)
    return res

print(twoMember())
