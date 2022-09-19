import random
from datetime import date
from faker import Faker
from typing import Type

class Worker():
    def __init__(self) -> None:
        self.name = ''
        self.__registration = ''
        self.__admission = ''
        self.__salary = 'N/A'
        self._dept = 'N/A'
        self._level = 'N/A2'
        self._office = 'N/A'

    @staticmethod
    def select_randon() -> dict:
        worker_data = {}
        new_dept = random.choice(["Finance", "Mkt", "Commercial", "TI"])
        worker_data['dept'] = new_dept
        new_office = random.choice(["main", "coworking", "remote"])
        worker_data['office'] = new_office
        new_level = random.choice(["Analyst Jr", "Analyst Mid", "Analyst Sr"])
        worker_data['level'] = new_level
        return worker_data


# Dados - Workers
# [{
#     "name": "Indiv_str",
#     "registration": "Indiv_int",
#     "admission": "MM/AAAA",
#     "dept": ["Finance", "Mkt", "Commercial", "TI"],
#     "level": ["Analyst", "Coord", "Manager"],
#     "office": ["main", "cowork", "remote"]
#     "salary": int(),
#     "costcenter": "C+first_letter_dept+first_letter_level",
#     "perf_indicator": ["decreasing", "regular", "evolving"]
# }]

if __name__ == '__main__':
    data = date(2002, 4, 28)
    data3 = data.strftime('%d/%m/%Y')   # 28/04/2002

    # GERANDO UM NOME FAKE - OK
    fake = Faker()
    test_name = fake.name()
    print(test_name)
