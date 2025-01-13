

# class about:
    # def __init__(self, name, age):
#         self.name = name 
#         self.age = age
    
#     def about_info(self):
#         return f"{self.name} is\t{self.age} years old and azamat"

# wer1 = about("aza",32)
# wer2 = about("zaz",11)

# print(wer1.name)
# # print(wer1.about_info())
# # print(wer2.about_info())




# class car:
#     def __init__(self,name, year,model):
#         self.name = name
#         self.year = year
#         self.model = model
    
#     def car_info(self):
#         return f"{self.name} is {self.year} and {self.model}"

# car1 = car("BMW",2020,"X5")
# car2 = car("CHEVROLET",2023,"MALIBU")

# print(car1.car_info())
# print(car2.car_info())









# class about:
#     def __init__(self,name,surname,ball):
#         self.name = name 
#         self.surname = surname
#         self.ball = ball
    
#     def study_info(self):
#         return f"{self.name}  {self.surname} ning bahosi {self.ball}"

# student1 = about("Azamat", "akbarjonov", 9)
# student2 = about("Otajon", "bozorboyev", 10)

# print(student1.study_info())
# print(student2.study_info())










# class yourself:
#     def __init__(self, name, surname, age, hobby):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.hobby = hobby
    
#     def your_about(self):
#         return f"{self.name} {self.surname} ning yoshi {self.age} da {self.hobby} qiziqadi"

# person1 = yourself("Azamat", "Akbarjonov", 14, "backend da ishlashga")
# person2 = yourself("Azamat", "Akbarjonov", 15, "Treding sohasiga")

# print(person1.your_about())
# print(person2.your_about())








# Agar OOPni yanada mukammal o'zlashtirmoqchi bo'lsangiz, polimorfizm va encapsulation haqida ko'proq mashq qilishni tavsiya qilaman. Bu kontseptsiyalarni to'liq tushunish OOPni yanada chuqurroq o'rganishga yordam beradi.











# p = [1,2,3,4,5]
# f = p.copy()
# f [3] = 777
# print(f)




# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)
# print(b)




# # user = input("Soni kiritng: ")
# # if user.isdigit():
# #     number = int(user)
# #     if number == 20:
# #         print("bu son 20 bn teng")
# #     elif number > 20:
# #         print("bu son 20 dan katta")
# #     else:
# #         print("bu son 20 dan kichik")
# # else:
# #     print("Iltimos, son kiriting!")








# # class about:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age

# #     def about_info(self):
# #         return f"Ismi: {self.name} yoshi: {self.age}"

# # person1 = about("azamat", "11")
# # person2 = about("hoshimjon", "55")

# # print(person1.about_info())
# # print(person2.about_info())







# class Car:
#     def __init__(self, model, color, price, year):
#         self.model = model  # Mashina modeli
#         self.color = color  # Mashina rangi
#         self.price = price  # Mashina narxi
#         self.year = year    # Ishlab chiqarilgan yil
#         self.sold = False   # Mashina sotilgan yoki yo'q

#     def info(self):
#         status = "Sotilgan" if self.sold else "Mavjud"
#         return f"Model: {self.model}, Rang: {self.color}, Narx: {self.price}$, Yil: {self.year}, Holat: {status}"

#     def sell(self):
#         if not self.sold:
#             self.sold = True
#             return f"{self.model} sotildi!"
#         return f"{self.model} allaqachon sotilgan."


# class CarShowroom:
#     def __init__(self, name):
#         self.name = name  # Salon nomi
#         self.cars = []    # Mashinalar ro‘yxati

#     def add_car(self, car):
#         self.cars.append(car)
#         print(f"{car.model} salon ro‘yxatiga qo‘shildi.")

#     def show_cars(self):
#         if not self.cars:
#             return "Salonda mashinalar yo‘q."
#         return "\n".join([car.info() for car in self.cars])

#     def sell_car(self, model_name):
#         for car in self.cars:
#             if car.model == model_name and not car.sold:
#                 print(car.sell())
#                 return
#         print(f"{model_name} yo‘q yoki sotilgan.")

# # Salon yaratish
# my_showroom = CarShowroom("AvtoSalon Super")

