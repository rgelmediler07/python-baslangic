print("--------------ARAÇ YAKIT MALİYETİNİ HESAPLAMA--------------------")
arac=[]
kmBasiYakit=float(input("ARACINIZ KM BAŞI NE KADAR YAKIYOR (TL CİNSİNDEN) ="))
kmGidis=float(input("KAÇ KM GİTTİNİZ ="))
sonuc=kmBasiYakit*kmGidis
arac=[kmBasiYakit , kmGidis , sonuc]
print("ARACINIZIN KM YAKTIĞI YAKIT ={} ₺ \t ARACINIZ KATTETİĞİ KM ={}km \t TOPLAM MALİYETİNİZ ={} ₺".format(arac[0] , arac[1] , arac[2]))