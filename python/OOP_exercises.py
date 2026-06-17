class Vehicle():
    def on_start(self):
        return 'Power on'

class Tesla(Vehicle):
    def drive(self):
        print(f'Cyber Truck {self.on_start()}')
        return 'Ready to go, Fasten your seatbelts'
    
my_car = Tesla()

print(my_car.drive())

class Employee():
    def __init__(self, name, id, department, monthly_salary, birth_year):
        self.name = name
        self.id = id 
        self.department = department
        self.monthly_salary = monthly_salary
        self.birth_year = birth_year

    def A_salary(self):
        return self.monthly_salary * 12
    
    def R_year(self):
        return self.birth_year + 60
        

cal = Employee('Joy', 204, 'Hr', 20000, 2005)

print(f'Yearly salary = {cal.A_salary()}')
print(f'Retirement Year = {cal.R_year()}')