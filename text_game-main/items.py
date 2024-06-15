class Item:
    def __init__(self, name, place):
        self.name = name
        self.equip_place = place

class Sword(Item):
    def __init__(self, name, damage):
        super().__init__(name, 'right_arm')
        self.damage = damage

class Helmet(Item):
    def __init__(self, name, armor):
        super().__init__(name, 'head')
        self.armor = armor

class Armor(Item):
    def __init__(self, name, armor):
        super().__init__(name, 'chest')
        self.armor = armor

class Pants(Item):
    def __init__(self, name, armor):
        super().__init__(name, 'legs')
        self.armor = armor

class Shoes(Item):
    def __init__(self, name, armor):
        super().__init__(name, 'feet')
        self.armor = armor

