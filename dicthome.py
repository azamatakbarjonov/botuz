#         total = price * 1.05  # 5% foiz
#     elif choice == '3':
#         months = 12
#         total = price * 1.1  # 10% foiz
#     else:
#         print("Noto'g'ri tanlov!")
#         return
    
#     monthly_payment = total / months
#     print(f"\n{months} oy davomida har oyda {monthly_payment:,.2f} $ to'lash kerak.")
#     print(f"Jami to'lov: {total:,.2f} $")
    
# # Chegirmalarni hisoblash
# def apply_discount(price):
#     discount = 0# mers = []
# # for i in range (15):
# #       NewCar = {
# #          'made': None,
# #         'model': None,
# #         'color': None,
# #         'price': 0,
# #         'engine': None,
# #       }
# #       mers.append(NewCar)
# # for i in mers[:3]:
# #         i ['made'] = 'BMW'
# #         i ['model'] = 'X7'
# #         i ['engine'] = 'auto'
# #         i ['price'] = 100_000
# #         i ['color'] = 'royalblue'

# #         # print(mers)
        
# # for i in mers[6:9]:
# #         i ['made'] = 'TOYOTA'
# #         i ['model'] = 'Prado'
# #         i ['engine'] = 'mechanic'
# #         i ['price'] = 130_000
# #         i ['color'] = 'white'

# # for i in mers[9:12]:
# #         i ['made'] = 'TESLA'
# #         i ['model'] = 'dirvecar3'
# #         i ['engine'] = 'mechanic'
# #         i ['price'] = 180_000
# #         i ['color'] = 'green'

# # for i in mers[12:15]:
# #         i ['made'] = 'BUGGATI'
# #         i ['model'] = 'CHiron'
# #         i ['engine'] = 'auto'
# #         i ['price'] = 980_000
# #         i ['color'] = 'blue'

# # for i in mers:
# #     if i['engine'] == "automatic":
# #         i['price'] += 50_000
# #     elif i['engine'] == 'mechanic':
# #         i['price'] += 30_000
# #     else:
# #         i['price'] += 10_000

# # for i in mers:
# #   print(i.values())







# avtosalon = {
#     "MERS": {
#         'mers amg63': 200_000,
#         'mers gls450': 145_000,
#         'mers gelik': 270_000,
#         'mers 43 gls': 80_000,
#         'mers 222': 110_000,
#     },
#     "BMW": {
#         'bmw x7 drive': 85_000,
#         'bmw i8': 76_000,
#         'bmw x6': 55_000,
#         'bmw m8': 138_000,
#         'bmw m5 f90 competition': 115_000
#     },
#     "TESLA": {
#         'tesla model x': 83_000,
#         'tesla cybertruck': 120_000,
#         'tesla model 3': 45_000,
#         'tesla model s': 85_000
#     },
#     "ROLLS-Royce": {
#          'rolls-royce phantom': 490_000,
#          'rolls-royce cullinan': 450_000,
#          'rolls-royce ghost': 380_000,
#          'rolls-royce spectre': 430_000
#     },
#     "FERRARI": {
#         'ferrari296 gtb': 370_000,
#         'ferrari roma': 260_000,
#         'ferrari sf90': 400_000,
#         'ferrari purosangue': 378_000
#     }
# }

# hisob = 0
# client = {}

# # Mashina kategoriyasini tanlash
# def display_categories():
#     print("\nAvtosalon kategoriyalari:")
#     for i in avtosalon:
#         print(f"- {i}")

# def display_cars_by_category(category):
#     print(f"\n{category.upper()} Kategoriyasidagi mashinalar:")
#     son = 1
#     for k, q in avtosalon[category].items():
#         print(f"\t{son}. {k.title()} --------------------- {q:,.0f} $")
#         son += 1

# # Bo'lib to'lashni hisoblash
# def payment_plan(price):
#     print("\nTo'lov rejasini tanlang:")
#     print("1. 3 oy davomida 0% foizli to'lov")
#     print("2. 6 oy davomida 5% foizli to'lov")
#     print("3. 12 oy davomida 10% foizli to'lov")
    
#     choice = input("Tanlovni kiriting (1/2/3): ")
#     if choice == '1':
#         months = 3
#         total = price
#     elif choice == '2':
#         months = 6

#     if price > 300_000:
#         discount = 0.1  # 10% chegirma
#     elif price > 100_000:
#         discount = 0.05  # 5% chegirma
#     elif price < 50_000:
#         discount = 0.02  # 2% chegirma
    
#     discounted_price = price * (1 - discount)
#     if discount > 0:
#         print(f"Chegirma: {discount*100}%")
#     return discounted_price

