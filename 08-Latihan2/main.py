class Hero:
    __jumlah = 0

    def __init__(this, name, health, attPower, armor):
        this.__name = name
        this.__healthStandar = health
        this.__attPowerStandar = attPower
        this.__armorStandar = armor

        this.__level = 1
        this.__exp = 0

        this.__healthMax = this.__healthStandar * this.__level
        this.__attPower = this.__attPowerStandar * this.__level
        this.__armor = this.__armorStandar * this.__level

        this.__health = this.__healthMax

        Hero.__jumlah += 1

    @property
    def info(this):
        return "{} level {}: \n\thealth: {}/{}\n\tattPower: {}\n\tarmor: {}".format(this.__name, this.__level, this.__health, this.__healthMax, this.__attPower, this.__armor)

    @property
    def gainExp(this):
        pass

    @gainExp.setter
    def gainExp(this, newExp):
        this.__exp += newExp

        if this.__exp >= 100:
            print(this.__name, " level up")
            this.__level += 1
            this.__exp -= 100

            this.__healthMax = this.__healthStandar * this.__level
            this.__attPower = this.__attPowerStandar * this.__level
            this.__armor = this.__armorStandar * this.__level

    def attacking(this, enemy):
        this.gainExp = 50
        print(this.__name, "menyerang", enemy.__name)
        this.attacked(enemy)

    def attacked(this, enemy):
        enemy.__health -= this.__attPower/enemy.__armor
        print(enemy.__name, "diserang", this.__name)

archer = Hero("archer", 100, 50, 5)
knight = Hero("knight", 150, 15, 20)
print(archer.info)
archer.attacking(knight)
archer.attacking(knight)
print(archer.info)
print(knight.info)