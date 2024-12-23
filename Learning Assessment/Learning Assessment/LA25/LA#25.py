print("lA:25")

from abc import ABC, abstractmethod

class Character(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

class Batman(Character):
    def __init__(self, rname, alias):
        self.rname = rname
        self.__alias = alias
    @property
    def name(self):
        return self.__alias
    
char1 = Batman("Bruce Wayne", "Batman")
print(char1.name)
