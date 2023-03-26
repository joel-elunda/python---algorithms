
import random 

def P(X): 
    return random.randrange(2) == 0 

def nbXverifiantP(T): 
    nb = 0 
    for i in range(len(T)): 
        pass
    
def minX(T):
    if len(T) ==  0: 
        return None 
    
    iMin = 0 
    minX = T[iMin]
    
    for i in range (1, len(T)): 
        if T[i] < minX: 
            minX = T[i]
            
    return [minX, iMin]

def maxX(T): 
    if len(T) == 0: 
        return None 
    
    iMax = 0
    maxX = T[iMax]
    
    for i in range(1, len(T)): 
        if T[i] > maxX: 
            iMax = i
            maxX = T[i]
            
    return [maxX, iMax]