# # Mashinalarni saralash
# def sort_cars_by_price():
#     all_cars = []
#     for brand, cars in avtosalon.items():
#         for car, price in cars.items():
#             all_cars.append((car, price))
    
#     # Narx bo'yicha saralash (kamdan ko'proq narx)
#     sorted_cars = sorted(all_cars, key=lambda x: x[1])
    
#     print("\nMashinalar narx bo'yicha:")
#     for car, price in sorted_cars:
#         print(f"{car.title()} --- {price:,.0f} $")

# # Avtosalonni boshlash
# while True:
#     print("\nAvtosalon menyusi:")
#     print("1. Kategoriyani tanlash")
#     print("2. Mashinalarni narx bo'yicha saralash")
#     print("3. To'lov rejasini ko'rish")
#     print("4. Chegirma olish")
#     print("5. Avtomobil sotib olish")
#     print("6. Chiqish")
    
#     choice = input("Tanlovni kiriting (1-6): ")
    
#     if choice == '1':
#         display_categories()
#         category = input("Tanlangan kategoriya: ").title()
#         if category in avtosalon:
#             display_cars_by_category(category)
#         else:
#             print("Noto'g'ri kategoriya.")
    
#     elif choice == '2':
#         sort_cars_by_price()
    
#     elif choice == '3':
#         car_name = input("To'lov rejasini ko'rish uchun mashina nomini kiriting: ").casefold()
#         for brand, cars in avtosalon.items():
#             for car, price in cars.items():
#                 if car_name in car.casefold():
#                     payment_plan(price)
#                     break
#         else:
#             print("Mashina topilmadi!")
    
#     elif choice == '4':
#         car_name = input("Chegirma olish uchun mashina nomini kiriting: ").casefold()
#         for brand, cars in avtosalon.items():
#             for car, price in cars.items():
#                 if car_name in car.casefold():
#                     discounted_price = apply_discount(price)
#                     print(f"Yangi narx: {discounted_price:,.0f} $")
#                     break
#         else:
#             print("Mashina topilmadi!")
    
#     elif choice == '5':
#         car_name = input("Sotib olish uchun mashina nomini kiriting: ").casefold()
#         for brand, cars in avtosalon.items():
#             for car, price in cars.items():
#                 if car_name in car.casefold():
#                     final_price = apply_discount(price)
#                     print(f"Siz tanlagan mashina: {car.title()}")
#                     print(f"Narxi: {final_price:,.0f} $")
#                     hisob += final_price
#                     client[car] = final_price
                    
#                     # Kredit to'lov rejasini tanlash
#                     print("\nTo'lov rejasini tanlang:")
#                     print("1. To'liq to'lash")
#                     print("2. Kredit/Bo'lib to'lash")
#                     payment_choice = input("Tanlovni kiriting (1/2): ")
                    
#                     if payment_choice == '1':
#                         print(f"Siz to'liq {final_price:,.0f} $ to'lashni tanladingiz.")
#                     elif payment_choice == '2':
#                         payment_plan(final_price)
#                     else:
#                         print("Noto'g'ri tanlov!")
#                     break
#         else:
#             print("Mashina topilmadi!")
    
#     elif choice == '6':
#         print(f"\nUmumiy xarajatlar: {hisob:,.0f} $")
#         break













avtosalon = {
    "MERS": {
        'mers amg63': 200_000,
        'mers gls450': 145_000,
        'mers gelik': 270_000,
        'mers 43 gls': 80_000,
        'mers 222': 110_000,
    },
    "BMW": {
        'bmw x7 drive': 85_000,
        'bmw i8': 76_000,
        'bmw x6': 55_000,
        'bmw m8': 138_000,
        'bmw m5 f90 competition': 115_000
    },
    "TESLA": {
        'tesla model x': 83_000,
        'tesla cybertruck': 120_000,
        'tesla model 3': 45_000,
        'tesla model s': 85_000
    },
    "ROLLS-Royce": {
         'rolls-royce phantom': 490_000,
         'rolls-royce cullinan': 450_000,
         'rolls-royce ghost': 380_000,
         'rolls-royce spectre': 430_000
    },
    "FERRARI": {
        'ferrari296 gtb': 370_000,
        'ferrari roma': 260_000,
        'ferrari sf90': 400_000,
        'ferrari purosangue': 378_000
    }
}

hisob = 0
client = {}

# Mashina kategoriyasini tanlash
def display_categories():
    print("\nAvtosalon kategoriyalari:")
    for i in avtosalon:
        print(f"- {i}")

