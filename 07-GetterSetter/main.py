class Hero:
    
    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor

    @property
    def info(self):
        return "name {} : \n\thealth: {}".format(self.name, self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print("armor di delete")
        self.__armor = None

hayabusa = Hero("hayabusa", 100, 20)

print("Merubah info")
print(hayabusa.info)
hayabusa.name = "assassin"
print(hayabusa.info)

print("getter and setter for __armor")
print(hayabusa.armor)
hayabusa.armor = 50
print(hayabusa.armor)

print("delete armor")
del hayabusa.armor
print(hayabusa.__dict__)