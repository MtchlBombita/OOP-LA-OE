print("LA:13")
class Animal():
    def __init__(self, name, type):
        self.name = name
        self.type = type 
class Fish(Animal):
    def __init__(self, name,type, can_swim):
        super().__init__(name, type)
        self.can_swim = True
    def describeFish(self):
        return f"The name of the fish is {self.name} and a {self.type} and it can swim? {self.can_swim}"
fish1 = Fish("Justin", "Kraken", True)

class Bear(Animal):
    def __init__(self, name, type, can_swim):
        super().__init__(name, type)
        self.can_swim = False
    def describeBear(self):
        return f"The name of this animal is {self.name} and a {self.type} and it can swim? {self.can_swim}"
bear1 = Bear("Webearbear", "Grizzly", False)

print(fish1.describeFish())
print(bear1.describeBear())
