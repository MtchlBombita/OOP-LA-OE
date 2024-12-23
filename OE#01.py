class MyTeam():
    def __init__(self,name, role,lane,dmg_type):
        self.name = name 
        self.role = role 
        self.lane = lane 
        self.dmg_type = dmg_type

    def __str__(self):
        return f"Hero Name: {self.name}, role {self.role} and her/his lane {self.lane} and a {self.dmg_type}"
    
hero1 = MyTeam("Fanny", "Assassin", "Jungle", "Damage Type")
hero2 = MyTeam("Cecilion", "Mage", "Mid Lane", "Magic Type")
hero3 = MyTeam("Yu Zhong", "Fighter", "Exp Lane", "Damage Type")
hero4 = MyTeam("Beatrix", "Marksman", "Gold Lane", "Damage Type")
hero5 = MyTeam("Hylos", "Tank", "Roamer", "Defense")

print(f'''{hero1.name} 
{hero1.role}
{hero1.lane}
{hero1.dmg_type}
{hero1}

{hero2.name}
{hero2.role}
{hero2.lane}
{hero2.dmg_type}
{hero2}  

{hero3.name}
{hero3.role}
{hero3.lane}
{hero3.dmg_type}
{hero3}

{hero4.name}
{hero4.role}
{hero4.lane}
{hero4.dmg_type}
{hero4}

{hero5.name}
{hero5.role}
{hero5.lane}
{hero5.dmg_type}
{hero5}
''')
