

def getBondPrice(y, face, couponRate, m, ppy=1):
 coup = face * couponRate / ppy
 m = m * ppy
 y = y / ppy
 Bond = (coup * (1 - (1 + y) ^ (-m)) / (y)) + face * (1 + y) ^ (-m)
 return (Bond)
