# class Player:
#     def __init__(self, nomi, puli = 50):
#         self.nomi = nomi 
#         self.puli = puli
#         self.investory = []

#     def xarid_qilish(self, mahsulot, narx):
#         if self.puli >= narx:
#             self.puli -= narx
#             self.investory.append(mahsulot)
#             print(f"{self.nomi}, siz {mahsulot} sotib oldingiz!")
#         else:
#             print(f"{self.nomi}Pulingiz yetarli emas!")
    
#     def invesrarni_korish(self):
#         if self.investory:
#             print(f"{self.nomi}ning investlari: {', '.join(self.investory)}")
        
#         else:
#             print(f"{self.nomi} ning inventari bosh.")


# magazindagi_mahsulotlar = {
#     "olma": 10,
#     "mandarin": 7,
#     "non": 5,
#     "suv": 3,
#     "shokolad": 12
# }

# player = Player("azaa")

# print("\nmagazingadagi mahsulotlar:")
# for mahsulot, narx in magazindagi_mahsulotlar.items():
#     print(f"{mahsulot} - {narx} som")

# player.xarid_qilish("Olma",  magazindagi_mahsulotlar["olma"])
# player.xarid_qilish("Shokolad",  magazindagi_mahsulotlar["shokolad"])
# player.xarid_qilish("mandarin", magazindagi_mahsulotlar["mandarin"])

# player.invesrarni_korish()

















# from random import choice

# class weapon:
#     def __init__(self, nomi, type):
#         self.nomi = nomi
#         self.type = type
#         if self.type.lower() == ''







# import random

# class Jangchi:
#     def __init__(self, nomi, sogliq, quvvat, himoya, stamina):
#         self.nomi = nomi
#         self.sogliq = sogliq
#         self.quvvat = quvvat
#         self.himoya = himoya
#         self.stamina = stamina
    
#     def hujum(self, raqib):
#         if self.stamina > 0:
#             zarar = random.randint(5, self.quvvat)
#             if raqib.himoya_qilish():
#                 zarar = int(zarar * 0.5)  # Himoya qilganda zarar kamayadi
#             raqib.zarar_qabul_qilish(zarar)
#             self.stamina -= 5  # Har bir hujumda staminani sarflaydi
#             print(f"{self.nomi} hujum qildi! {raqib.nomi} ga {zarar} zarar yetdi.")
#         else:
#             print(f"{self.nomi}ning stamina'i yetarli emas!")

    # def himoya_qilish(self):
    #     return random.choice([True, False])

#     def zarar_qabul_qilish(self, zarar):
#         self.sogliq -= zarar
#         if self.sogliq < 0:
#             self.sogliq = 0
    
#     def dam_olish(self):
#         if self.stamina < 100:
#             self.stamina += 10  # Har bir dam olishda staminani qaytaradi
#             print(f"{self.nomi} dam olib, staminani tikladi.")
#         else:
#             print(f"{self.nomi}ning staminasi to‘liq.")

#     def tirikmi(self):
#         return self.sogliq > 0

#     def statusini_korsatish(self):
#         return f"{self.nomi}: Sog'liq = {self.sogliq}, Stamina = {self.stamina}"

# def jang(jangchi1, jangchi2):
#     round = 1
#     while jangchi1.tirikmi() and jangchi2.tirikmi():
#         print(f"\nRound {round}:")
        
#         # Figherlar hujum qilmoqda
#         jangchi1.hujum(jangchi2)
#         jangchi2.hujum(jangchi1)
        
#         # Jangchilarning statusini ko'rsatish
#         print(jangchi1.statusini_korsatish())
#         print(jangchi2.statusini_korsatish())

#         # Dam olish va staminani tiklash har 3-raundda
#         if round % 3 == 0:
#             jangchi1.dam_olish()
#             jangchi2.dam_olish()

#         round += 1

#     # Jangchi yutganini aniqlash
#     if jangchi1.tirikmi():
#         print(f"\n{jangchi1.nomi} yutdi!")
#     else:
#         print(f"\n{jangchi2.nomi} yutdi!")

# if __name__ == "__main__":
#     # Jangchilarni yaratish
#     jangchi1 = Jangchi(nomi="Azam", sogliq=100, quvvat=20, himoya=15, stamina=100)
#     jangchi2 = Jangchi(nomi="107", sogliq=100, quvvat=18, himoya=17, stamina=100)
    
#     # Jangni boshlash
#     jang(jangchi1, jangchi2)













import random

class Jangchi:
    def __init__(self, nomi, sogliq, quvvat, himoya, stamina):
        self.nomi = nomi
        self.sogliq = sogliq
        self.quvvat = quvvat
        self.himoya = himoya
        self.stamina = stamina

    def hujum(self, raqib):
        if self.stamina > 0:
            zarar = random.randint(5, self.quvvat)
            if raqib.himoya_qilish():
                zarar = int(zarar * 0.5)
            raqib.zarar_qabul_qilish(zarar)
            self.stamina -= 5 
            print(f"{self.nomi} hujum qildi! {raqib.nomi} ga {zarar} zarar yetdi.")

        else:
            print(f"{self.nomi}ning stamini yetarli emas!")

    def himoya_qilish(self):
        return random.choice([True, False])

    def zarar_qabul_qilish(self, zarar):
        self.sogliq -= zarar
        if self.sogliq < 0:
            self.sogliq = 0
    
    def dam_olish(self):
        if self.stamina < 100:
            self.stamina += 10
            print(f"{self.nomi} dam olib, staminani egib oldi.")
        
        else:
            print(f"{self.nomi}ning staminasi toliq")

    def tirikmi(self):
        return self.sogliq > 0
    
    def statusini_korsatish(self):
        return f"{self.nomi}: Sogliqi = {self.sogliq}, Staminasi = {self.stamina}"

def jang(Qahramon1, Qahramon2):
    round = 1
    while Qahramon1.tirikmi() and Qahramon2.tirikmi():
        print(f"\nRound {round}:")

        Qahramon1.hujum(Qahramon2)
        Qahramon2.hujum(Qahramon1)

        print(Qahramon1.statusini_korsatish())
        print(Qahramon2.statusini_korsatish())

        if round %3 == 0:
            Qahramon1.dam_olish()
            Qahramon2.dam_olish()
        
        round += 1

    if Qahramon1.tirikmi():
        print(f"\n{Qahramon1.nomi} yutdi!")
    else:
        print(f"\n{Qahramon2.nomi} yutdi!")


if __name__ == "__main__":
    Qahramon1 = Jangchi(nomi="AZAMAT", sogliq=100, quvvat=30, himoya=25, stamina=100)
    Qahramon2 = Jangchi(nomi="TAYSON", sogliq=100, quvvat=30, himoya=25, stamina=100)

    jang(Qahramon1, Qahramon2)