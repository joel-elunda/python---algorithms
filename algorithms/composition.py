
def minimum2(X, Y): 
    if X < Y: 
        return X 
    else: 
        return Y 
    
def minimum2(X, Y, Z): 
    return minimum2(minimum2(X, Y), Z)