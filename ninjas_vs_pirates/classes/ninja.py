from xml.sax import parseString


class Ninja:
    ninja_school = []
    ninja_count = 0
    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        Ninja.ninja_school.append(self)
        Ninja.ninja_count += 1
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        print(f"{self.name} health : {self.health} VS {pirate.name} health : {pirate.health} ")
        if check_life(pirate.health):
            print(f"{self.name} attack {pirate.name} with {self.strength}\n")
            pirate.health -= self.strength
        else:
            print(f"Game Over")
        return self

    @classmethod
    def print_all(cls):
        for pirates in cls.ninja_school:
            pirates.show_stats()

@staticmethod
def check_life (health):
    if health < 0:
        print(f"Not enough health point, please reload")
        return False
    elif health >10:
            print(f"You are strong. Fighting! ")
            return True
    else:
        print(f"You almost die, please reload")
        return True

class Ninja_mate(Ninja):
    def __init__(self, name,position,power):
        super().__init__(name)
        self.position = position
        self.power = power
    pass


