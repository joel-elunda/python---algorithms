
def echangeV1(X, Y): 
    aux = X 
    X = Y 
    Y = aux 
    
def echangeV2(X, Y): 
    return Y, X 

def echangeV3(T, i, j): 
    aux = T[i]
    T[i] = T[j]
    T[j] = aux