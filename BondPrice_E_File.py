

def getBondPrice_E(face, couponRate, m, yc):
 
  pv=[]
  coup = couponRate * face
  for index,value in enumerate(yc):
        pv.append((1+(value))**-(index+1))

  Bond = coup * sum(pv) + pv[-1] * face
  
  return (Bond)
