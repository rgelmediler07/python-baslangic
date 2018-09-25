print("----------------SAYILARIN YERLERİNİ DEĞİŞTİRME-----------------")
sonuc=[]
sayi1=int(input("İlk Sayıyı Gir     ="))
sayi2=int(input("İkinci Sayıyı Gir  ="))
sonuc=[sayi1 , sayi2]
print("1.Sayı ={} \t 2.Sayı ={}".format(sonuc[1] , sonuc[0]))
sayi1 , sayi2 = sayi2 , sayi1
print(sayi1 , sayi2) 
