class classification():
    def __init__(self, name, bsc_atck, role):
        self.name = name 
        self.bsc_atck = bsc_atck
        self.role = role

    def describe(self):
        return f"{self.name} is a {self.role} type hero"
    
mm1 = classification("gusion", 120, "assassin")
mm2 = classification("fanny", 240, "assassin")

print(mm1.name)
print(mm1.bsc_atck)
print(mm1.describe())
print(mm2.name)
print(mm2.bsc_atck)
print(mm1.describe())
