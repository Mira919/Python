from application.salary import calculate_salary
from application.db.people import get_employees
import datetime

def get_date():
    print(datetime.date.today())

if __name__ == '__main__':
    get_date()
    calculate_salary()
    get_employees()