
#! Функции:

def menu(): # Меню
  print ('''Замечательно, ', nickname + ', теперь выберите игру: 
Сколько воды нужно пить в день -  выберите "1"
Тест "Насколько богат Ваш лексикон -  выберите "2"
Насколько вы отличаетесь от "среднего человека" -  выберите "3"
Угадай число -  выберите "4"
Выйти с игры - нажмите "0"''')
  pass

def enter_game(): # Выбор игры
  index_game = input ('Введите номер игры: ')
  index_game = error (index_game)
  return cheking_game(index_game)

def cheking_game(index_game): # Проверяет номер игы
  index_game = error(index_game)
  while not (int(index_game) < 6) and (int(index_game) >= 1):
    print ('Выберите игру ещё раз: ')
    index_game = input ()
    index_game = error(index_game)
  return (index_game)
  
def error(index_game): # Проверяет введённый параметр на наличие ошибок(только для чисел!)
  x = 1
  if x == 1:
    try:
      int(index_game) - 0
    except:
      print ('Некорректный ввод, попробуйте ещё раз: ')
      index_game = input ()
      index_game = error(index_game)
      x = 0
  return index_game

def game(enter_game): # Направление на игру
  if enter_game == 0:
    return exit_of_game()
  if enter_game == 1:
    return game_1()
  if enter_game == 2:
    return game_2()
  if enter_game == 3:
    return game_3()
  if enter_game == 4:
    return game_4()

def game_1(): # Первая игра
  print ()
  print ('Чтобы посчитать, сколько Вам нужно выпивать воды в сутки мне нужно знать ваш вес')
  print ('Введите свой вес')
  weight = int(input ())
  weight = error(weight)
  while (not(weight > 10)) and (not(weight < 200)):
      print ('Введите свой НАСТОЯЩИЙ вес')
      weight = int(input ())
      weight = error(weight)
  print (round((weight) * 0.03), 'литров воды Вам нужно выпивать в сутки, чтобы водяной баланс находился в норме')
  print () 



#! Начало программы

menu ()
number_of_game = enter_game()
game(number_of_game)

  



