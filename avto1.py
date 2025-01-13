






# ona = {'anor','nok','pomidor','apelsin','banan','karom','olma'}

# men = {'bodiring','olma','xurmo','nok','orik','pomidor'}

# print(ona&men)

# a = ona.union(men)










# # guruh=['Aziz', 'Zuxra',[2005,2008,['-yanvar','-sentyabr','-aperil'],2014],'Akobir',[12,21,['Qashqadaryo_v',['Qamashi_t','Olmazor_t','Katttaqorgon_t'],'Toshkent_v','Samarqand_v'],8]]


# # a=(guruh[0])

# # b=(guruh[-1][2][0])

# # s=(guruh[-1][2][1][0])

# # d=(guruh[2][0])

# # f=(guruh[-1][-1])

# # k=(guruh[2][2][1])


# # print('ismi', a, b, s,'da yashaydi', d,'-yil', f, k,'da tugilgan')






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


def sort_cars_by_price():

    all_cars = []

    for brand, cars in avtosalon.items():

        for car, price in cars.items():

            all_cars.append((car, price))
    

    sorted_cars = sorted(all_cars, key=lambda x: x[1])
    

    print("\nMashinalar narx bo'yicha:")

    for car, price in sorted_cars:

        print(f"{car.title()} --- {price:,.0f} $")


# Mashina ro'yxatini chiqarish bu 


for i in avtosalon:

    print(f"\n{i.upper()}")

    son = 1

    for k, q in avtosalon[i].items():

        print(f"\t{son}. {k.title()} ----------------------- {q:,.0f} $")

        son += 1



for i in avtosalon:
         if   avtosalon[i]:

            print(f"Siz tanlagan mashina: {buyurtma.title()} --- {avtosalon[i][buyurtma]:,.0f} $")

            # Rang tanlash

            rang = input("Mashinangizni qanday rangda olishni xohlaysiz? (red, yellow, blue): ").casefold().strip()

         if rang in ranglar:

                print(f"Rang: {rang.title()} --- {ranglar[rang]:,.0f} $ qo'shildi.")

                client[buyurtma] = avtosalon[i][buyurtma] + ranglar[rang]

                hisob += avtosalon[i][buyurtma] + ranglar[rang]
         else:

                print("Noto'g'ri rang kiritildi, rang qo'shilmaydi.")

                client[buyurtma] = avtosalon[i][buyurtma]

                hisob += avtosalon[i][buyurtma]

                break



# client mashina tanlashi

while True:

    buyurtma = input("Qanday mashina sotib olmoqchisiz? (stop yoki exit deb yozing to'xtatish uchun): ").casefold().strip()


    if buyurtma in ['stop', 'exit']:

        print(f"\nSizning jami sotib olgan mashinangiz: {hisob:,.0f} $")

        break


    for i in avtosalon:

        if buyurtma in avtosalon[i]:

            print(f"Siz tanlagan mashina: {buyurtma.title()} --- {avtosalon[i][buyurtma]:,.0f} $")

            client[buyurtma] = avtosalon[i][buyurtma]

            hisob += avtosalon[i][buyurtma]

            break
    else:

        print("Bunday mashina bizda mavjud emas! Iltimos, boshqa mashina tanlang.")
    

    # Xaridni jami narxini chiqarish bu 

    print(f"Sizning jami xaridingiz: {hisob:,.0f} $")


















