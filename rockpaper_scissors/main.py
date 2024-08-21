import random

def comp_secimi_yap():
    n = random.randint(1, 3)
    if n == 1:
        return "tas"
    elif n == 2:
        return "kagit"
    else:
        return "makas"

skor_kullanici = 0
skor_comp = 0

while True:
    kullanici_tercih = input("Taş, kağıt veya makas? ").lower()

    if kullanici_tercih not in ["taş", "kağıt", "makas"]:
        print("Geçersiz tercih. Lütfen 'taş', 'kağıt' ya da 'makas' giriniz.")
        continue

    comp_tercih = comp_secimi_yap()
    print("Bilgisayar:", comp_tercih)

    if comp_tercih == kullanici_tercih:
        print("Berabere gelindi.")
    elif (comp_tercih == "tas" and kullanici_tercih == "kagit") or \
            (comp_tercih == "kagit" and kullanici_tercih == "makas") or \
            (comp_tercih == "makas" and kullanici_tercih == "tas"):
        skor_kullanici += 1
        print("Siz kazandınız!")
    else:
        skor_comp += 1
        print("Bilgisayar kazandı :( ")

    print(f"Skor - Siz: {skor_kullanici} vs Bilgisayar: {skor_comp}")

    if skor_kullanici == 5 or skor_comp == 5:
        if skor_comp > skor_kullanici:
            print("KAYBETTİNİZ!")
        else:
            print("KAZANDINIZ!!!")
        break