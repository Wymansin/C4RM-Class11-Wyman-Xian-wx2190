

def getBondPrice_Z(face, couponRate, times, yc):
    pv=[]
    coup = couponRate * face
    for index,value in enumerate(yc):
        pv.append((1+(value))**-times[index])
        
    Bond = coup * sum(pv) + pv[-1] * face
    
    return(Bond)

yc = [.010,.015,.020,.025,.030]
times=[1,1.5,3,4,7]
face = 2000000
couponRate = .04


z = getBondPrice_Z(face, couponRate, times, yc)