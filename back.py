import random as r

ismlar = ['azamat','doston','muhammadali','shukurlo','norbuta','ogabek']
python = ['def','while','if','dct','for i in','import']


ismlar = r.choice(ismlar)
lst = r.choice(python)

print(f"Tanlangan ism: {ismlar}")
print(f"Tanlangan dastur: {lst}")



def talaba_info():
    student_about={}

    while True:
        key = input("Studentlarni malumotlarini kiriting:")
        if key.lower() =="stop":
            break
        value = input(f"{key}ning kiriting:")

        student_about[key]=value
    return student_about
succesful = talaba_info()
print(succesful)





def davlatlar_info():
    malumotlar_about={}
    while True:
        davlat = input("Davlat nomini :")
        if davlat.lower() == "stop":
            break
        value = input(f"{davlat}ning haqida kiriting: ")
        malumotlar_about[davlat]=value
    return malumotlar_about
succesful = davlatlar_info()
print(succesful)













