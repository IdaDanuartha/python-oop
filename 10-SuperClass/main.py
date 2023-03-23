class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print(self.name, "dengan health : ", self.health)

class HeroStrength(Hero):
    def __init__(self, name):
        # Hero.__init__(self, name, 200)
        super().__init__(name, 200)
        super().showInfo()

class HeroIntelligence(Hero):
    def __init__(self, name):
        super().__init__(name, 120)
        super().showInfo()

knight = HeroStrength("knight")
assassin = HeroIntelligence("assassin")