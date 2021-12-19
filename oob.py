print("Object Oriented Programming")

class Account:
    def __init__(self, isim,numara,bakiye):
        self.isim = isim
        self.numara = numara
        self.bakiye = int(bakiye)
    def hesapBilgileri(self):
        print("İsim :", self.isim)
        print("Numara :",self.numara)
        print("Bakiye :",self.bakiye)
    def paraCek(self,miktar):
        if (self.bakiye - miktar < 0):
            print("Bakiyeniz yeterli değil...")
        else:
            self.bakiye -= int(miktar)
            print("Yeni bakiye:", self.bakiye)
    def paraYatir(self,miktar):
        self.bakiye += int(miktar)
        print("Yeni bakiye:", self.bakiye)

yenihesap = Account(input("Isim: "),input("Numara: "),input("Bakiye: ") )

c =input("Para yatımak istediğiniz miktarı giriniz: ")

yenihesap.paraYatir(c)
print("Paraniz yatirildiii:)")
yenihesap.hesapBilgileri()

c=input("Yeni hesap açmak ister misiniz?? E/H")
if c == "E":
    hesapbilgisiiste = Account(input("Isim: "),input("Numara: "),input("Bakiye: "))
    hesapbilgisiiste.hesapBilgileri()
else:
    print("Teşekkürler, iyi  günler")
