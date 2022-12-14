
def loopFor(L, E, min, max): 
    for x in L: 
        print(x)
    for y in E: 
        print(y)
    for i in range(min, max + 1): 
        print(i)
        
def loopWhile(smin): 
    s = 0 
    i = 0 
    while s < smin: 
        s = s + i 
        i = i + 1 
    return i