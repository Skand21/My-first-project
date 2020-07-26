#Simple Numbers

numbermain = 600851475143

x = 0
z = 0

for f in range (2, numbermain):
  if (numbermain % f == 0):
    numbermax = numbermain / f
    for i in range (2, int(numbermax + 1)):
      if i == numbermax:
        x = 1
      while x == 0:
        if ((numbermax % i) == 0):
          x = 1
          z += 1
        else:
          x = 1
    if z == 0:
      print (numbermax)