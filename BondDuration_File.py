
def getBondDuration(y, face, couponRate, m, ppy = 1):
  cf = face * couponRate
  pvcf = 0
  t = 1
  tot = 0
  pvcft = 0
  
  for t in range(m):
    pvcf = cf * (1 + y) ** -t
    tot = tot + pvcf
    pvcft = pvcft + pvcf * t
  
  tot = tot + face * (1 + y) ** -m
  pvcft = pvcft + (face * (1 + y) ** -m) * m
  Bond = tot
  Duration = pvcft / Bond
  return (Duration)