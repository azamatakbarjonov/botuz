class  person:
    def __init__(self, name, last_name, tyil):
        self.name = name
        self.last_name = last_name
        self.tyil = tyil
    

    def info(self):
        return f"{self.name}, {self.last_name}, {self.tyil}"


odam = person("azamat", "akbarjonov", 2010)
print(odam.info())


# class student(person):
#     def __init__(self, name, last_name, tyil, guvohnoma, kurs):
#         super(student,self).__init__(name, last_name, tyil)
#         self.guvohnoma = guvohnoma
#         self.kurs = kurs

#     def get_kurs(self):
#         return self.kurs


# st1 = student("xamid", "abduganiyev", 2001, "ABS10349923190", 1)
# print(st1.info())
# print(st1.get_kurs()) 




# class person:
#     def __init__(self,name, last_name, tyil):
#         self.name = name
#         self.last_name = last_name
#         self.tyil = tyil


#     def info(self):
#         return f"{self.name}, {self.last_name}, {self.tyil}"







# i = 1  # Boshlang‘ich qiymat
# while i <= 10:  # Shart: i 5 dan kichik yoki teng bo‘lsa
#     print(i)  # i ni chiqaramiz
#     i += 1  # i ni 1 ga oshiramiz



# z = 10
# while z >= 1:
#     print(z)
#     z -= 1


# i = 10  # Boshlang'ich qiymat
# while i >= 1:  # Shart: i 1 dan katta yoki teng bo'lsa
#     print(i)  # i ni chiqaramiz
#     i -= 1  # i ni 1 ga kamaytiramiz





# son = []
# for num in range(1,11):
#     if num % 2 == 0:
#         son.append(num**2)
# print(son)





# son = []
# # for num in range(1,21):
# #     if num % 2 == 0:
# #         son.append(num**2)

































