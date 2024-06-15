import npc
import creatures
class Room:
    def __init__(self, obj, ppl, crs):
        self.objects = obj
        self.people = ppl
        self.creatures = crs

class Tavern(Room):
    def __init__(self):
        bartender = npc.Bartender()
        bountyhunter = npc.BountyHunter()
        parrot = creatures.Parrot()

        obj = {}
        ppl = {'bartender' : bartender, 'bountyhunter' : bountyhunter}
        crs = {'parrot' : parrot}
        super().__init__(obj, ppl, crs)

class easy(Room):
    def __init__(self):
        obj = {}
        ppl = {}
        crs = {}
        super().__init__(obj, ppl, crs)

class medium(Room):
    def __init__(self):
        obj = {}
        ppl = {}
        crs = {}
        super().__init__(obj, ppl, crs)

class hard(Room):
    def __init__(self):
        obj = {}
        ppl = {}
        crs = {}
        super().__init__(obj, ppl, crs)