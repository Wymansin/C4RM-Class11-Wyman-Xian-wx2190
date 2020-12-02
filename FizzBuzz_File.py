

def FizzBuzz(start, finish):

  n = finish-start+1
  v = []
  i = 0
  
  for i in range(n):
    if ((i + start) % 3 == 0 & (i + start) % 5 == 0):
      v.append("fizzbuzz")
    
    
    elif ((i + start) % 5 == 0):
      v.append("Buzz")
    
    elif ((i + start) % 3 == 0):
      v.append("Fizz")
    
    else:
      v.append(i + start)

  print(v)

  return(v)
