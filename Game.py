
#! Функции:

def indents(): # Отступы
  print()
  print()
  pass

def introduction(): # Вступление
  print ('''Привет, решил провести время с пользой?
-Молодец!
Основные правила игры:
Я буду обращаться на "Вы" независимо кто и как ты, ой, Вы
Чтобы ответить мне набирайте на клавиатуре ответ и нажимайте Enter
Нажмите "1" и Enter: ''')
  introduction = input ()
  introduction = int(error(introduction))
  verification_of_consent(introduction)
  indents()
  print ('Так, продолжаем')
  nickname = name_user()
  return nickname

def name_user(): # Знакомство с пользователем
  print ('Для начала игры введите своё имя')
  name  = input ()
  name = name_verification(name)
  print ('Теперь введите свою фамилию') 
  secondname = input ()
  secondname = secondname_verification(secondname)
  print ('Замечательно,' , name + ', теперь напишите год Вашего рождения')
  year = 2020
  age = input()
  age = int(error(age))
  age = year - age
  while (age <= 0) or (age >= 120):
    print('Хмм.. Некорректный год, попробуйте ввести свой возраст')
    age = input()
    age = int(error(age))
  nickname = age_verification_nickname(age)
  return nickname

def age_verification_nickname(age): # Проверка на возраст + никнейм
  if (12 - age <= 0):
    print('Вы успешно зарегестрировались, под ником "SvinkaPeppa_225".. эмм.. стоп! Вы не ввёли свой ник, прошу')
    nickname = input ()
    return nickname
  else:
    print ('Извини, но ты ещё слишком мал.')
    leave_the_game()


def name_verification(name): # Проверяет имя (чтобы были только буквы)
  while not name.isalpha():
    print ('Введите настоящее имя:')
    name = input()
  return name
  
def secondname_verification(secondname): # Проверяет фамилию (чтобы были только буквы)
  while not secondname.isalpha():
    print ('Введите настоящую фамилию:')
    secondname = input()
  return secondname

def verification_of_consent(introduction): # Проверка на введенное подтверждение - '1'
  while introduction != 1:
    print ('''Извините, но я не знаю такой команды.
Попробуйте повторить попытку:''')
    introduction = input ()
    introduction = int(error(introduction))
  return introduction

def menu(): # Меню
  indents()
  print ('''Замечательно, ''', nickname  ,''', теперь выберите игру:

Сколько воды нужно пить в день -  выберите "1"
Тест "Насколько богат Ваш лексикон" -  выберите "2"
Sorry, but this game is in development -  выберите "3"
Угадай число -  выберите "4"

Чтобы выйти с игры - нажмите "0"
''')
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
      index_game = int(error(index_game))
      x = 0
  return index_game

def game(enter_game): # Направление на игру
  if int(enter_game) == 0:
    return leave_the_game()
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
  while not((int(weight) > 10) and (int(weight) < 350)):
    print ('Введите свой НАСТОЯЩИЙ вес')
    weight = input ()
    weight = error(weight)
  print (round(int(weight) * 0.03, 2), 'литров воды Вам нужно выпивать в сутки, чтобы водяной баланс находился в норме')
  indents()

def game_2(): # Вторая игра
  indents()
  print ('''Как подсчитали ученые-лингвисты, в русском языке около 500 000 слов.
У великого русского поэта А. С. Пушкина, знатока и мастера языка, в литературной речи было 21 197 слов.
У выпускника средней школы словарный запас составляет в среднем от 2000 до 5000 слов,
а Эллочка-людоедка обходилась тридцатью, но ими она могла выразить практически любую мысль.
Судари и сударыни, пройдите тест и обогатите свой лексикон или порадуйтесь своим знаниям!
Количество вопросов в тесте: 10
Возможные вводимые ответы: "1", "2", "3"''')
  ask_number = int(0)
  questions()

def one_two_three (ask): # Проверяет, чтобы ответ == 1, 2 или 3
  while not ((int(ask) == 1) or (int(ask) == 2) or (int(ask) == 3)):
    print ('Ответьте ещё раз, ваш ответ некорректен')
    ask = input ()
    ask = int(error(ask))
  return ask
  
