

def getBondPrice_E(face, couponRate, m, yc):

 coup = face * couponRate
 
 for index,value in enumerate(yc):
  pv = (1 + value) ** - (index + 1) 
  
 Bond = coup * (sum(pv) + pv[-1])

 return (Bond)


