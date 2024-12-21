
class classification():
    def __init__(self, name, bsc_atck, role):
        self.name = name 
        self.bsc_atck = bsc_atck
        self.role = role

mm1 = classification("gusion", 120, "assassin")
mm2 = classification("fanny", 240, "assassin")

print(mm1.name)
print(mm1.bsc_atck)
print(mm1.role)
print(mm2.name)
print(mm2.bsc_atck)
print(mm2.role)
