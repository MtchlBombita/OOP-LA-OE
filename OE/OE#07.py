class TekkenCharacter():
    def __init__(self,name,ability):
        self.name = name 
        self.ability = ability
    def Introduce(self,func):
        def open_mthd(*args, **kwargs):
            print("Introducing the Character....")
            func(*args, **kwargs)
            print("This character is amazing! ")
        return open_mthd
char = TekkenCharacter("King", "Dance King")

@char.Introduce
def Character_Intro(char_name, char_ability):
    print(f"Character name: {char_name}, Special Ability: {char_ability}")
Character_Intro("King", "Dance King")
