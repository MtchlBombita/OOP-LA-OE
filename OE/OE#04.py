class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        target.health -= self.power
        print(f"{self.name} attacks {target.name}!, {self.name} deals {self.power} damage, "
              f"{target.name} now has only {target.health} health.")

    def special_move(self):
        pass

    def defend(self, attacker):
        dmg_taken = attacker.power * 0.9
        self.health -= dmg_taken
        print(f"{self.name} defends against {attacker.name}'s attack. {self.name}'s health is now {self.health}.")

class Warrior(Character):
    def special_move(self, target):
        self.power *= 2
        print(f"{self.name} uses Shield Bash!")

class Mage(Character):
    def special_move(self, target):
        target.health -= 100
        print(f"{self.name} casts Fireball! {target.name}'s health is reduced by 100.")

class Archer(Character):
    def special_move(self, target):
        target.health -= self.power * 1.5
        print(f"{self.name} shoots a Piercing Arrow! {target.name}'s health is reduced by 1.5 times "
              f"than the normal damage.")

class Monster(Character):
    def special_move(self, target):
        target.health += 50
        print(f"{self.name} roars and gains 50 health.")

niwniw = Warrior("niwniw", 200, 10)
nitnit = Mage("nitnit", 100, 20)
juljul = Archer("juljul", 50, 15)
kuya_kort = Monster("Monster", 150, 20)

characters = [niwniw,nitnit, juljul]

while True:
    for character in characters:
        character.attack(kuya_kort)
        character.special_move(kuya_kort)
        kuya_kort.defend(character)
        if kuya_kort.health <= 0:
            print("Monster defeated!")
            break

    if kuya_kort.health <= 0:
        break

    for character in characters[:]:
        kuya_kort.attack(character)
        kuya_kort.special_move(character)
        character.defend(kuya_kort)
        if character.health <= 0:
            print(f"{character.name} is defeated!")
            characters.remove(character)
            break

    if not characters:
        print("Monster wins!")
        break
