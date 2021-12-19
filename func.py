print("Fonksiyonlar Dersi")

def selamla():
    print("Merhaba")
    print("Nasılsın ?")


selamla()
selamla()


def selam(isim="İsimsiz"):
    print("Merhaba", isim)

selam("Murat")
selam()

selam(input("İsiminiz Nedir: "))


def toplama(a,b,c):
    print("Toplam:", a+b+c)

toplama(5,6,7)

a = toplama(5,6,7)
print (a)



def toplam(a,b,c):
    return a+b+c

toplami = toplam(4,5,6)
print(toplami)
