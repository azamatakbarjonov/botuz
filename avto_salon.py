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

ranglar = {
    'red': 5_000,
    'yellow': 4_500,
    'blue': 4_000,
    'white': 3_500,
    'black': 6_000,
    'green': 5_000,
    'pink': 4_000,
}

hisob = 0
client = {}

# Mashina ro'yxatini chiqarish
for i in avtosalon:
    print(f"\n{i.upper()}")
    son = 1
    for k, q in avtosalon[i].items():
        print(f"\t{son}. {k.title()} ----------------------- {q:,.0f} $")
        son += 1

# Mashina tanlash va xarid qilish
while True:
    buyurtma = input("Qanday mashina sotib olmoqchisiz? (stop yoki exit deb yozing to'xtatish uchun): ").casefold().strip()

    if buyurtma in ['stop', 'exit']:
        print(f"\nSizning jami sotib olgan mashinangiz: {hisob:,.0f} $")
        break

    # Mashina mavjudligini tekshirish
    for i in avtosalon:
        if buyurtma in avtosalon[i]:
            print(f"Siz tanlagan mashina: {buyurtma.title()} --- {avtosalon[i][buyurtma]:,.0f} $")
            client[buyurtma] = avtosalon[i][buyurtma]
            hisob += avtosalon[i][buyurtma]

            # Rang tanlash
            rang = input("Mashinangizni qanday rangda olishni xohlaysiz? (red, yellow, blue): ").casefold().strip()

            if rang in ranglar:
                print(f"Rang: {rang.title()} --- {ranglar[rang]:,.0f} $ qo'shildi.")
                client[buyurtma] += ranglar[rang]
                hisob += ranglar[rang]
            else:
                print("Noto'g'ri rang kiritildi, rang qo'shilmaydi.")
            
            break
    else:
        print("Bunday mashina bizda mavjud emas! Iltimos, boshqa mashina tanlang.")
    
    # Xaridni jami narxini chiqarish
    print(f"Sizning jami xaridingiz: {hisob:,.0f} $")















