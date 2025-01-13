
from random import choice

class weapon:
    def __init__(self, nomi, type):
        self.nomi = nomi
        self.type = type
        if self.type.lower() == 'avtomat':
            self.__soni = 30
        elif self.type.lower() == 'pistik':
            self.__soni = 9

    def otish(self):
        self.__soni -= 1
        if self.__soni == 0:
            self.oqlash()
    
    def oqlash(self):
        if self.type.lower() == 'avtomat':
            self.__soni = 30
        elif self.type.lower() == 'pistik':
            self.__soni = 9

class player:
    def __init__(self, nick, weapon: weapon):
        self.__health = 100
        self.wp = weapon
        self.nick = nick
    
    def oqlash_weaponni(self):
        self.wp.oqlash()
    
    def get_health(self):
        return f"{self.nick} -> {self.__health}"

    def set_health(self, obj):
        dct = {'bosh': 100,'yurak': 99, 'gavda': 75, "qo'l": 25,'qorin':40}
        qayerga = choice([i for i in dct.keys()])
        obj.__health -= dct[qayerga]
        print(f"{self.nick} -> {obj.nick} ning {qayerga} otdi.")
        if obj.__health <= 0:
            print(f"{obj.nick} is Dead by {self.nick}")
            exit()
    
    def otish_weaponni(self, obj):
        self.wp.otish()
        self.set_health(obj)



if __name__ == "__main__":
    w1 = weapon("Deagle", "pistik")
    w2 = weapon("AK-47", "avtomat")
    

    p1 = player("shoxaa", w2)
    p2 = player("Azza107", w1)

    while True:
        p1.otish_weaponni(p2)
        print(p2.get_health())
        p2.otish_weaponni(p1)
        print(p1.get_health())