def questions(): # Вопросы
  ask_number = 0
  progress = 0
  ask_number += int(1)
  if int(ask_number) == 1:
    indents()
    print ('Вопрос №', ask_number, ': ')
    print ('Кто такой деверь? \n\n1)Брат мужа \n\n2)Оконный мастер \n\n3)Крупный феодал')
    ask = input ()
    ask = int(error(ask))
    one_two_three(ask)
    indents()
    if int(ask) == 1:
      progress +=1
      print ('Верный ответ!')
      print ('Ваш прогресс:', progress,'/ 10')
    else:
      print ('Неверный ответ')
      print ('Ваш прогресс:', progress,'/ 10')
      indents()

  ask_number += int(1)
  if int(ask_number) == 2:
    indents()
    print ('Вопрос №', ask_number, ': ')
    print ('Знакомо ли вам слово «курвиметр»? \n\n1)Механическая модель \n\n2)Прибор для измерения длины кривых линий \n\n3)Измеритель веса цыплят')
    ask = input ()
    ask = int(error(ask))
    one_two_three(ask)
    indents()
    if int(ask) == 2:
      progress +=1
      print ('Верный ответ!')
      print ('Ваш прогресс:', progress,'/ 10')
    else:
      print ('Неверный ответ')
      print ('Ваш прогресс:', progress,'/ 10')
      indents()

  ask_number += int(1)
  if int(ask_number) == 3:
    indents()
    print ('Вопрос №', ask_number, ': ')
    print ('Что означает прилагательное «матримониальный»? \n\n1)Правомерный \n\n2)Брачный \n\n3)Финансовый')
    ask = input ()
    ask = int(error(ask))
    one_two_three(ask)
    indents()
    if int(ask) == 2:
      progress +=1
      print ('Верный ответ!')
      print ('Ваш прогресс:', progress,'/ 10')
    else:
      print ('Неверный ответ')
      print ('Ваш прогресс:', progress,'/ 10')
      indents()

  ask_number += int(1)
  if int(ask_number) == 4:
    indents()
    print ('Вопрос №', ask_number, ': ')
    print ('Какое красивое слово «бриошь», а каково его значение? \n\n1)Ювелирное украшение \n\n2)Французский крем \n\n3)Сдобная круглая булочка')
    ask = input ()
    ask = int(error(ask))
    one_two_three(ask)
    indents()
    if int(ask) == 3:
      progress +=1
      print ('Верный ответ!')
      print ('Ваш прогресс:', progress,'/ 10')
    else:
      print ('Неверный ответ')
      print ('Ваш прогресс:', progress,'/ 10')
      indents()

  ask_number += int(1)
  if int(ask_number) == 5:
    indents()
    print ('Вопрос №', ask_number, ': ')
    print ('Слово «пропих» звучит странно, но оно есть. \n\n1)Запрещённый удар в бильярде \n\n2)Остаток пропана \n\n3)Образец написания знаков')
    ask = input ()
    ask = int(error(ask))
    one_two_three(ask)
    indents()
    if int(ask) == 1:
      progress +=1
      print ('Верный ответ!')
      print ('Ваш прогресс:', progress,'/ 10')
    else:
      print ('Неверный ответ')
      print ('Ваш прогресс:', progress,'/ 10')
      indents()

  ask_number += int(1)
  if int(ask_number) == 6:
    indents()
    print ('Вопрос №', ask_number, ': ')
    print ('Кто чаще пользуется каподастром? \n\n1)Землепользователи, это их инструмент \n\n2)Никто, это мифическое существо \n\n3)Гитаристы')
    ask = input ()
    ask = int(error(ask))
    one_two_three(ask)
    indents()
    if int(ask) == 3:
      progress +=1
      print ('Верный ответ!')
      print ('Ваш прогресс:', progress,'/ 10')
    else:
      print ('Неверный ответ')
      print ('Ваш прогресс:', progress,'/ 10')
      indents()

  ask_number += int(1)
  if int(ask_number) == 7:
    indents()
    print ('Вопрос №', ask_number, ': ')
    print ('Что такое фишю? \n\n1)Морская рыбка \n\n2)Кружевная косынка \n\n3)Окрас лошади')
    ask = input ()
    ask = int(error(ask))
    one_two_three(ask)
    indents()
    if int(ask) == 2:
      progress +=1
      print ('Верный ответ!')
      print ('Ваш прогресс:', progress,'/ 10')
    else:
      print ('Неверный ответ')
      print ('Ваш прогресс:', progress,'/ 10')
      indents()

  ask_number += int(1)
  if int(ask_number) == 8:
    indents()
    print ('Вопрос №', ask_number, ': ')
    print ('Слово «зарница», что обозначает оно? \n\n1)Отдаленная вспышка на небосклоне \n\n2)Падающая звезда \n\n3)Военно-спортивная игра')
    ask = input ()
    ask = int(error(ask))
    one_two_three(ask)
    indents()
    if int(ask) == 1:
      progress +=1
      print ('Верный ответ!')
      print ('Ваш прогресс:', progress,'/ 10')
    else:
      print ('Неверный ответ')
      print ('Ваш прогресс:', progress,'/ 10')
      indents()

  ask_number += int(1)
  if int(ask_number) == 9:
    indents()
    print ('Вопрос №', ask_number, ': ')
    print ('Говорят, что он банальный. Но нам ближе слово... \n\n1)Неоригинальный \n\n2)Невкусный \n\n3)Иностранный')
    ask = input ()
    ask = int(error(ask))
    one_two_three(ask)
    indents()
    if int(ask) == 1:
      progress +=1
      print ('Верный ответ!')
      print ('Ваш прогресс:', progress,'/ 10')
    else:
      print ('Неверный ответ')
      print ('Ваш прогресс:', progress,'/ 10')
      indents()

  ask_number += int(1)
  if int(ask_number) == 10:
    indents()
    print ('Вопрос №', ask_number, ': ')
    print ('Пушкин писал: «Его чело, его ланиты мгновенным пламенем горят...» А что такое ланиты? \n\n1)Щёки \n\n2)Доспехи \n\n3)Глаза')
    ask = input ()
    ask = int(error(ask))
    one_two_three(ask)
    indents()
    if int(ask) == 1:
      progress +=1
      print ('Верный ответ!')
      print ('Ваш прогресс:', progress,'/ 10')
    else:
      print ('Неверный ответ')
      print ('Ваш прогресс:', progress,'/ 10')
      indents()

    if progress <= 3: # Завершающая часть
        print ('Вы ответили на', progress ,'вопросов верно. Попробуйте ещё раз, я уверена, у Вас всё получится')
    if (progress <= 6) and (not (progress <= 3)):
        print ('Вы ответили на', progress ,'вопросов верно. Неплохой результат, но Вы можете и лучше, попробуйте ещё разок')
    if (progress <= 9) and (not (progress <= 6)):
        print ('Вы ответили на', progress ,'вопросов верно. Хороший результат, но даже это нужно довести до идеала. Дерзай!')
    if (progress == 10):
        print ('Вы ответили на все', progress ,'вопросов верно. Вы молодец!!! Но... "Достигнув вершины приготовься оказаться на дне следующего уровня" Не останавливайс на достигнутом')
  pass

