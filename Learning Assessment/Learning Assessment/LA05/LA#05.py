class mlGame():
    def __init__(self,name, role, heroType):
        self.name = name
        self.role = role
        self.heroType = heroType
        
    def describe(self):
        return f"{self.name} is a {self.role} and {self.heroType}"
    
first_Hero = mlGame("Ling", "Assasin" , "Damage Type Hero")
second_Hero = mlGame("Brody", "Marksman", "Damage Type Hero")

print(f'''
{first_Hero.describe()}
{second_Hero.describe()}
''')
