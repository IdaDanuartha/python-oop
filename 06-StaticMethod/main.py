class Hero:
    __health = 0

    def __init__(self, name, health):
        self.__name = name
        self.__health = health
        Hero.__health += 1

    # method ini hanya berlaku untuk objek
    def getHealth1(self):
        return self.__health

    # method ini tidak berlaku untuk objek tapi belaku untuk class
    def getHealth2():
        return Hero.__health

    # method static (decorator) nempel ke objek dan class
    @staticmethod
    def getHealth3():
        return Hero.__health

    # method static (decorator) nempel ke objek dan class, tetapi lewat argument
    @classmethod
    def getHealth4(this):
        return this.__health

hayabusa = Hero("hayabusa", 100)

print(hayabusa.getHealth1())
print(Hero.getHealth2())

print(hayabusa.getHealth3())
print(Hero.getHealth3())

print(hayabusa.getHealth4())
print(Hero.getHealth4())