def display_cars_by_category(category):
    print(f"\n{category.upper()} Kategoriyasidagi mashinalar:")
    son = 1
    for k, q in avtosalon[category].items():
        print(f"\t{son}. {k.title()} --------------------- {q:,.0f} $")
        son += 1

# Bo'lib to'lashni hisoblash
def payment_plan(price):
    print("\nTo'lov rejasini tanlang:")
    print("1. 3 oy davomida 0% foizli to'lov")
    print("2. 6 oy davomida 5% foizli to'lov")
    print("3. 12 oy davomida 10% foizli to'lov")
    
    choice = input("Tanlovni kiriting (1/2/3): ")
    if choice == '1':
        months = 3
        total = price
    elif choice == '2':
        months = 6
        total = price * 1.05  # 5% foiz
    elif choice == '3':
        months = 12
        total = price * 1.1  # 10% foiz
    else:
        print("Noto'g'ri tanlov!")
        return
    
    monthly_payment = total / months
    print(f"\n{months} oy davomida har oyda {monthly_payment:,.2f} $ to'lash kerak.")
    print(f"Jami to'lov: {total:,.2f} $")
    
# Chegirmalarni hisoblash
def apply_discount(price):
    discount = 0
    if price > 300_000:
        discount = 0.1  # 10% chegirma
    elif price > 100_000:
        discount = 0.05  # 5% chegirma
    elif price < 50_000:
        discount = 0.02  # 2% chegirma
    
    discounted_price = price * (1 - discount)
    if discount > 0:
        print(f"Chegirma: {discount*100}%")
    return discounted_price

# Mashinalarni saralash
def sort_cars_by_price():
    all_cars = []
    for brand, cars in avtosalon.items():
        for car, price in cars.items():
            all_cars.append((car, price))
    
    # Narx bo'yicha saralash (kamdan ko'proq narx)
    sorted_cars = sorted(all_cars, key=lambda x: x[1])
    
    print("\nMashinalar narx bo'yicha:")
    for car, price in sorted_cars:
        print(f"{car.title()} --- {price:,.0f} $")

# Avtosalonni boshlash
while True:
    print("\nAvtosalon menyusi:")
    print("1. Kategoriyani tanlash")
    print("2. Mashinalarni narx bo'yicha saralash")
    print("3. To'lov rejasini ko'rish")
    print("4. Chegirma olish")
    print("5. Avtomobil sotib olish")
    print("6. Chiqish")
    
    choice = input("Tanlovni kiriting (1-6): ")
    
    if choice == '1':
        display_categories()
        category = input("Tanlangan kategoriya: ").title()
        if category in avtosalon:
            display_cars_by_category(category)
        else:
            print("Noto'g'ri kategoriya.")
    
    elif choice == '2':
        sort_cars_by_price()
    
    elif choice == '3':
        car_name = input("To'lov rejasini ko'rish uchun mashina nomini kiriting: ").casefold()
        for brand, cars in avtosalon.items():
            for car, price in cars.items():
                if car_name in car.casefold():
                    payment_plan(price)
                    break
        else:
            print("Mashina topilmadi!")
    
    elif choice == '4':
        car_name = input("Chegirma olish uchun mashina nomini kiriting: ").casefold()
        for brand, cars in avtosalon.items():
            for car, price in cars.items():
                if car_name in car.casefold():
                    discounted_price = apply_discount(price)
                    print(f"Yangi narx: {discounted_price:,.0f} $")
                    break
        else:
            print("Mashina topilmadi!")
    
    elif choice == '5':
        car_name = input("Sotib olish uchun mashina nomini kiriting: ").casefold()
        for brand, cars in avtosalon.items():
            for car, price in cars.items():
                if car_name in car.casefold():
                    final_price = apply_discount(price)
                    print(f"Siz tanlagan mashina: {car.title()}")
                    print(f"Narxi: {final_price:,.0f} $")
                    hisob += final_price
                    client[car] = final_price
                    
                    # Kredit to'lov rejasini tanlash
                    print("\nTo'lov rejasini tanlang:")
                    print("1. To'liq to'lash")
                    print("2. Kredit/Bo'lib to'lash")
                    payment_choice = input("Tanlovni kiriting (1/2): ")
                    
                    if payment_choice == '1':
                        print(f"Siz to'liq {final_price:,.0f} $ to'lashni tanladingiz.")
                    elif payment_choice == '2':
                        payment_plan(final_price)
                    else:
                        print("Noto'g'ri tanlov!")
                    break
        else:
            print("Mashina topilmadi!")
    
    elif choice == '6':
        print(f"\nUmumiy xarajatlar: {hisob:,.0f} $")
        break
    





