class Car():
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"My car brand is: {self.brand}"
    
car = Car("Lamborghini")
print(car)
del car
print(car)
