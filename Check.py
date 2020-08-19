def name_verification(name):
  while not str.isalpha(name):
    print ('Введите настоящее имя:')
    name = input()
  return name
  
def secondname_verification(secondname):  
  while not str.isalpha(name):
    print ('Введите настоящую фамилию:')
    name = input()
  return secondname

name_verification(name)
