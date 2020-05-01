class Parent:
    def func(self):
        print('function from parent class')


class Child(Parent):
    def func(self):
        super().func()


#test
p=Parent()
p.func()

c=Child()
c.func()

c=Child
print(c)

f=c.func
print(f)