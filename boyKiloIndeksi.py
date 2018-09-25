print("--------------BEDEN KİLO İNDEKSİNİ HESAPLA-----------------\n")
indeks=[]
boy=float(input("Boyunu Gir (metre cinsinden) ="))
kilo=float(input("Kilonu Gir ="))
sonuc=kilo/boy**2
indeks=[boy , kilo , sonuc]
print("Boyun ={}\t Kilon ={}\t İndeksin ={}".format(indeks[0],indeks[1],indeks[2]))
