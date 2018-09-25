print("LÜTFEN BELİRTİLEN İŞLEM İÇİN SAYI GİRİNİZ")
print("1-ÇARPMA\t2-TOPLAMA\t3-BÖLME")
sayi=int(input("SAYIYI GİR:"))
if sayi==1:
    print("----------Çarpma İşlemi--------------")
    carpanlar=[]
    ilkCarpan=int(input("İlk Sayıyı Gir     ="))
    ikinciCarpan=int(input("İkinci Carpanı Gir ="))
    ucuncuCarpan=int(input("Üçüncü Çarpanı Gir ="))
    sonuc=ilkCarpan*ikinciCarpan*ucuncuCarpan
    carpanlar=[ilkCarpan , ikinciCarpan , ucuncuCarpan , sonuc]

    print("{} * {} * {} = {}".format(carpanlar[0],carpanlar[1],carpanlar[2] , carpanlar[3]))
elif sayi==2:
    print("----------Toplama İşlemi--------------")
    carpanlar=[]
    ilkCarpan=int(input("İlk Sayıyı Gir     ="))
    ikinciCarpan=int(input("İkinci Sayıyı Gir ="))
    ucuncuCarpan=int(input("Üçüncü Sayıyı Gir ="))
    sonuc=ilkCarpan+ikinciCarpan+ucuncuCarpan
    carpanlar=[ilkCarpan , ikinciCarpan , ucuncuCarpan , sonuc]

    print("{} + {} + {} = {}".format(carpanlar[0],carpanlar[1],carpanlar[2] , carpanlar[3]))
elif sayi==3:
    print("----------Bölme İşlemi--------------")
    carpanlar=[]
    ilkCarpan=int(input("İlk Sayıyı Gir     ="))
    ikinciCarpan=int(input("İkinci Carpanı Gir ="))
    sonuc=ilkCarpan/ikinciCarpan
    carpanlar=[ilkCarpan , ikinciCarpan , sonuc]

    print("{} / {} = {}".format(carpanlar[0],carpanlar[1],carpanlar[2] ))
else:
    print("Geçerli Sayı Girilmedi\nYine Bekleriz")