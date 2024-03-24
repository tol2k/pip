from application.salary import calculate_salary
from application.db.people import get_employees
import datetime as dt
from emoji import emojize
def get_date():
    print(dt.datetime.now())

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    get_date()
    print(emojize(":black_heart:"))
