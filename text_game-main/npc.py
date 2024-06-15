import termcolor as co
class NPC:
    def __init__(self, name, dialogs):
        self.name = name
        self.dialogues = dialogs
        self.relationship = 0
    
    def add_relationship(self, amount):
        self.relationship += amount
        if self.relationship < 0:
            self.relationship = 0

class Bartender(NPC):
    def __init__(self):
        name = "Oliver"
        dialogs = {'Greeting' : self.greeting,
                   'Question' : self.place,
                   'Line1' : self.line1}
        super().__init__(name, dialogs)
    
    def greeting(self):
        print(co.colored("""
Welcome traveler! What name do you go by?""", color='light_yellow'))

    def place(self, name):
        print(co.colored(f"""
Where do you come from {name}? You don't look like you're from around here.""", color='light_yellow'))

    def line1(self):
        print(co.colored("""
Let's just say Herta's people have a certain look -- and smell -- that gives them away!""", color='light_yellow'))

class BountyHunter(NPC):
    def __init__(self):
        name = "John Wick"
        dialogs = {'Greeting' : "EAGHD?",
                   'Question' : "Fuck off!"}
        super().__init__(name, dialogs)