# # Mashinalar qo‘shish
# car1 = Car("Toyota Camry", "Oq", 30000, 2022)
# car2 = Car("Chevrolet Malibu", "Qora", 25000, 2021)
# car3 = Car("Hyundai Sonata", "Ko‘k", 27000, 2023)

# my_showroom.add_car(car1)
# my_showroom.add_car(car2)
# my_showroom.add_car(car3)

# # Mashinalarni ko‘rish
# print("\nSalondagi mashinalar:")
# print(my_showroom.show_cars())

# # Mashina sotish
# my_showroom.sell_car("Toyota Camry")

# # Mashinalarni yangilangan holda ko‘rish
# print("\nYangilangan mashinalar ro‘yxati:")
# print(my_showroom.show_cars())








# numbers = [7]
# for number in numbers:
#     print(f"Son: {number}, kvadrati: {number ** 2}")




# numbers = [1,2,3,4,5,]
# for num in numbers:
#     if num % 2 != 0:
        # print(f"son: {num}, kvadrati: {num** 2}")





# numbers = [1, 2, 3, 4, 5]
# # for num in numbers:
#     if num % 2 == 0:  # Juft sonni tekshirish
#         print(f"Son: {num}, kvadrati: {num ** 2}")




# son = []
# number = [1, 2, 3, 4, 5,6,7,8,9,10]

# for num in number:
#     if num % 2 == 0:
#         son.append()
#         print(f"royhat {son}")


# son = []
# for num in range(1,21):
#     if num % 2 == 0:
#         son.append(num**2)
# print(f"judt son",son)



# son = []
# for num in range(1,21):
#     if num % 2 == 0:
# #         son.append(num**2)

# #     else:
# #         print(f"toq sonlar{num}") 


# # print(f"judt sonlar: {son}")

# def toq_sonlar_yigindisi(a, b):
#     return a + b

# print(toq_sonlar_yigindisi(5, 7))















# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def display_info(self):
#         return f"{self.year} {self.brand} {self.model}"

# # ElectricCar klassi Car'dan meros oladi
# class ElectricCar(Car):
#     def __init__(self, brand, model, year, battery_capacity):
#         super().__init__(brand, model, year)  # Asosiy klassdan init chaqiramiz
#         self.battery_capacity = battery_capacity

#     def display_battery_info(self):
#         return f"Battery capacity: {self.battery_capacity} kWh"

# # Ob'ektlar yaratamiz
# car1 = Car("Toyota", "Corolla", 2021)
# car2 = ElectricCar("Tesla", "Model S", 2023, 100)

# print(car1.display_info())  # Oddiy avtomobil ma'lumotlari
# print(car2.display_info())  # Elektromobil ma'lumotlari
# print(car2.display_battery_info())  # Elektromobilning batareya ma'lumotlari




















# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_info(self):
#         return f"Name: {self.name} Age: {self.age}"



# class emploee(person):
#     def __init__(self, name, age, job, position):
#         super().__init__(name, age)
#         self.job = job
#         self.position = position


#     def display_info(self):
#         about_info = super().display_info()
#         return f"{about_info}, Job: {self.job}, Position: {self.position}"

# xodim = emploee("azamat",15,"programmer","juniyor")

# print(xodim.display_info())











# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def play_info(self):
#         return f"Name: {self.name}, Age: {self.age}"


# class emploeee(person):
#     def __init__(self, name, age, hobby, free_time):
#         super().__init__(name, age)
#         self.hobby = hobby
#         self.free_time = free_time


# #     def play_info(self):
# #         about_info = super().play_info()
# #         return f"{about_info}, Hobby: {self.hobby}, free_time: {self.free_time}"

# # student = emploeee("azamm", 15, "treder", "game club")

# # print(student.play_info())






# class people:
#     def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age


    
#     def display_info(self):
#         return f"Name: {self.name}, Last_name: {self.last_name}, Age: {self.age}"



# class meros(people):
#     def __init__(self, name, last_name, age, job, tel_number):
#         super().__init__(name, last_name, age)
#         self.job = job
#         self.tel_number = tel_number


#     def display_info(self):
# #         about_st = super().display_info()
# #         return f"{about_st}, Job: {self.job}, TEL: {self.tel_number}"


# # odam = meros("azamat", "akbarjonov", 15, "programmer", 946920700)

