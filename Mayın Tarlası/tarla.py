import random

def mayın_kontrol(tarla, mayınlı, satır, sütun):
    satir_sayisi = len(tarla)
    sutun_sayisi = len(tarla[0])

    mayın = 0

    if sütun > 0:
        if mayınlı[satır][sütun - 1] == "*":
            mayın += 1

    if sütun < sutun_sayisi - 1:
        if mayınlı[satır][sütun + 1] == "*":
            mayın += 1

    if satır > 0:
        if mayınlı[satır - 1][sütun] == "*":
            mayın += 1 

    if satır < satir_sayisi - 1:
        if mayınlı[satır + 1][sütun] == "*":
            mayın += 1

    tarla[satır][sütun] = mayın
    return tarla

def bitiş_kontrol(liste,sayı):
    düz_liste= [eleman for altliste in liste for eleman in altliste]
    if düz_liste.count("-") == sayı:
        return 1
    else:
        return 0

satır = int(input("Satır Sayısı: "))
sütun = int(input("Sütun Sayısı: "))
mayın_sayısı = int(input("Mayın Sayısı: "))

tarla = [["-" for _ in range(sütun)] for _ in range(satır)]
mayınlı_tarla = [["-" for _ in range(sütun)] for _ in range(satır)]

for i in range(mayın_sayısı):
    satir = random.randint(0, len(tarla) - 1)
    sutun = random.randint(0, len(tarla[0]) - 1)
    mayınlı_tarla[satir][sutun] = "*"

düz_liste = [eleman for altliste in mayınlı_tarla for eleman in altliste]
mayın_say = düz_liste.count("*")

for i in mayınlı_tarla:
    for j in i:
        print(j, end=" ")
    print("\n")


for i in range(satır):
    for j in range(sütun):
        print("{}{}{}{}{}".format('(', i, ',', j, ')'), end=" ")
    print("\n")

while True:
    satır1 = int(input("Satır: "))
    sütun1 = int(input("Sütun: "))
    if mayınlı_tarla[satır1][sütun1] == "*":
        print("----KAYBETTİN----")
        for i in mayınlı_tarla:
            for j in i:
                print(j, end=" ")
            print("\n")
        break
    a = mayın_kontrol(tarla, mayınlı_tarla, satır1, sütun1)

    for i in a:
        for j in i:
            print(j, end=" ")
        print("\n")


    if bitiş_kontrol(a,mayın_say) == 1:
        print("----KAZANDIN----")
        for i in mayınlı_tarla:
            for j in i:
                print(j, end=" ")
            print("\n")
        break
        
