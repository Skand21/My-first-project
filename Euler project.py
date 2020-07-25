'''Простое число №3'''

number = int(46)

for p in range (2, number + 1):
  while ((number % p) != 0) and (number != p):
    print (p)







delit = 2
conclusion = 0
while ((number % delit) != 0) and ((number != delit)):
  number = number - 1
  for delit in range (2,number + 1):
    conclusion = (delit)
if conclusion == 0:
  print (conclusion)