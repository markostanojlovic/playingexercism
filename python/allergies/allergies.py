from enum import Enum


class AllergiesPool(Enum):
    eggs = 1
    peanuts = 2 
    shellfish = 4
    strawberries = 8
    tomatoes = 16
    chocolate = 32 
    pollen = 64
    cats = 128


class Allergies(object):

    def __init__(self, score):
        self.allergies = [ i.name for i in AllergiesPool if score & i.value == i.value ]

    def is_allergic_to(self, item):
        return item.lower() in self.allergies

    @property
    def lst(self):
        return list(self.allergies)
        
