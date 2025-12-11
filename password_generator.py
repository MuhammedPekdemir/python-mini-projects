import random

sifre_uzunluk = int(input("Istediginiz sifre uzunlugunu giriniz: "))

kucuk_harfler = "abcdefghijklmnopqrstuvwxyz"
buyuk_harfler = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rakamlar = "0123456789"
ozel_karakterler = "!#$@%&?+-*/"

tum_karakterler = kucuk_harfler + buyuk_harfler + rakamlar + ozel_karakterler

sifre = ""
sayac = 0

while sayac < sifre_uzunluk:
    sifre += random.choice(tum_karakterler)
    sayac += 1

print("Uretilen sifre:", sifre)
