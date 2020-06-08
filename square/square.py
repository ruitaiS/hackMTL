def p2(x, y):
    return (x+2-y, y-1+x)

def p3(x,y):
    p2x, p2y = p2(x,y)
    return (p2x+1-x, p2y+2- y)

def getPoints(x,y):
    return [(1,2), (x,y), p2(x,y), p3(x,y)]

def checkAdj(a, b):
    if (a[0] == a[1]) or (b[0]==b[1]): return False
    else: return (a[0] == b[0]) ^ (a[1] == b[1]) ^ (a[0]==b[1]) ^ (a[1]==b[0])
        
def checkOpp(a, b):
    pList = (a[0], a[1], b[0], b[1])
    for p in pList:
        if pList.count(p) > 1: return False
    return True

adjPoints = [(0,1), (1,2), (2,3), (3,0)]
oppPoints = [(0,2), (1,3)]

def include(sq):
    for p in sq:
        if (p[0]<1) or (p[1]<1) or (p[0]>10) or (p[1]>10) : return False
    for (a,b) in adjPoints:
        if not checkAdj(sq[a],sq[b]) : return False
    for (a,b) in oppPoints:
        if not checkOpp(sq[a],sq[b]) : return False
    return True

def getList():
    sqList = [] 
    for i in range(1, 11):
        for j in range(1,11):
            sq = getPoints(i, j)
            if include(sq):
                sqList.append(sq)
    for sq in sqList:
        print(sq)
        print("\n")


getList()
