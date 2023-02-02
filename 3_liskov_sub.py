"""
    LISKOV SUBSTITUTION PRINCIPLE
        Definition:
        - Objects should be replaceble with their subtypes without affecting the correctness of the program
    

"""

# Sample SOLID Principle
class Vehicle:
    def getInteriorWidth(self):
        pass

class Car(Vehicle):
    def getInteriorWidth(self):
        return self.getCabinWidth()
    
    def getCabinWidth(self):
        return 10


class RacingCar(Vehicle):
    def getInteriorWidth(self):
        return self.getCockpitWidth()

    def getCockpitWidth(self):
        return 4

first = Car()
second = Car()
third = RacingCar()

myVehicles = []

myVehicles.append(first)
myVehicles.append(second)
myVehicles.append(third)

# for i in range(len(myVehicles)):
#     print(myVehicles[i].getInteriorWidth())

################################################################################
# Sample 2 pt.1: NOT A SOLID PRINCIPLE
################################################################################
class Product:
    def __init__(self) -> None:
        self.discount = 4
    
    def getDiscount(self):
        return self.discount
    
class InHouseProduct(Product):
    def applyExtraDiscount(self):
        self.discount = self.discount * 1.5
    
p1 = Product()
p2 = Product()
p3 = InHouseProduct()

myProductsList = []
myProductsList.append(p1)
myProductsList.append(p2)
myProductsList.append(p3)


# NOT a SOLID Principle!!! 
for i in range(len(myProductsList)):
    if type(myProductsList[i]) == InHouseProduct:
        myProductsList[i].applyExtraDiscount()
    print(myProductsList[i].getDiscount())
print("\nEND\n")
################################################################################
# Sample 2 pt.2: SOLID PRINCIPLE
################################################################################

class Product:
    def __init__(self) -> None:
        self.discount = 20
    
    def getDiscount(self):
        return self.discount

class InHouseProduct(Product):
    def getDiscount(self):
        self.applyExtraDiscount()
        return self.discount
    
    def applyExtraDiscount(self):
        self.discount = self.discount * 1.5

p1 = Product()
p2 = Product()
p3 = InHouseProduct()

myProductsList = []
myProductsList.append(p1)
myProductsList.append(p2)
myProductsList.append(p3)

for i in range(len(myProductsList)):
    print(myProductsList[i].getDiscount())
