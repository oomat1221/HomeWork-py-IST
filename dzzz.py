
class Car:
    def __init__(self, mark, engine_volume, mileage=0):
        self.mark = mark
        self.engine_volume = engine_volume
        self.mileage = mileage

    def fuel_consumption(self):
        if self.engine_volume <= 1.8:
            return f"{self.mark} - малый расход"
        elif self.engine_volume < 3.0:      
            return f"{self.mark} - средний расход"
        else:                               
            return f"{self.mark} - большой расход"

    def drive(self, distance):
        self.mileage += distance
        print(f"Машина {self.mark} проехала {distance} км. "
              f"Текущий пробег: {self.mileage} км.")

    def __str__(self):
        return (f"Машина {self.mark}, объем двигателя: {self.engine_volume} л, "
                f"пробег: {self.mileage} км")


class Smartphone:
    def __init__(self, brand, model, battery_level=100):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level

    def play_game(self, hours):
        self.battery_level -= 15 * hours
        if self.battery_level <= 0:
            self.battery_level = 0
            print("Телефон разряжен!")
        else:
            print(f"Вы играли {hours} ч. Заряд батареи: {self.battery_level}%")

    def charge(self):
        self.battery_level = 100
        print("Телефон полностью заряжен!")


class Driver:
    def __init__(self, name, car):
        self.name = name
        self.car = car

    def start_trip(self, km):
        print(f"Водитель {self.name} заводит {self.car.mark} и отправляется в путь!")
        self.car.drive(km)


# Проверка
car = Car("Toyota", 2.5)
print(car.fuel_consumption())   
print(Car("Honda", 2.0).fuel_consumption())  

car.drive(100)
print(car)

phone = Smartphone("Samsung", "S23")
phone.play_game(2)   
phone.play_game(5)  
phone.charge()

driver = Driver("Иван", car)
driver.start_trip(50)  