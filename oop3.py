class Person:
    def set_data(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender


class Teacher(Person):
    def __init__(self, salary):
        self.salary=salary

    def show_teacher_data(self):
        print(f'{self.name} is {self.age} years old, {self.gender} and earns {self.salary}.')



class Employee:
    name='Paul'
    _age=30
    __salary=8000

    def show_data(self):
        print(self.name, self._age, self.__salary)


class Boss(Employee):
    def show_data(self):
        # print(self.name, self._age, self.__salary)
        print(self._Employee__salary)


#test
teacher=Teacher(9000)
teacher.set_data('Mihai', 78, 'male')
teacher.show_teacher_data()

e=Employee()
e.show_data()

b=Boss()
b.show_data()