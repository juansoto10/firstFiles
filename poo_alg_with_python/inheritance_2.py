# Creating the super class Warrior:

class Warrior:

    def __init__(self, name, power, speed, health, agility):
        self.name = name
        self.power = power
        self.speed = speed
        self.health = health
        self.agility = agility

    def move(self):
        f'{self.name} just moved 5 m at a speed of {self.speed} Warrior Units (WU)'

    def attack(self):
        return f'{self.name} just performed an attack with a power of {float(self.power * 0.25)} Attack Units (AU)'

    def elude(self):
        return f'{self.name} just eluded the enemy with a {self.agility} agility and a speed of {float(self.speed * 1.2)} Warrior Units (WU)'

# Creating LandWarrior (Warrior sub-class)

class LandWarrior(Warrior):

    def __init__(self, name, power, speed, health, agility):
        super().__init__(name, power, speed, health, agility)

    def super_attack(self):
        return f'{self.name} just performed a super-attack with a power of {float(1.4 * self.power * 0.25)} Attack Units (AU)'

# Creating Amazona (LandWarrior sub-class)

class Amazona(LandWarrior):

    def __init__(self, name, power, speed, health, agility):
        super().__init__(name, power, speed, health, agility)

    def glorious_attack(self):
        return f'{self.name} just performed a glorious-attack with a power of {float(1.7 * self.power * 0.25)} Attack Units (AU)'


def main():
    
    # Instantiating 1 Amazona:

    amazona_1 = Amazona('Sahian', 40, 60, 115, 'decent')

    # Let's call some functions:

    print(amazona_1.elude()) # A function defined in the super class Warrior
    print(amazona_1.super_attack()) # A function defined in the sub class LandWarrior
    print(amazona_1.glorious_attack()) # A function defined in the sub class Amazona

    # --> Sahian just eluded the enemy with a decent agility and a speed of 72.0 Warrior Units (WU)
    # --> Sahian just performed a super-attack with a power of 14.0 Attack Units (AU)
    # --> Sahian just performed a glorious-attack with a power of 17.0 Attack Units (AU)


if __name__ == '__main__':
    main()