# # print(odam.display_info())












# class animal:
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         return f"Name: {self.name} is  making a sound"


# class dog(animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

#     def speak(self):
#         about = super().speak()
#         return f"{about} Woof!, I am a {self.breed}"


# class cat(animal):
#     def __init__(self, name, color):
#         super().__init__(name)
#         self.color = color

#     def speak(self):
#         about = super().speak()
#         return f"{about} Meau! I am a {self.color} cat"


# class bird(animal):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age

#     def speak(self):
#         about = super().speak()
#         return f"{about} cheap! I am a {self.age}"


# cat = cat("Kittye", "white")
# dog = dog("biss", "alabay")
# bird = bird("eagle",11)

# print(cat.speak())
# print(dog.speak())
# print(bird.speak())










# class transport:
#     def __init__(self, nomi, narxi, yili):
#         self.nomi = nomi
#         self.narxi = narxi
#         self.yili = yili
    
#     def info(self):
#         return f"Nomi: {self.nomi}, Narxi: ${self.narxi}, Yili: {self.yili}"


# class car(transport):
#     def __init__(self, nomi, narxi, yili, moshin_kuzuf):
#         super().__init__(nomi, narxi, yili)
#         self.moshin_kuzuf = moshin_kuzuf

#     def info(self):
#         return super().info() + f", kuzof_moshin: {self.moshin_kuzuf}"


# class malibu(transport):
#     def __init__(self, nomi, narxi, yili, matori):
#         super().__init__(nomi, narxi, yili)
#         self.matori = matori
    

#     def info(self):
#         return super().info() + f", Matori: {self.matori}"


# class mers(transport):
#     def __init__(self, nomi, narxi, yili, rangi):
#         super().__init__(nomi, narxi, yili)
#         self.rangi = rangi

#     def info(self):
#         return super().info() + f",  Rangi: {self.rangi}"


# class avto_salon:
#     def __init__(self):
#         self.transportlar = []

#     def add_transport(self,transport):
#         self.transportlar.append(transport)

    
#     def list_transport(self):
#         for transport in self.transportlar:
#             print(transport.info())

# avto_salon = avto_salon()
# avto_salon.add_transport(car("bmw", 185_000, 2025, "babper"))
# avto_salon.add_transport(malibu("malibu xl", 40_000, 2024, 2))
# avto_salon.add_transport(mers("mers gl63", 300_000, 2025, "qora"))

# avto_salon.list_transport()



# 5 ta sonni kiritish va ularning yig'indisini hisoblash
# total = 0  # Yig'indini saqlash uchun o'zgaruvchi
# count = 0  # Necha marta son kiritilganini hisoblash uchun o'zgaruvchi

# print("5 ta son kiriting:")

# while count < 5:  # Shart: kiritilgan sonlar soni 5 dan kam bo'lsa
#     number = float(input(f"{count + 1}-son: "))  # Foydalanuvchidan son kiritiladi
#     total += number  # Kiritilgan sonni yig'indiga qo'shamiz
#     count += 1  # Son kiritish hisoblagichini oshiramiz

# print(f"Yig'indisi: {total}")  # Yakuniy yig'indini chiqaramiz








# even_count = 0
# evenn_sum = 0
# odd_sum = 0
# odd_count = 0

# print("7 ta son kiriting: ")


# for i in range(7):
#     number = int(input(f"{i + 1}- son: "))

#     if number % 2 == 0:
#         even_count += 1
#         evenn_sum += number

#     else: 
#         odd_count += 1
#         odd_sum += number

# print(f"Juft sonlar: {even_count} ta, yigindisi: {evenn_sum}")
# print(f"Toq sonlar: {odd_count} ta, yigindisi: {odd_sum}")




juft_count = 0
juft_sum = 0
toq_sum = 0
toq_count = 0



print("5 ta son kiriting: ")



for i in range(5):
    number = int(input(f"{i +1}>>>"))

    if number % 2 == 0:
        juft_count += 1
        juft_sum += number

    else:
        toq_count += 1
        toq_sum += number

print(f"Juft sonlar: {juft_count} ta, Yigindisi: {juft_sum}")
print(f"Toq sonlar: {toq_count} ta, Yigindisi: {toq_sum}")



