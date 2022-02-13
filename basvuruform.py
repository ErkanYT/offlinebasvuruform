print("Basit Başvuru Formu")
#basit bir ofline basvuru formudur
ad = input("Kullanıcı Ad Gir : ")
soyad = input("Kullanıcı Soyad Gir : ")
no = int(input("Telefon No Gir : "))

bilgiler = [ad,soyad,no]

print("Ad: {} \nSoyad: {} \nNumaran: {}".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("Bilgiler Kaydedildi...")

#pwd by erkan