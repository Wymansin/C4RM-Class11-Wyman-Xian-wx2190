

def getBondPrice_Z(face, couponRate, times, yc):
    pv=[]
    coup = couponRate * face
    for index,value in enumerate(yc):
        pv.append((1+(value))**-times[index])
        
    Bond = coup * sum(pv) + pv[-1] * face
    
    return(Bond)