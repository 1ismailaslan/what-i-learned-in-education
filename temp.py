# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
"""
"""
i = 0
while(i < 10):
    print("i nin değeri",i)
    i += 1
"""
"""
defkullanici = "ismailaslan"
defparola = "1234"
while(True):
    kullanici = input("kullanıcı adınızı giriniz:")
    parola = input("parolanızı giriniz:")
    if((kullanici == defkullanici) and(parola == defparola)):
        print("sisteme hoşgeldiniz...",kullanici)
        break
    elif((kullanici != defkullanici) and (parola == defparola)):
        print("kullanıcı adınızı kontrol ediniz!")
    elif((kullanici == defkullanici) and (parola != defparola)):
        print("parolanızı kontrol ediniz!")
        print("şifrenizi değiştirmek ister misiniz?(E/H)")
        cevap = input()
        if (cevap == "E"):
            yeniparola = input("yeni parolanızı giriniz:")
            print("Lütfen bekleyiniz...")
            defparola = yeniparola
            print("Şifreniz başarıyla değiştirilmiştir")
    else:
        print("tekrar deneyiniz")
"""
"""
x = 1
while x <= 100:
    if x % 2 == 1:
        print(f'sayı tek: {x}')
    else:
        print(f'sayı çift {x}')
    x += 1    
    
print("bitti...")
"""


"""
km_litre = float(input("aracınız km başına ne kadar yakıt tüketiyor?: "))
yakit_birim_fiyati = float(input("kullandığınız yakıtın güncel fiyatını giriniz: ")) 
km = int(input("aracınızla kaç km yol yapacaksınız?: "))   
km_basi_fiyat = (km_litre * yakit_birim_fiyati) / 100
tutar = km_basi_fiyat * km
print("aracın yol masrafı: {:.2f} lira".format(tutar))
"""

#for döngüsü
"""
string = "ismail"
for i in string:
    print(i)
"""




#for döngüsü liste elemanlarının bastırma
"""
list = ["ismail","aslan","masssaka","diablo","36","killa"] 
for i in list:
    print(i)
"""


#range komutu ile 10 elemanlı liste oluşturma
"""    
print(*range(10))
""" 


#range komutu kullanımı
"""   
for i in range(20):
    print(i)
"""
"""
for i in range(1,20):
    print(i*"*")
"""


#faktöriyel hesaplama
"""
faktöriyel = 1 
while True:
    sayi = int(input("lütfen negatif olmayan bir sayı giriniz: "))
    if (sayi <= 0):
        print("hatalı giriş yaptınız!")
    else:
        for i in range(1, sayi+1):
            faktöriyel *= i
        print("faktöriyel",faktöriyel)
        break
"""   
""" 
name = input("lütfen isim giriniz: ")
for i in range(5):
    print(name)
""" 


#break komutu çalışması
"""
for i in range(1,101):
    if i %2 == 0:
        print(i)
""" 
"""
def_kullanici = "ismail"
def_parola = "1234"
while True:
    kullanici = input("kullanıcı adınızı giriniz: ")
    parola = input("parolanızı giriniz: ")
    if ((kullanici != def_kullanici) or (parola != def_parola)):
        print("hatalı giriş yaptınız!")
    else:
        print("sisteme hoşgeldiniz...")
        break
"""


#fonksiyonlara giriş ilk çalışma
"""
def i():
    print("ismailaslan")

i()
"""

#fonksiyonlar faktöriyel hesaplama
"""
def factoriel(numara):
    faktöriyel =1
    for i in range(1,numara+1):
        faktöriyel *= i
    print("faktöriyel = ",faktöriyel)
    
sayi = int(input("sayı giriniz: ")) 

factoriel(sayi)
factoriel(3)
factoriel(4)
factoriel(5)
factoriel(6)
factoriel(7)
"""    




#kok hesaplama fonksiyonu
"""
def kokbul(a,b,c):
    delta = (b*b - 4*a*c)
    if (delta < 0):
        print("reel kk bulunamamıştır")
        return
    
    x1 = (-b - delta**0.5) / 2*a
    x2 = (-b + delta**0.5) / (2*a)
    
    return(x1,x2)
    
a = int(input("a: "))    
b = int(input("b: "))
c = int(input("c: "))

sonuc = kokbul(a,b,c)  

print(sonuc)      
"""    



#varsayılan değerler (hatalı kod var)
"""
def kayit_ekle(ad= "bilgi yok",soyad= "bilgi yok",yas= "bilgi yok",meslek= "bilgi yok"):
    print("kayıt ekleniyor...")
    
print("ad: {}\n soyad: {}\n yas: {}\n meslek: {}".format(ad,soyad,yas,meslek))

print("kayıt başarıyla eklendi")

