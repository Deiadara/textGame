# To kathe creature kalo tha itan na exei inventory ktl san person wste na exoume looting eykolo

class Creature:
    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage
        self.loot = {}
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print("Creature defeated!")

class Orc(Creature):
    def __init__(self):
        # Orc me 5 hp kai 5 dmg
        super().__init__(5, 5)

class Parrot(Creature):
    def __init__(self):
        # Parrot that repeats whatever you say
        super().__init__(1000, 1)
    
    def speak(self, message):
        print(message)