def main():
    hesap_sahibi = input("Adiniz: ")
    hesap = BankAccount(hesap_sahibi)

    while True:
        secim = input(
            "\nYapmak istediginiz islemi seciniz:\n"
            "1- Para yatir\n"
            "2- Para cek\n"
            "3- Bakiyeyi goster\n"
            "4- Cikis\n"
            "Secim: "
        )

        if secim == "1":
            tutar = int(input("Ne kadar yatirmak istiyorsunuz: "))
            hesap.para_yatir(tutar)

        elif secim == "2":
            tutar = int(input("Ne kadar cekmek istiyorsunuz: "))
            hesap.para_cek(tutar)

        elif secim == "3":
            hesap.bakiye_goster()

        elif secim == "4":
            print("Cikis yapiliyor...")
            break

        else:
            print("Gecersiz secim!")


if __name__ == "__main__":
    main(
