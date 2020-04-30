
class BMI:
    def calculate_bmi(self):
        print('Enter you weight in KG: ')
        self.weight=float(input())
        print('Enter your height in meters: ')
        self.height=float(input())
        self.bmi=self.weight/(self.height**2)
        print('Your BMI is: ', self.bmi)
        if self.bmi<18.5:
            print('underweight')
        elif 18.5<self.bmi<24.9:
            print('normal')
        elif 24.9<self.bmi<29.9:
            print('overweight')
        elif self.bmi>30:
            print('obese')



#test
bmi=BMI()

while True:
    print('1. Calculate your BMI.')
    print('2. Exit.')

    choice=int(input())
    if choice is 1:
        bmi.calculate_bmi()
    elif choice is 2:
        exit()