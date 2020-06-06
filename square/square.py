def p2(x, y):
    return (x+2-y, y-1+x)

def p3(x,y):
    p2x, p2y = p2(x,y)
    return (p2x+1-x, p2y+2- y)

def getPoints(x,y):
    return ((1,2), (x,y), p2(x,y), p3(x,y))

def checkAdj(a, b):
    if (a[0] == a[1]) or (b[0]==b[1]): return false
    else: return (a[0] == b[0]) ^ (a[1] == b[1]) ^ (a[0]==b[1]) ^ (a[1]==b[0])
        
def checkOpp(a, b):
    pList = (a[0], a[1], b[0], b[1])
    for p in pList:
        if pList.count(p) > 1: return false
    return true
    

#print("P2: " + str(p2(2,1)))
#print("P3: " + str(p3(2,1)))

for i in getPoints(2,1):
    print(i)
