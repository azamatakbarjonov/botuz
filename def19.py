def working_info():
    workend_data ={}

    while True:
        key = input("ishchilar haqida malumot kiriting:(Masalan:ismi:,yoshi:,lavozimi)")

        if key.lower() == 'stop':
         break

        value = input(f"{key}ni kiriting:")

        workend_data[key]=value
        
    return workend_data
result = working_info()
print(result)







def talaba_info():
    student_about={}

#     while True:
#         key = input("Studentlarni malumotlarini kiriting:")
#         if key.lower() =="stop":
#             break
#         value = input(f"{key}ning kiriting:")

#         student_about[key]=value
#     return student_about
# succesful = talaba_info()
# print(succesful)








# def davlatlar_info():
#     malumotlar_about={}
#     while True:
#         davlat = input("Davlat nomini :")
#         if davlat.lower() == "stop":
#             break
#         value = input(f"{davlat}ning haqida kiriting: ")
#         malumotlar_about[davlat]=value
#     return malumotlar_about
# succesful = davlatlar_info()
# print(succesful)























