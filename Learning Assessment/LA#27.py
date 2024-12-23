
from abc import ABC, abstractmethod

class NinjaTurtles(ABC):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias

    @abstractmethod
    def Intro(self):
        pass

class Leonardo(NinjaTurtles):
    def __init__(self, real_name, alias):
        super().__init__(real_name, alias)

    def Intro(self):
        print(f"My name is {self.real_name} and my alias is {self._NinjaTurtles__alias}")

class MichaelAngelo(NinjaTurtles):
    def __init__(self, real_name, alias):
        super().__init__(real_name, alias)

    def Intro(self):
        print(f"My name is {self.real_name} and my alias is {self._NinjaTurtles__alias}")

class Donatello(NinjaTurtles):
    def __init__(self, real_name, alias):
        super().__init__(real_name, alias)

    def Intro(self):
        print(f"My name is {self.real_name} and my alias is {self._NinjaTurtles__alias}")

class Raphael(NinjaTurtles):
    def __init__(self, real_name, alias):
        super().__init__(real_name, alias)

    def Intro(self):
        print(f"My name is {self.real_name} and my alias is {self._NinjaTurtles__alias}")

ninja1 = Leonardo("Leonardo", "Pagong 1")
ninja2 = MichaelAngelo("MichaelAngelo", "Pagong 2")
ninja3 = Donatello("Donatello", "Pagong 3")
ninja4 = Raphael("Raphael", "Pagong 4")

for x in (ninja1, ninja2, ninja3, ninja4):
    x.Intro()  
