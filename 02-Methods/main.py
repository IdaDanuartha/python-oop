class Hero:
    
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    # void function (method tanpa return)
    def sayHi(self):
        print("Hai", self.name)

    # function with argument
    def powerUp(self, power):
        self.power += power

    # function with return
    def getPower(self):
        return self.power


hero1 = Hero("Miya", 100, 150)
hero2 = Hero("Balmond", 90, 200)

hero1.sayHi()
hero1.powerUp(50)
print(hero1.getPower())