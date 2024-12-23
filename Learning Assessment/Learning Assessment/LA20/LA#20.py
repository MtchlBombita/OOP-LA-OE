print("LA:20")

class Favoritefood():
    def __init__(self,dish, firstingre, secondingre, thirdingre, fourthingre):
        self.dish = dish
        self.firstingre = firstingre
        self.secondingre = secondingre
        self.thirdingre = thirdingre
        self.fourthingre  = fourthingre
    
    def __str__(self):
        return f"My Favorite dish is {self.dish} and the ingredients is\n1. {self.firstingre} \n2. {self.secondingre} \n3. {self.thirdingre} \n4. {self.fourthingre}"
    
    def may_baboy(self, age):
        self.age = age 
        if age >= 15:
            return f"Meron"
        else:
            return f"alaws"
favorite1 = Favoritefood("Munggo", "Kamatis", "sibuyas", "chicharon", "baboy")
favorite2 = Favoritefood("Pork Giniling", "giniling", "sibuyas", "patatas", "toyo")
favorite3 = Favoritefood("Adobo sa gata", "45 days na manok", "sibuyas", "Luya", "Gata")

print(f'''{favorite1}
{favorite2}
{favorite3}''')
print(favorite1.may_baboy(16))
