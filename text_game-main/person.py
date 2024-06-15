import termcolor as co
class Person:
    def __init__(self, name):
        self.name = name
        self.hitpoints = 10
        self.inventory = {}
        self.apparel = {'head' : None,
                        'chest' : None,
                        'left_arm' : None,
                        'right_arm' : None,
                        'legs' : None,
                        'feet' : None}
        self.strength = 1
        self.luck = 0
        self.agility = 0
        self.gold = 0
        self.background = None

    def pickup(self, item):
        self.inventory[item.name] = item

    def equip(self, item):
        self.apparel[item.equip_place] = item

    def take_damage(self, damage):
        self.hitpoints -= damage
        if self.hitpoints <= 0:
            print(co.colored("You are dead!", color="red"))
            quit()

    def print_inventory(self):
        print(co.colored("Your Inventory: ", color="yellow"))
        for el in self.inventory.keys():
            print(co.colored(f'\t{el}', color="yellow"))

    def print_apparel(self):
        print(co.colored("Your Apparel: ", color="light_yellow"))
        print(co.colored(f"Head: {self.apparel['head']}", color="light_yellow"))
        print(co.colored(f"Left arm: {self.apparel['left_arm']}", color="light_yellow"))
        print(co.colored(f"Right arm: {self.apparel['right_arm']}", color="light_yellow"))
        print(co.colored(f"Legs: {self.apparel['legs']}", color="light_yellow"))
        print(co.colored(f"Feet: {self.apparel['feet']}", color="light_yellow"))

    def give_gold(self, amount):
        if amount > self.gold:
            return False
        else:
            self.gold -= amount
            return True
        
    def get_gold(self, amount):
        self.gold += amount
    
    def print_gold(self):
        print(co.colored(f"Your Gold: {self.gold}", color="light_cyan"))

    

