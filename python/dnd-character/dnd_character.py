import random

def modifier(n):
    return (n - 10)//2

class Character:
    def __init__(self):
        self.abilities = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
        for ability in self.abilities:
            trow = [random.randint(1,6) for i in range(4)]
            trow.sort()
            setattr(self, ability, sum(trow[:3]))
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return getattr(self, random.sample(self.abilities,1)[0])
