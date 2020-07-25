'''Простое число'''

number = int(input ('Enter a number '))
delit = 2
while ((number % delit) != 0) and ((number != delit)):
  for delit in range (1,number):
    print (delit)

print ('The programme is finished')