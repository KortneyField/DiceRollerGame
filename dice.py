import random

class Die:
    def__init__(self, sides=2, value=0):
        if not sides >=2:
            raise ValueError("Must have at least 2 sides or more")
        if not ininstance(sides, int):
            raise ValueError("Sides must be a whole number")
        self.value = value or random.randint(1,sides)
        
