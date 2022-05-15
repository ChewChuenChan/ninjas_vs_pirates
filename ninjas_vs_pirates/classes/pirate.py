class Pirate:
    pirate_ship =[]
    pirate_count = 0

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        Pirate.pirate_ship.append(self)
        Pirate.pirate_count +=1

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        print(f"{self.name} health : {self.health} VS {ninja.name} health : {ninja.health} ")
        if check_life(ninja.health):
            print(f"{self.name} attack {ninja.name} with {self.strength}\n")
            ninja.health -= self.strength
        else:
            print(f"Game Over")
        return self

    @classmethod
    def print_all(cls):
        for pirates in cls.pirate_ship:
            pirates.show_stats()

@staticmethod
def check_life (health):
    if health < 0:
        print(f"Not enough health point, please reload")
        return False
    elif health >10:
            print(f"You are strong. Fighting!")
            return True
    else:
        print(f"You almost die, raise your health point")
        return True


class Pirate_mate(Pirate):
    def __init__(self, name,position,power):
        super().__init__(name)
        self.position = position
        self.power = power
    pass

