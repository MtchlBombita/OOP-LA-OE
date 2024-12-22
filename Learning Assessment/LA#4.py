class classification():
    def __init__(self, name, bsc_atck, role):
        self.name = name 
        self.bsc_atck = bsc_atck
        self.role = role

    def __str__(self):
        return f"{self.name} is a {self.role} type hero"
    
mm1 = classification("gusion", 120, "assassin")
mm2 = classification("fanny", 240, "assassin")

print(mm1)
print(mm2)
