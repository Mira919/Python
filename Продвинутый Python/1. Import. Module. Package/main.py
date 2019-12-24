# вызвать функцию calculate_salary из другого файла
# вызвать функцию get_employees из другого файла
# cоздать рядом с файлом main.py модуль dirty_main.py и импортировать все функции с помощью конструкции *

from application.salary import calculate_salary
from application.db.people import get_employees
import datetime

def get_date():
    print(datetime.date.today())

if __name__ == '__main__':
    get_date()
    calculate_salary()
    get_employees()
