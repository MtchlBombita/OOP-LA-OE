from abc import ABC, abstractmethod

class NinjaTurtles(ABC):
    def __init__(self, real_name, __alias):
       self.real_name = real_name
    @property
    @abstractmethod
    def __init__(self, real_name):
        pass

class Leonardo (NinjaTurtles):
     def __init__(self, real_name, __alias):
        self.real_name = real_name 
        self.__alias = __alias
     @property
     def alias(self):
        return self.__alias

class MichaelAngelo (NinjaTurtles):
     def __init__(self, real_name, __alias):
        self.real_name = real_name 
        self.__alias = __alias
     @property
     def alias(self):
        return self.__alias     

class Donatello (NinjaTurtles):
     def __init__(self, real_name, __alias):
        self.real_name = real_name 
        self.__alias = __alias
     @property
     def alias(self):
        return self.__alias

class Raphael (NinjaTurtles):
     def __init__(self, real_name, __alias):
        self.real_name = real_name 
        self.__alias = __alias
     @property
     def alias(self):
        return self.__alias

if _name_ == "_main_":
    epo = Leonardo ("Leonardo", "NiwNiw")
    epo1 = MichaelAngelo ("MichaelAngelo", "NitNit")
    epo2 = Donatello ("Donatello", "MitchiBoy")
    epo3 = Raphael ("Raphael", "Labo")
    print(epo.alias)
    print(epo1.alias)
    print(epo2.alias)
    print(epo3.alias)
