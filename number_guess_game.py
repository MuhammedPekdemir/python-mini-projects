import random

random_number = random.randint(1,100)

print("1 ile 100 arasinda rastgele belirlenmis sayiyi bulunuz.")

tahmin = 0
deneme = 0

while tahmin != random_number:
    tahmin = int(input("\nRastgele sayi tahmini: "))
    deneme += 1

    if tahmin > random_number:
        print("Tahmininiz rastgele secilen sayidan buyuk.")
    elif tahmin < random_number:
        print("Tahmininiz rastgele secilen sayidan kucuk.")
    else:
        print(f"Tebrikler! Tahmininiz dogru. {deneme} denemede bildiniz.")
