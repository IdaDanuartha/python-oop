class Hero: # template
    # class variable
    jumlah = 0
    def __init__(self, name, power): # constructor
        self.name = name
        self.power = power
        Hero.jumlah += 1

hero1 = Hero("Warrior", 100)
print(hero1.name, hero1.power)
print(Hero.jumlah)

hero2 = Hero("Archer", 150)
print(hero2.name, hero2.power)
print(Hero.jumlah)

print(hero1.__dict__, hero2.__dict__)
