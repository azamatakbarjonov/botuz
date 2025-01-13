# with open('person.txt', 'w') as p:
#     p.write("Rasulov Bexruz\n")
#     p.write("Akbarjonov Azamat\n")
#     p.write("Saidov Bahrom\n")
#     p.write("Xakimov Nodrbek\n")
#     p.write("Agzamov Muhammad\n")
#     p.write("Jamshid Karimov\n")
#     p.write("Kamron Ulugbekov\n")
#     p.write("Abdugani Karimov\n")
#     p.write("Elyor Abduroupov\n")
#     p.write("Miraziz Abdussatorov\n")


# with open('person.txt', 'r') as p:
#     person = p.readlines()
# for person in person:
#     print(person.strip())













# # 1. .txt formatdagi faylni yaratish va unga turli sonlarni kiritish
# with open('numbers.txt', 'w') as n:
#     n.write("12\n")
#     n.write("45\n")
#     n.write("78\n")
    # n.write("23\n")

# # 2. Fayldan sonlarni o'qish
# with open('numbers.txt', 'r') as n:
#     numbers = n.readlines()

# # Sonlarni ro'yxatga aylantirish
# numbers = [int(num.strip()) for num in numbers]

# # 3. Sonlar ustida qo'shish amali bajarish
# total_sum = sum(numbers)  # Sonlarning yig'indisi

# # 4. Natijalarni ekranga chiqarish
# print(f"Sonlarning yig'indisi: {total_sum}")




# with open('guruh.txt','w') as c:
#     c.write("AZAMAT PYTHON\n")
#     c.write("SHUKURULLO HTML\n")
#     c.write("MUHAMMADALI JS\n")
#     c.write("NORBUTA JAVA\n")
#     c.write("DOSTON CSS\n")
#     c.write("SANJAR C##\n")

# with open('guruh.txt', 'r') as rd:
# #     read = rd.readlines()
# # for about in read:
# #     print(about.strip())




# import pickle
# student1 = {'name':'Azamat','surname':'Akbarjonov','year':2010}
# student2 = {'name':'Bakir','surname':'Abdurahmonov','year':2011}

# with open('about.dat', 'wb') as a:
#     pickle.dump(student1, a)
#     pickle.dump(student2, a)

# with open('about.dat', 'rb') as a:
#     oquvchi1 = pickle.load(a)
#     oquvchi2 = pickle.load(a) 
# print(oquvchi1)
# print(oquvchi2)


yosh = 30  # 'yosh' o'zgaruvchisiga yangi qiymat beriladi





# n = ['aka', 25, [ 'uka', 3, 10, 'ona']]

# result = [n[0].upper(), n[1], n[2][1], n[2][1].upper(), n[2][2], n[2][3], n[2][4].upper()]

# print(result)


# n = ['aka', 25, [ 1,'uka', 3, 10, 'ona']]
# work = [n[0].upper(), n[1], n[2][0], n[2][1].upper(),n[2][2],n[2][3],n[2][4].upper()]


# print(work)











z = ['aka', 25, [ 1,'uka', 3, 10, 'ona']]
result = [z[0].upper(), z[1], z[2][0], z[2][1], z[2][2], z[2][3], z[2][4].upper()]

print(result)