def game_3(): # Третяя игра #? Доделать!!!
  indents()
  print('Sorry, but this game is in development')
  indents()

def game_4(): # Четвёртая игра #? Доделать уровни сложности(рандинт растянуть до  100, 500, 1000 + добавить Lava + сделать очки
  indents()
  print ('''Суть игры:
Угадать случайно загаданное мной число в диапазоне от 0 до 100 включительно за наименьшее количество попыток.
Такие слова как: "Лёд", "Холодно", "Тепло", "Горячо", "Огонь", "Угадали!!!" будут помогать определить насколько далеко вы от цели''')
  print ('Введите число:')
  indents()
  known_number = input ()
  known_number = int(error(known_number))

  from random import randint
  unknown_number = int(randint (0, 100))
  attempts = 1
  
  while (unknown_number != known_number):
      attempts += 1
      if (known_number < 0):
          print ('Ошибка, это число меньше 0')
      if (known_number > 100):
          print ('Ошибка, это число больше 100')
      if abs(unknown_number - known_number) <= 5:
          print ('Огонь')
      elif abs(unknown_number - known_number) <= 20:
          print ('Горячо')
      elif abs(unknown_number - known_number) <= 35:
          print ('Тепло')
      elif abs(unknown_number - known_number) <= 60:
          print ('Холодно')
      elif abs(unknown_number - known_number) <= 100:
          print ('Лёд')

      known_number = input ()
      known_number = int(error(known_number))
      if attempts == 15:
        print('Извините, Вы проиграли')
        return menu() #? Доделать, чтобы была 1 менюшка
     
  print ('Угадали!!!')
  print ('Ура, у Вас получилось!!! Спустя', attempts, 'попыток Вы угадали число!')
  indents()
  
def leave_the_game(): # Выход из игры
  print('Приходи ещё!!!')
  exit()

#! Начало программы
number_of_game = 5
nickname = introduction()
while number_of_game != 0:
  menu ()
  number_of_game = enter_game()
  game(number_of_game)

  



