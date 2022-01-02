#7.soru B ŞIKKI
    
adet=0
toplam=0
ortalama=0

while True:

    girilen_sayi=int(input("Lutfen pozitif sayi giriniz: "))
  
    if girilen_sayi<0: #sayı negatif girilirse döngüyü kıracak
        break
    
    toplam+=girilen_sayi #girilen sayıları topluyoruz
    adet+=1 #sayı girişi oldukça kaç adet girildiğini hesaplıyoruz
    ortalama=toplam/adet #ortalama formülü
    
print("{} tane sayı girdiniz.".format(adet))
print("Girdiginiz sayilarin toplami: {} ".format(toplam))
print("Girdiginiz sayilarin ortalamasi: {} ".format(ortalama))






     