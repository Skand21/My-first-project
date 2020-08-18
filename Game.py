
#! Функции:

def indents(): # Отступы
  print()
  print()
  print()
  pass

def menu(): # Меню
  indents()
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
  if int(enter_game) == 0:
    return exit_of_game()
  if int(enter_game) == 1:
    return game_1()
  if int(enter_game) == 2:
    return game_2()
  if int(enter_game) == 3:
    return game_3()
  if int(enter_game) == 4:
    return game_4()

def game_1(weight = 0): # Первая игра
  indents()
  print ('Чтобы посчитать, сколько Вам нужно выпивать воды в сутки мне нужно знать Ваш вес')
  print ('Введите свой вес:')
  weight = input ()
  weight = error(weight)
  while not((int(weight) > 10) and (int(weight) < 200)):
    print ('Введите свой НАСТОЯЩИЙ вес')
    weight = input ()
    weight = error(weight)
  print (round(int(weight) * 0.03, 2), 'литров воды Вам нужно выпивать в сутки, чтобы водяной баланс находился в норме')
  indents()

def game_2(): # Вторая игра
  progress = 0
  print ('''Как подсчитали ученые-лингвисты, в русском языке около 500 000 слов.
У великого русского поэта А. С. Пушкина, знатока и мастера языка, в литературной речи было 21 197 слов.
У выпускника средней школы словарный запас составляет в среднем от 2000 до 5000 слов,
а Эллочка-людоедка обходилась тридцатью, но ими она могла выразить практически любую мысль.
Судари и сударыни, пройдите тест и обогатите свой лексикон или порадуйтесь своим знаниям!
Количество вопросов в тесте: 10
Возможные вводимые ответы: "1", "2", "3"''')
  ask_number = int(0)
  def questions(ask_number):
    ask_number += int(1)
    if int(ask_number) == 1:
      indents()
      print ('Вопрос №', ask_number, ': ')
      print ('Кто такой деверь? \n\n1)Брат мужа \n\n2)Оконный мастер \n\n3)Крупный феодал')
      ask = int(input ())
      error(ask)
      answers(ask)
    
    ask_number += int(1)
    if int(ask_number) == 2:
      indents()
      print ('Вопрос №', ask_number, ':')
      print ('Знакомо ли вам слово «курвиметр»? \n\n1)Механическая модель \n\n2)Прибор для измерения длины кривых линий \n\n3)Измеритель веса цыплят')
      ask = int(input ())
      error(ask)
      answers(ask)
  
  def answers(ask, ask_number):
    while not (((int(ask) == 1) or (int(ask) == 2) or (int(ask) == 3))):
      print ('Ответьте ещё раз, ваш ответ некорректен')
      print ('Кто такой деверь? \n\n1)Брат мужа \n\n2)Оконный мастер \n\n3)Крупный феодал')
      ask = int(input ())
      error(ask)

    if int(ask_number) == 1:
      indents()
      if ask == 1:
        progress +=1
        print ('Верный ответ!')
        print ('Ваш прогресс:', progress,'/ 10')
      else:
        print ('Неверный ответ')
        print ('Ваш прогресс:', progress,'/ 10')
        indents()
      
      while not (((int(ask) == 1) or (int(ask) == 2) or (int(ask) == 3))):
          print ('Ответьте ещё раз, ваш ответ некорректен')
          print ('Знакомо ли вам слово «курвиметр»? \n\n1)Механическая модель \n\n2)Прибор для измерения длины кривых линий \n\n3)Измеритель веса цыплят')
          ask = int(input ())
  
      if ask == 2:
          progress +=1
          print ('Верный ответ!')
          print ('Ваш прогресс:', progress,'/ 10')
  
      elif (int(ask) == 1) or (int(ask) == 3):
          print ('Неверный ответ')
          print ('Ваш прогресс:', progress,'/ 10')
      print ()
      ask_number += int(1)
      print ('Вопрос №', ask_number, ':')
      print ('Что означает прилагательное «матримониальный»? \n\n1)Правомерный \n\n2)Брачный \n\n3)Финансовый')
      ask = int(input ())
  
      while not (((int(ask) == 1) or (int(ask) == 2) or (int(ask) == 3))):
          print ('Ответьте ещё раз, ваш ответ некорректен')
          print ('Что означает прилагательное «матримониальный»? \n\n1)Правомерный \n\n2)Брачный \n\n3)Финансовый')
          ask = int(input ())
  
      if ask == 2:
          progress +=1
          print ('Верный ответ!')
          print ('Ваш прогресс:', progress,'/ 10')
  
      elif (int(ask) == 1) or (int(ask) == 3):
          print ('Неверный ответ')
          print ('Ваш прогресс:', progress,'/ 10')
      print ()
      ask_number += int(1)
      print ('Вопрос №', ask_number, ':')
      print ('Какое красивое слово «бриошь», а каково его значение? \n\n1)Ювелирное украшение \n\n2)Французский крем \n\n3)Сдобная круглая булочка')
      ask = int(input ())
  
      while not (((int(ask) == 1) or (int(ask) == 2) or (int(ask) == 3))):
          print ('Ответьте ещё раз, ваш ответ некорректен')
          print ('Какое красивое слово «бриошь», а каково его значение? \n\n1)Ювелирное украшение \n\n2)Французский крем \n\n3)Сдобная круглая булочка')
          ask = int(input ())
  
      if ask == 3:
          progress +=1
          print ('Верный ответ!')
          print ('Ваш прогресс:', progress,'/ 10')
  
      elif (int(ask) == 1) or (int(ask) == 2):
          print ('Неверный ответ')
          print ('Ваш прогресс:', progress,'/ 10')
      print ()
      ask_number += int(1)
      print ('Вопрос №', ask_number, ':')
      print ('Слово «пропих» звучит странно, но оно есть. \n\n1)Запрещённый удар в бильярде \n\n2)Остаток пропана \n\n3)Образец написания знаков')
      ask = int(input ())
  
      while not (((int(ask) == 1) or (int(ask) == 2) or (int(ask) == 3))):
          print ('Ответьте ещё раз, ваш ответ некорректен')
          print ('Слово «пропих» звучит странно, но оно есть. \n\n1)Запрещённый удар в бильярде \n\n2)Остаток пропана \n\n3)Образец написания знаков')
          ask = int(input ())
  
      if ask == 1:
          progress +=1
          print ('Верный ответ!')
          print ('Ваш прогресс:', progress,'/ 10')
  
      elif (int(ask) == 2) or (int(ask) == 3):
          print ('Неверный ответ')
          print ('Ваш прогресс:', progress,'/ 10')
      print ()
      ask_number += int(1)
      print ('Вопрос №', ask_number, ':')
      print ('Кто чаще пользуется каподастром? \n\n1)Землепользователи, это их инструмент \n\n2)Никто, это мифическое существо \n\n3)Гитаристы')
      ask = int(input ())
  
      while not (((int(ask) == 1) or (int(ask) == 2) or (int(ask) == 3))):
          print ('Ответьте ещё раз, ваш ответ некорректен')
          print ('Кто чаще пользуется каподастром? \n\n1)Землепользователи, это их инструмент \n\n2)Никто, это мифическое существо \n\n3)Гитаристы')
          ask = int(input ())
  
      if ask == 3:
          progress +=1
          print ('Верный ответ!')
          print ('Ваш прогресс:', progress,'/ 10')
  
      elif (int(ask) == 1) or (int(ask) == 2):
          print ('Неверный ответ')
          print ('Ваш прогресс:', progress,'/ 10')
      print ()
      ask_number += int(1)
      print ('Вопрос №', ask_number, ':')
      print ('Что такое фишю? \n\n1)Морская рыбка \n\n2)Кружевная косынка \n\n3)Окрас лошади')
      ask = int(input ())
  
      while not (((int(ask) == 1) or (int(ask) == 2) or (int(ask) == 3))):
          print ('Ответьте ещё раз, ваш ответ некорректен')
          print ('Что такое фишю? \n\n1)Морская рыбка \n\n2)Кружевная косынка \n\n3)Окрас лошади')
          ask = int(input ())
  
      if ask == 2:
          progress +=1
          print ('Верный ответ!')
          print ('Ваш прогресс:', progress,'/ 10')
  
      elif (int(ask) == 1) or (int(ask) == 3):
          print ('Неверный ответ')
          print ('Ваш прогресс:', progress,'/ 10')
      print ()
      ask_number += int(1)
      print ('Вопрос №', ask_number, ':')
      print ('Слово «зарница», что обозначает оно? \n\n1)Отдаленная вспышка на небосклоне \n\n2)Падающая звезда \n\n3)Военно-спортивная игра')
      ask = int(input ())
  
      while not (((int(ask) == 1) or (int(ask) == 2) or (int(ask) == 3))):
          print ('Ответьте ещё раз, ваш ответ некорректен')
          print ('Слово «зарница», что обозначает оно? \n\n1)Отдаленная вспышка на небосклоне \n\n2)Падающая звезда \n\n3)Военно-спортивная игра')
          ask = int(input ())
  
      if ask == 1:
          progress +=1
          print ('Верный ответ!')
          print ('Ваш прогресс:', progress,'/ 10')
  
      elif (int(ask) == 2) or (int(ask) == 3):
          print ('Неверный ответ')
          print ('Ваш прогресс:', progress,'/ 10')
      print ()
      ask_number += int(1)
      print ('Вопрос №', ask_number, ':')
      print ('Говорят, что он банальный. Но нам ближе слово... \n\n1)Неоригинальный \n\n2)Невкусный \n\n3)Иностранный')
      ask = int(input ())
  
      while not (((int(ask) == 1) or (int(ask) == 2) or (int(ask) == 3))):
          print ('Ответьте ещё раз, ваш ответ некорректен')
          print ('Говорят, что он банальный. Но нам ближе слово... \n\n1)Неоригинальный \n\n2)Невкусный \n\n3)Иностранный')
          ask = int(input ())
  
      if ask == 1:
          progress +=1
          print ('Верный ответ!')
          print ('Ваш прогресс:', progress,'/ 10')
  
      elif (int(ask) == 2) or (int(ask) == 3):
          print ('Неверный ответ')
          print ('Ваш прогресс:', progress,'/ 10')
      print ()
      ask_number += int(1)
      print ('Вопрос №', ask_number, ':')
      print ('Пушкин писал: «Его чело, его ланиты мгновенным пламенем горят...» А что такое ланиты? \n\n1)Щёки \n\n2)Доспехи \n\n3)Глаза')
      ask = int(input ())
  
      while not (((int(ask) == 1) or (int(ask) == 2) or (int(ask) == 3))):
          print ('Ответьте ещё раз, ваш ответ некорректен')
          print ('Пушкин писал: «Его чело, его ланиты мгновенным пламенем горят...» А что такое ланиты? \n\n1)Щёки \n\n2)Доспехи \n\n3)Глаза')
          ask = int(input ())
  
      if ask == 1:
          progress +=1
          print ('Верный ответ!')
  
      elif (int(ask) == 2) or (int(ask) == 3):
          print ('Неверный ответ')
      if (progress <= 3):
          print ('Вы ответили на', progress ,'вопросов верно. Попробуйте ещё раз, я уверена, у Вас всё получится')
      if (progress <= 6) and (not (progress <= 3)):
          print ('Вы ответили на', progress ,'вопросов верно. Неплохой результат, но Вы можете и лучше, попробуйте ещё разок')
      if (progress <= 9) and (not (progress <= 6)):
          print ('Вы ответили на', progress ,'вопросов верно. Хороший результат, но даже это нужно довести до идеала. Дерзай!')
      if (progress == 10):
          print ('Вы ответили на все', progress ,'вопросов верно. Вы молодец!!! Но... "Достигнув вершины приготовься оказаться на дне следующего уровня" Не останавливайс на достигнутом')


#! Начало программы
number_of_game = 10
while number_of_game != 0:
  menu ()
  number_of_game = enter_game()
  game(number_of_game)

  



