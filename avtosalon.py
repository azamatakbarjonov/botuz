avtosalon = {
        "MERS": {
        'mers amg63': 200_000,
        'mers gls450': 145_000,
        'mers gelik': 270_000,
        'mers 43 gls':80_000,
        'mers 222':110_000,
    },
    "BMW": {
        'bmw x7 drive':85_000,
        'bmw i8':76_000,
        'bmw x6':55_000,
        'bmw m8':138_000,
        'bmw m5 f90 competition':115_000
    },
    "TESLA":{
        'tesla model x':83_000,
        'tesla cybertruck':120_000,
        'tesla model 3':45_000,
        'tesla model s':85_000
    },
    "ROLLS-Royce":{
         'rolls-royce phantom':490_000,
         'rolls-royce cullinan':450_000,
         'rolls-royce ghost':380_000,
         'rolls-royce spectre':430_000

    },
    "FERRARI": {
        'ferrari296 gtb':370_000,
        'ferrari roma':260_000,
        'ferrari sf90':400_000,
        'ferrari purosangue':378_000

    }
}
hisob = 0
client = {}

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

for i in avtosalon:
    print(f"\n{i.upper()}")
    son = 1
    for k,q in avtosalon[i].items():
        print(f"\t{son}. {k.title()} --------------------- {q:,.0f} $")
        son += 1

while True:
    buyurtma = input(" Qanday mashina sotib olmoqchisiz: ").casefold().strip()
    for i in avtosalon:
        if buyurtma in avtosalon[i]:
         print(f"{avtosalon[i][buyurtma]} $")
         client[buyurtma] = avtosalon[i][buyurtma]
         hisob += avtosalon[i][buyurtma]
         break
    else:
        if buyurtma in ['stop', 'exit']:
            print(f"\n UMMMIY MASHINALAR: {hisob} $")
            break
        else:
            print("BUNDAY MASHINA BIZDA MAVJUD EMAS!")
            
    if choice == '5':
        car_name = input("Sotib olish uchun mashina nomini kiriting: ").casefold()
    for brand, cars in avtosalon.items():
        for car, price in cars.items():
         if car_name in car.casefold():
          print(f"Siz tanlagan mashina: {car.title()}")
          print(f"Narxi: {final_price:,.0f} $")
          hisob += final_price
          client[car] = final_price













    

























