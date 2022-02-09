from application.salary import calculate_salary as cs
from application.db.people import get_employees as ge
from datetime import date

if __name__ == '__main__':
    print(date.today())
    salary_from = cs(ge('Fedor'))
    print(salary_from)
