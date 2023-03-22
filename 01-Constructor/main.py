class Hero: # template
    def __init__(self, name, power): # constructor
        self.name = name
        self.power = power

hero1 = Hero("Warrior", 100)
hero2 = Hero("Archer", 150)

print(hero1.name, hero1.power)
print(hero2.name, hero2.power)
print(hero1.__dict__, hero2.__dict__)