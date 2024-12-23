class FavoriteFood:
    def __init__(self, dish, firstingre, secondingre, thirdingre, fourthingre):
        self.dish = dish 
        self.__firstingre = firstingre
        self._secondingre = secondingre
        self.__thirdingre = thirdingre
        self.__fourthingre = fourthingre
    
    def __str__(self):
        return f"My favorite dish is {self.dish} and the ingredients are:\n1. {self.__firstingre} \n2. {self._secondingre} \n3. {self.__thirdingre} \n4. {self.__fourthingre}"
    
    def may_baboy(self, age):
        self.age = age
        if age >= 15:
            return "Norem"
        else:
            return "Alaws"

    def updatebaboy(self, new, meronkaba):
        if meronkaba == "oo":
            self.__firstingre = new
            return "Success"
        else: 
            return "Failed"

favorite1 = FavoriteFood("Pork Adobo", "Baboy", "Sibuyas", "Pineapple Tidbits", "Toyo")
favorite2 = FavoriteFood("Adobong Manok", "45 days na Manok", "Sibuyas", "Paminta", "Laurel")
favorite3 = FavoriteFood("Adobo sa Gata", "Gata", "Sibuyas", "Toyo", "Panabong na Manok")


print(favorite1.may_baboy(16)) 
print(favorite1.updatebaboy("Isang Kilong Baboy", "oo")) 
print(favorite1)
