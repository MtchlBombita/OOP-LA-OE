print("LA:23")

class AnimeCharacter():
    def __init__(self, name, ability):
        self.__name = name
        self.ability = ability
    def introduce(self, func):
        def open_mthd(*args, **kwargs):
            print("Introducing...")
            func(*args, **kwargs)
            return open_mthd

char1 = AnimeCharacter("Sung Jinwoo", "Arise")

@char1.introduce
def character_intro(char_name,char_ability):
    print(f"I am {char_name} and i can use {char_ability}")
character_intro("Sung Jinwoo", "Arise")
