class avto:
    def __init__(self, brand, model, price, color):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.moshina = 0
    
    def info(self):
        return f"{self.brand} {self.model} - {self.price} $, rangi {self.color} avto soni >>>{self.moshina}"

    def update_moshina(self):
        self.moshina += 1

car1 = avto("BMW", "X7", 140_000, "RED")
car2 = avto("RANGEROVER", "DEFENDER", 300_000, "BLUE")
car3 = avto("PORSCHE", "911", 240_000, "GREEN")

car1.update_moshina()
car1.update_moshina()
car2.update_moshina()
car3.update_moshina()
car3.update_moshina()
car3.update_moshina()
print(car1.info())
print(car2.info())
# print(car3.info())




class azam_motors:
    def __init__(self, brand, model):
    #     self.brand = brand
    #     self.model = model
    #     self.cars = []
    #     self.cars_soni = 0

    # def add_car(self, car):
    #     self.cars.append(car)
        self.cars_soni += 1
    
    def info_carr(self):
        return [avto.info() for avto in self.cars]


zzzz = avto("aza_motor")
aaaa = avto("aaa_salon")

car1 = avto("BMW", "x7", 140_000,"yellow")
car2 = avto("mers", "w223", 190_000,"white")














