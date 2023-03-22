class Hero:
    def __init__(self, heroName, health, attackPower, defenseNumber):
        self.name = heroName
        self.health = health
        self.attack = attackPower
        self.defense = defenseNumber

    def attacking(self, enemy):
        print(self.name, "menyerang", enemy.name)
        enemy.attacked(self, self.attack)

    def attacked(self, enemy, enemyAttackPower):
        print(self.name, "diserang", enemy.name)

        attack_received = enemyAttackPower/self.defense
        print("serangan diterima :", str(attack_received))

        self.health -= attack_received
        print("darah", self.name, "tersisa :", str(self.health))

archer = Hero("archer", 100, 25, 10)
knight = Hero("knight", 120, 5, 50)

archer.attacking(knight)
print("\n")
archer.attacking(knight)
print("\n")
knight.attacking(knight)
print("\n")
knight.attacking(knight)
print("\n")
archer.attacking(knight)