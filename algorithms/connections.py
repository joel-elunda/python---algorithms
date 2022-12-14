
def civility(male, first_name, last_name): 
    if male: 
        print("Hello Mr %s %s" %(last_name, first_name))
    else: 
        print("Hello Mrs %s %s" %(last_name, first_name))
        
def minimum2VI(X, Y): 
    if X <= Y: 
        min = X
    else: 
        min = Y 
    return min 

def minimum2V2(X, Y): 
    if X <= Y: 
        return X 
    else: 
        return Y 
    
def minimum2V3(X, Y): 
    if X <= Y: 
        return X 
    return Y 

def minimum3V1(X, Y, Z): 
    if X <= Y:
        if X <= Z: 
            return X 
        else: 
            return Z 
    else: 
        if X <= Z: 
            return Y 
        else: 
            return Z
        
def minimum3V2(X, Y, Z): 
    if X <= Y and X <= Z: 
        return X 
    elif Y <= X and Y <= Z:
        return Y 
    else: 
        return Z