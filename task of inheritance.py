# 1:
class Vehicle:
    def __init__(self, name, model, weight, year):
        self.name = name
        self.model = model
        self.weight = weight
        self.year = year

    def start_engine(self):
        print("The vehicle's engine is starting...")

class Car(Vehicle):
    def __init__(self, name, model, weight, year, num_doors, num_passengers):
        super().__init__(name, model, weight, year)
        self.num_doors = num_doors
        self.num_passengers = num_passengers

    def start_engine(self):
        return "The car's engine is starting..."

    def drive(self):
        return "The car is being driven..."


a = Vehicle('mustang', 'ford', 2528, 858)
print(a.start_engine())

car = Car('mustang', 'ford', 2528, 858, 4, 5)
print(car.start_engine())
print(car.drive())

# 2:

class Truck(Vehicle):
    def __init__(self, name, model, weight, year, cargo_capacity, towing_capacity):
        super().__init__(name, model, weight, year)
        self.cargo_capacity = cargo_capacity
        self.towing_capacity = towing_capacity

    def start_engine(self):
        return "The truck's engine is starting..."

    def haul(self):
        print(f"Фірма {self.name}, Модель {self.model}, Вага {self.weight}, Рік {self.year}")

truck = Truck ('Toyota', 'Supra', '1621 kg', '1978')
print(truck.start_engine())

# 3:

class Motorcycle(Vehicle):
    def __init__(self, name, model, weight, year, num_wheels, has_sidecar):
        super().__init__(name, model, weight, year)
        self.num_wheels = num_wheels
        self.has_sidecar = has_sidecar

    def start_engine(self):
        return "The motorcycle's engine is starting..."

    def ride(self):
        print(f"Фірма {self.name}, Модель {self.model}, Вага {self.weight}, Рік {self.year}", \
              f"Кількість колес {self.num_wheels}, Має коляску {self.has_sidecar}")


motorcycle = Motorcycle('Yamaha', 'R1', '200 kg', 2021, 'two wheels', 'no sidecar')

print(motorcycle.start_engine())
motorcycle.ride()

print(car.start_engine())
print(truck.start_engine())
print(motorcycle.start_engine())
print(a.start_engine())
