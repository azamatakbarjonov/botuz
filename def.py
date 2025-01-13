def user_info(isim, familiya, tugilgan_yil, tugilgan_joy, email=None, telefon=None):
    user_data = {
        'Ism': isim,
        'Familiya': familiya,
        'Tug\'ilgan Yil': tugilgan_yil,
        'Tug\'ilgan Joy': tugilgan_joy,
        'Email': email,
        'Telefon': telefon
    }
    
    if not email:
        del user_data['Email']
    if not telefon:
        del user_data['Telefon']
    
    return user_data

isim = input("Ismingizni kiriting: ")
familiya = input("Familiyangizni kiriting: ")
tugilgan_yil = int(input("Tug'ilgan yilingizni kiriting: "))
tugilgan_joy = input("Tug'ilgan joyingizni kiriting: ")
email = input("Elektron pochta (ixtiyoriy): ")
telefon = input("Telefon raqami (ixtiyoriy): ")

foydalanuvchi_malumotlari = user_info(isim, familiya, tugilgan_yil, tugilgan_joy, email or None, telefon or None)
print(foydalanuvchi_malumotlari)






son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
son3 = float(input("Uchunchi sonni kiriting: "))

eng_katta = max(son1, son2)

print("Eng  katta son:", str(eng_katta))  



































