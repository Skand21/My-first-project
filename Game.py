
#! Функции:

def menu():
  print ('''Замечательно, ', nickname + ', теперь выберите игру: 
Сколько воды нужно пить в день -  выберите "1"
Тест "Насколько богат Ваш лексикон -  выберите "2"
Насколько вы отличаетесь от "среднего человека" -  выберите "3"
Угадай число -  выберите "4"
Выйти с игры - нажмите "5"''')
  pass

def cheking_game(index_game):
  while not (int(index_game) < 6) and (int(index_game) >= 1):
    print ('Выберите игру ещё раз: ')
    index_game = int(input ())
  return (index_game)

 
def game_1():
  print ()
  print ('Чтобы посчитать, сколько Вам нужно выпивать воды в сутки мне нужно знать ваш вес')
  print ('Введите свой вес')
  weight = int(input ())
  while (not(weight > 10)) and (not(weight < 200)):
      print ('Введите свой НАСТОЯЩИЙ вес')
      weight = int(input ())
  print (round((weight) * 0.03, 2), 'литров воды Вам нужно выпивать в сутки, чтобы водяной баланс находился в норме')
  print () 


#! Начало программы

menu ()
index_game = input ('Введите номер игры: ')
index_game = cheking_game(index_game)
print ()


