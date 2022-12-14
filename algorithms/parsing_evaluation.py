
def correctOr(): 
    P = True
    return P or Q

def correctAnd(): 
    P = False 
    return P and Q

def bugOr(): 
    P = False
    return P or Q 

def bugAnd(): 
    P = True
    return P and Q