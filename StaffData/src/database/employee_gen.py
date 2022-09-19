import json
from faker import Faker, Factory
import random


class employee:
    def __init__(self):
        # self.fake = Faker()
        self.dept = ['IT', 'Finance', 'Operational', 'Commercial', 'HR', 'Marketing']
        self.level = ['Analyst', 'Supervisor', 'Coordinator', 'Manager', 'Director']
        self.office = ['main', 'coworking', 'remote']
        self.date_year = [2019, 2020, 2021]
        self.perf_indicator = ['decreasing', 'regular', 'evolving']
        self.info = {}

    def create(self, reg: int):
        fake = Faker()
        self.info = {
            "_id": reg,
            "name": f"{fake.name()}",
            "dept": f"{random.choice(self.dept)}",
            "level":f"{random.choice(self.level)}",
            "office": f"{random.choice(self.office)}",
            "costcenter": "FI-M02",   # example
            "startdate": 'Jun/2020',   # for year make random on self.date_year and month call a random(datetime.month)
            "salary": 4350.00,  # float number with
            "perf_indicator": f"{random.choice(self.perf_indicator)}"
        }

        return self.info


class worker_gen:
    def __init__(self):
        # self.fake = Faker()
        self.dept = ['IT', 'Finance', 'Operational', 'Commercial', 'HR', 'Marketing']
        self.level = ['Analyst', 'Supervisor', 'Coordinator', 'Manager', 'Director']
        self.office = ['main', 'coworking', 'remote']
        self.date_year = [2019, 2020, 2021]
        self.perf_indicator = ['decreasing', 'regular', 'evolving']
        self.info = {}

    def create(self, reg: int):
        fake = Faker()
        self.info = {
            "_id": reg,
            "name": f"{fake.name()}",
            "dept": f"{random.choice(self.dept)}",
            "level":f"{random.choice(self.level)}",
            "office": f"{random.choice(self.office)}",
            "startdate": 'Jun/2020',   # for year make random on self.date_year and month call a random(datetime.month)
            "salary": 4350.00,  # float number with
            "perf_indicator": f"{random.choice(self.perf_indicator)}"
        }
        return self.info


if __name__ == '__main__':
    print("generating employees database\n")

    # with open('StaffData/src/data.json', 'r') as file:
    #     data = json.load(file)
    #     print(data)
    #     for i, item in enumerate(data):
    #         print(i)
    #         print(item)

    worker = employee()
    print(worker.create(104))

    # dept = ['IT', 'Finance', 'Operational', 'Commercial', 'HR', 'Marketing']
    # print(random.choice(dept))
