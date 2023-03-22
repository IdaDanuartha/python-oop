class Hero:
    # private variable
    __jumlah = 0

    # protected variable
    _weapon = "Katana"

    def __init__(self, name, health):
        self.name = name
        self.health = health

        self.__attackPower = "private"
        self._defense = "protected"

lili = Hero("lili", 100)
print(Hero.__dict__)
print(lili.__dict__)

print("\n")

# print(Hero.__jumlah)
print(Hero._weapon)

# print(lili.__attackPower)
print(lili._defense)