import random
sayiAralik=int(input("0'dan kaça kadar bir sayı tutmamı istersiniz :"))
sayi=random.randint(0,sayiAralik)
hak=5
ipucu=0
print(sayi)

# * asal sayı olup olmadığı
bolenler=0
for i in range(2,sayi):
    if sayi%i==0:
        bolenler+=1
if bolenler>=1:
    asal=False
else: 
    asal=True

# * faktöriyelini hesaplama
faktor=1
for i in range(1,sayi+1):
    faktor*=i

# * bölenlerini bulma
bolen=[]
for i in range(1,sayi):
    if sayi%i==0:
        bolen.append(i)

for i in range(1,10):
    if i==6:
        print(f"Haklarınız doldu! Tutulan sayı: {sayi}")
        break
    tahminSay=int(input(f"{hak} hakkınız var. {i}. tahmininizi giriniz :"))
    if tahminSay==sayi:
        print(f"{i}. hakkınızda bildiniz! Tutulan sayı : {sayi}")
        break
    elif tahminSay<sayi:
        print(f"{tahminSay} tutulan sayıdan küçük!")
        hak-=1
    elif tahminSay>sayi:
        print(f"{tahminSay} tutulan sayıdan büyük!")
        hak-=1
    if hak<=4 and hak>1:
        tip=input(f"İpucu ister misiniz? e/h :")
        if tip=="e":
            kalan=sayi%2
            if ipucu==0 and kalan==0:
                print("Tutulan sayı bir çift sayı.")
                ipucu+=1
            elif ipucu==0 and kalan==1:
                print("Tutulan sayı bir tek sayı.")
                ipucu+=1
            elif ipucu==1 and asal==True:
                print("Tutulan sayı asal bir sayıdır.")
                ipucu+=1
            elif ipucu==1 and asal==False:
                print("Tutulan sayı asal bir sayı değildir.")
                ipucu+=1
            elif ipucu==2 and sayi<20:
                print(f"Tutulan sayının faktöriyeli : {faktor}")
                ipucu+=1
            elif ipucu==2 and sayi>=20:
                print(f"Tutulan sayının bölenleri : {bolen}")
                ipucu+=1
            elif ipucu>=3:
                continue
        elif tip=="h":
            print("Denemeye devam o zaman!")
        elif tip!="e" and tip!="h":
            print(f"Hatalı giriş! Tutulan sayı : {sayi}")
            break