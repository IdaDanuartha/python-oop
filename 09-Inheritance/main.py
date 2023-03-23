class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class HeroStrength(Hero):
    pass

class HeroIntelligence(Hero):
    pass

archer = Hero("archer", 100)
knight = HeroStrength("knight", 100)
assassin = HeroIntelligence("assassin", 100)

print(archer.__dict__)
print(knight.__dict__)
print(assassin.__dict__)