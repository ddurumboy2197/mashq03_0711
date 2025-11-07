class Vehicle:
    def start(self):
        print("Vehicle ishga tushdi.")

    def stop(self):
        print("Vehicle to‘xtadi.")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car ishga tushdi.")

    def stop(self):
        super().stop()
        print("Car to‘xtadi.")

car = Car()
car.start()
car.stop()
