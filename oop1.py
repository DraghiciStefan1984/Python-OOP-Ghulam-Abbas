class Employee:
    company='Dreamin'
    def __init__(self, name, age, salary):
        self.name=name
        self.age=age
        self.salary=salary

    #instance method
    def set_salary(self, sal):
        self.salary=sal

    def get_salary(self):
        return self.salary

    #static method
    @staticmethod
    def company_info():
        print(f'{Employee.company} is awesome!')

    def __str__(self):
        return f'{self.name} is {self.age} old, works at {self.company} and earns {self.salary} RON per month.'


#test
e=Employee('Stefan', 35, 6500)
print(e.get_salary())
e.set_salary(8000)
print(e.get_salary())
print(e.age)
print(e.company)
print(e)
e.company_info()
Employee.company_info()