#161.satırda hata aldım.
"""



#geometrik şekil hesaplam 
"""
def geometri(sekil):
    if len(sekil) == 3:
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]
        
        
        if (a+b) > c and (a+c) > b and (b+c) > a:
            if (a == b) and (a == b) and (b == c):
                print("bu bir eşkenar üçgendir")
            elif (a == b) and (a == c):
                print("bu bir ikizkenar üçgendir")
            else:
                print("bu bir çeşit kenar üçgendir")

        else:
            print("üçgen belirtmiyor")
            
    
    elif len(sekil) == 4:
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]
        d = sekil[3]
        if (a == b) and (a == c) and (a == d):
            print("bu bir karedir")
        elif (a == c) and (b == d):
            print("bu bir dikdörtgendir")
        else:
            print("normal dörtgen")
            
        
        
    else:
        print("herhangi bir şekil bulunamadı")        
        
      
while (True):
    eleman_sayisi = int(input("eleman sayısını giriniz: "))
    if (eleman_sayisi == 3):
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        geometri([a,b,c])
              
    elif (eleman_sayisi == 4):
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        d = int(input("d: "))
        geometri([a,b,c,d])
               
    else:
        print("lütfen tekrar deneyiniz")
"""
#UDEMY EĞİTİM 1 YÖNTEM 1    
"""
def ayni_mi(yazi):
    
    if yazi.isupper():
        return True
    
    elif yazi.islower():
        return True
    
    else:
        return False
    
print(ayni_mi("İsmail"))
"""
#UDEMY EĞİTİM 1 YÖNTEM 2
"""
ayni_mi = lambda yazi : yazi.isupper() or yazi.islower()
"""
#UDEMY EĞİTİM 2 HATA ALDIM
"""
def carpanlar(sayi):
    
    liste = []
    
    for i in range(1,sayi+1):
        
        if sayi % i == 0:
            
            liste.append(i)
            
            return liste     
        
print(carpanlar(12))
"""
#UDEMY EĞİTİM 3 
"""
def hayvan_bacak_sayisi(tavuk,inek,koyun):
    tavuk_bacak = 2*tavuk
    inek_bacak = 4*inek
    koyun_bacak = 4*koyun
    cevap = tavuk_bacak + inek_bacak + koyun_bacak
    return cevap
print(hayvan_bacak_sayisi(10, 30, 50))
"""
"""
#UDEMY EĞİTİM 3 YÖNTEM 2
def hayvanlar(t,i,k):
    return t*2+(i+k)*4

print(hayvanlar(10, 30, 50))
"""
"""

name = input("yaşıonızı giriniz: ")

age = int(input("yaşınızı giriniz: "))

year = str((2022 - age ) + 100)

print(name + " " + year + " " + " yılında 100 yaşında olacak ")

"""
"""
name = input("isminizi giriniz: ")

surname = input("soyadınızı giriniz: ") 

print("merhabalar",name, surname,"hoşgeldiniz efendim")

sayi1 = float(input("vize notunuzu giriniz: "))

sayi2 = float(input("final notunuzu giriniz: "))

sayilar = sayi1 + sayi2

sayibölünen = sayilar/2
               
print("toplam puan: ", sayilar,"\n" "geçerli olan puan" , sayibölünen)

if sayibölünen >= 50:
    
    print("geçtiniz...")
    
elif sayibölünen <= 50:
    
    print("kaldınız...:/")
"""   
# benim yazdığım şifre oluşturma kodu hata veriyor şifreleri yanlış sıralıyor
"""
    
import random

Chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"

password_len = int(input("şifre kaç karakterden olşturulsun: "))
password_count = int(input("kaç adet şifre oluşturulsun: "))
for x in range(0, password_count):
    password = ""
    for x in range(0, password_len):
        password_char = random.choice(Chars)
        password      = password + password_char
        print("rondom şifreniz : ", password)
"""        
"""        
import random
Chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
 
password_len = int(input("Şifre kaç karakterden oluşturulsun : "))
password_count = int(input("Kaç adet şifre oluşturulsun : "))
for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(Chars)
            password      = password + password_char
        print("Random Şifreniz : " , password)
 """
#takvim        
"""
import calendar
yil = int(input("yıl giriniz : "))
ay = int(input("ay giriniz : "))
print(calendar.month(yil, ay))
"""
"""
a = ["ahmet","mehmet","tuğrul"]
print(a.index("ahmet"))
"""
#i ve e harfini kaldırmıyor
"""
def sesli_harf_kaldıran(cümle):
    yeni_dizi = ""
    sesli_harfler = ("a", "e", "ı", "i", "o","ö", "u", "ü")
    for x in cümle.lower():
        if x in sesli_harfler:
            yeni_dizi = cümle.replace(x,"")
    return yeni_dizi

print(sesli_harf_kaldıran("ismail aslan merhaba"))
"""
"""
def anti_sesli(text):
    for i in "a, e, ı, i, o, ö, u, ü":
        text = text.replace(i , "")
    return text
   
print(anti_sesli("ismail aslan nasılsın")) 
"""


def sesli_kaldir(cumle):
    sesliHarfler = "aeıioöuüAEIİOÖUÜ"
    yeni = ""
    for i in cumle:
        if i not in sesliHarfler:
            yeni += i
    return yeni

print(sesli_kaldir("bakalım olmuş mu ne çıkacak"))        
    
       
        
        
        
        
    
       
   
    
     
    