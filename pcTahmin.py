import random

hak=int(input("Bana kaç tahmin hakkı vereceksin?"))
ipucu=0

# * Sayı aralığı belirleyip bu aralıkta bir random sayı tutulmasını sağlıyoruz.
# * Tahmin edilecek sayı x olacak.
maxSayi=int(input("0 ile hangi sayı arasında bir sayı tutmak istersiniz : "))
x=random.randint(0,maxSayi+1)
print(f"Tahmin etmem gereken sayı : {x}")

# * Tahmin edilecek x sayısının çift mi ya da tek mi olduğunu anlamasını sağlamak için listelendirdik
sayList=[]
tekler=[]
ciftler=[]
for i in range(0,maxSayi+1):
    sayList.append(i)
    if i%2==0:
        ciftler.append(i)
    else:
        tekler.append(i)
# * Büyüklük küçüklük için listelendirdik
kucukler=[]
buyukler=[]
for i in range(maxSayi+1):
    if i<x:
        kucukler.append(i)
    else:
        buyukler.append(i)
# * ortak listeleri oluşturduk
buyukcift=[]
kucukcift=[]
buyuktek=[]
kucuktek=[]
for i in range(maxSayi+1):
    if i>x and i in ciftler:
        buyukcift.append(i)
    elif i>x and i in tekler:
        buyuktek.append(i)
    elif i<x and i in ciftler:
        kucukcift.append(i)
    elif i<x and i in tekler:
        kucuktek.append(i)
tahminler=[]    

for i in range(1,hak+1):
    tahminSay=random.choice(sayList)
    tahminler.append(tahminSay)
    sayList=list(set(sayList)-set(tahminler))
    cevap=input(f"{i}. tahminim : {tahminSay}\nDoğru mu bildim? e/h")
    if cevap=="e" and tahminSay==x:
        print(f"Demek tuttuğun sayı {tahminSay}!\n{i}. tahminimde buldum!\nAferin bana!!!")
        break
    elif cevap=="e" and tahminSay!=x:
        print(f"Beni kandırmaya mı çalışıyorsun?\nTutulan sayı {x},benim tahminim {tahminSay}.\nÜzdün..")
        break
    elif cevap=="h" and tahminSay==x:
        print(f"Beni kandırmaya mı çalışıyorsun?\nTutulan sayı {x},benim tahminim {tahminSay}.\nÜzdün..")
        break
    elif cevap=="h" and tahminSay!=x:
        hak-=1
        if hak==0:
            print(f"Bilemediğime inanamıyorum!\nDemek tutulan sayı {x} idi.\nJavascriptle python bir tahmin oyununu kazanamadı diye arkamdan konuşmayın!")
            break
        ipucu1=input(f"{hak} hakkım kaldı. Hımmm....\nBana ipucu verebilir misin? e/h")
        if ipucu1=="e":
            if ipucu==0:
                tekCift=input(f"Tutulan sayı çift bir sayı mı? e/h")
                if tekCift=="e":
                    sayList=ciftler
                    ipucu+=1
                elif tekCift=="h":
                    sayList=tekler
                    ipucu+=1
                else:
                    print("Hatalı giriş yaptın.\nOynamıyorum!!")
                    break
            elif ipucu==1:
                ipucu2=input(f"Tutulan sayı {tahminSay} sayısından büyük mü? e/h")
                if ipucu2=="e" and tahminSay<x and x in ciftler:
                    print("Hımm demek büyük!")
                    sayList=buyukcift
                elif ipucu2=="e" and tahminSay<x and x in tekler:
                    print("Hımm demek büyük!")
                    sayList=buyuktek
                elif ipucu2!="e" and tahminSay<x:
                    print(f"Beni KANDIRMA!")
                    break
                elif ipucu2=="h" and tahminSay>x and x in ciftler:
                    print("Hımm demek küçük!")
                    sayList=kucukcift
                elif ipucu2=="h" and tahminSay>x and x in tekler:
                    print("Hımm demek küçük!")
                    sayList=kucuktek
                elif ipucu2!="h" and tahminSay>x:
                    print(f"Beni KANDIRMA!")
                    break
            elif ipucu>1:
                print("Vazgeçtim, başka ipucu verme! Kendim bulmak istiyorum!")
        elif ipucu1=="h":
                print("Aşkolsun!\nBen olsam sana ipucu verirdim!")





