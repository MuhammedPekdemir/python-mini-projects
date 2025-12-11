def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b == 0:
        return "Hata!"
    return a / b

def hesap_makinesi():
    print("--- Hesap Makinesi ---")
    print("1 - Toplama")
    print("2 - Cikarma")
    print("3 - Carpma")
    print("4 - Bolme")
    print("0 - Cikis")

    while True:
        secim = input("Islem Seciniz: ")

        if secim == "0":
            print("Program Sonlandirildi")
            break

        if secim not in ["1", "2", "3", "4"]:
            print("Gecersiz secim yaptin.")
            continue

        try:
            a = float(input("1. Sayiyi Giriniz: "))
            b = float(input("2. Sayiyi Giriniz: "))
        except ValueError:
            print("Girdiginiz deger hatali! Lutfen tekrar giriniz!")
            continue

        if secim == "1":
            print("Sonuc:", toplama(a, b))
        elif secim == "2":
            print("Sonuc:", cikarma(a, b))
        elif secim == "3":
            print("Sonuc:", carpma(a, b))
        elif secim == "4":
            print("Sonuc:", bolme(a, b))

if __name__ == "__main__":
    hesap_makinesi()
