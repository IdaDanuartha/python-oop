class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    def regenHealth(self):
        self.__health += 5

hanabi = Hero("hanabi", 100)
print(hanabi.getName())
print("darah", hanabi.getName(), "=", hanabi.getHealth())
hanabi.regenHealth()
hanabi.regenHealth()
print("darah", hanabi.getName(), "setelah regen =", hanabi.getHealth())