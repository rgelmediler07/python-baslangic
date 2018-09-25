from math import sqrt
print("-------------------HİPOTENÜS---------------------")
hipotenus=[]
ilkAci=int(input("İLK AÇIYI GİR :"))
ikinciAci=int(input("İKİNCİ AÇIYI GİR :"))
sonuc=(ikinciAci*ikinciAci)+(ilkAci*ilkAci)
hipotenus=[ilkAci , ikinciAci , sqrt(sonuc)]
print("İlk Açınız ={}\tİkinci Açınız ={}\tHipotenüsünüz  ={}".format(hipotenus[0],hipotenus[1],hipotenus[2]))