# Определение знака зодиака по дате рождения

month = input('Введите месяц: ')
number = int(input('Введите число: '))
if ((month == 'март') and (21 <= number <= 31)) or ((month == 'апрель') and (1 <= number <= 20)):
    zodiac_sign = 'Овен'

if ((month == 'апрель') and (21 <= number <= 30)) or ((month == 'май') and (1 <= number <= 20)):
    zodiac_sign = 'Телец'

if ((month == 'май') and (21 <= number <= 31)) or ((month == 'июнь') and (1 <= number <= 21)):
    zodiac_sign = 'Близнецы'

if ((month == 'июнь') and (22 <= number <= 30)) or ((month == 'июль') and (1 <= number <= 22)):
    zodiac_sign = 'Рак'

if ((month == 'июль') and (23 <= number <= 31)) or ((month == 'август') and (1 <= number <= 23)):
    zodiac_sign = 'Лев'

if ((month == 'август') and (24 <= number <= 31)) or ((month == 'сентябрь') and (1 <= number <= 23)):
    zodiac_sign = 'Дева'

if ((month == 'сентябрь') and (24 <= number <= 30)) or ((month == 'октябрь') and (1 <= number <= 23)):
    zodiac_sign = 'Весы'

if ((month == 'октябрь') and (24 <= number <= 31)) or ((month == 'ноябрь') and (1 <= number <= 22)):
    zodiac_sign = 'Скорпион'

if ((month == 'ноябрь') and (23 <= number <= 30)) or ((month == 'декабрь') and (1 <= number <= 21)):
    zodiac_sign = 'Стрелец'

if ((month == 'декабрь') and (22 <= number <= 31)) or ((month == 'январь') and (1 <= number <= 20)):
    zodiac_sign = 'Козерог'

if ((month == 'январь') and (21 <= number <= 31)) or ((month == 'февраль') and (1 <= number <= 20)):
    zodiac_sign = 'Водолей'

if ((month == 'февраль') and (21 <= number <= 30)) or ((month == 'март') and (1 <= number <= 20)):
    zodiac_sign = 'Рыбы'

print('Вывод:')
print(zodiac_sign)
