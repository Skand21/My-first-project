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

def indents():
  print()

def game_4(): # Четвёртая игра #? Доделать уровни сложности рандинт растянуть до  100, 500, 1000 + сделать очки
  eggs = 0
  indents()
  print ('''Суть игры:
Угадать случайно загаданное мной число в диапазоне от 0 до 100 включительно за наименьшее количество попыток.
Такие слова как: "Лёд", "Холодно", "Тепло", "Горячо", "Огонь", "Лава", "Угадали!!!" будут помогать определить насколько далеко вы от цели''')
  while eggs != 1:
    l = verification_fourth_game()
    l()
  
  
def verification_fourth_game (level): # Проверка на угаданное число

  indents()
  attempts = 1
  level = 1
  print ('Введите число:')
  known_number = input ()
  known_number = int(error(known_number))
  l = l()
  from random import randint
  unknown_number = int(randint (0, l))

  while (unknown_number != known_number) and (attempts != 20):
    attempts += 1
    if (known_number < 0):
        print ('Ошибка, это число меньше 0')
    if (known_number > l):
        print ('Ошибка, это число больше 100')

    if abs(unknown_number - known_number) <= l * 0.02:
        print ('Лава')
    elif abs(unknown_number - known_number) <= l * 0.1:
        print ('Огонь')
    elif abs(unknown_number - known_number) <= l * 0.25:
        print ('Горячо')
    elif abs(unknown_number - known_number) <= l * 0.4:
        print ('Тепло')
    elif abs(unknown_number - known_number) <= l * 0.6:
        print ('Холодно')
    elif abs(unknown_number - known_number) <= l * 0.75:
        print ('Лёд')

    known_number = input ()
    known_number = int(error(known_number))

  if unknown_number != known_number:
    print('Извините, Вы проиграли')
    eggs = 1
  else:
    print ('Угадали!!!')
    print ('Ура, у Вас получилось!!! Спустя', attempts, 'попыток Вы угадали число!')
    print ('Вы переходите на уровень', level)
    level += 1
    return l
    indents()

def l(level) : # Условия уровня
  if level == 1:
    l = 50
  elif level == 2:
    l = 100
  elif level == 3:
    l = 250
  elif level == 4:
    l = 500
  elif level == 5:
    l = 1000
  return l
