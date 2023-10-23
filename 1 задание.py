class Car:
    fuel = 53
    brand = "lada"
    model = "kalina"
    year = "2017"
    driver = "Volodya"

def go(self):
    pass

def turn(self):
    pass

def stop(self):
    pass

def show_info(self):
    print(Car.fuel,Car.brand,Car.model,Car.year,Car.driver)
class Driver:
    name="Volodya"
    surname="Rjavuy"
    age="45"
def show_info(self):
    print(Driver.name,Driver.surname,Driver.age)

myCar = Car()
myCar.go()

myCar.show_info()

myDriver = Driver()
myDriver.show_info()