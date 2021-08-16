import random
import sys
import time
import os

words = []
n = 0
source = "Name Creater.txt"
folderName = "Name Creater"

## -----------------------------------------------------------------
## 5 harfliler
def clear():
    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')

# 5 harfli sesli ile başlayıp sesli ile biten kelime üretir
def create():
    ra = random.randint(0, 7)  # sesli
    ra1 = random.randint(0, 20)  # sessiz

    Ra = random.randint(0, 7)  # sesli
    Ra1 = random.randint(0, 20)  # sessiz

    RRa = random.randint(0, 7)  # sesli

    # Sesli Harfler
    while True:
        if ra == 0:
            # print(ra)
            break
        elif ra == 1:
            # print(ra)
            break
        elif ra == 2:
            # print(ra)
            break
        elif ra == 3:
            # print(ra)
            break
        elif ra == 4:
            # print(ra)
            break
        elif ra == 5:
            # print(ra)
            break
        elif ra == 6:
            # print(ra)
            break
        elif ra == 7:
            # print(ra)
            break
    # Sesli Harfler
    while True:
        if Ra == 0:
            # print(ra)
            break
        elif Ra == 1:
            # print(ra)
            break
        elif Ra == 2:
            # print(ra)
            break
        elif Ra == 3:
            # print(ra)
            break
        elif Ra == 4:
            # print(ra)
            break
        elif Ra == 5:
            # print(ra)
            break
        elif Ra == 6:
            # print(ra)
            break
        elif Ra == 7:
            # print(ra)
            break
    # Sesli Harfler
    while True:
        if RRa == 0:
            # print(ra)
            break
        elif RRa == 1:
            # print(ra)
            break
        elif RRa == 2:
            # print(ra)
            break
        elif RRa == 3:
            # print(ra)
            break
        elif RRa == 4:
            # print(ra)
            break
        elif RRa == 5:
            # print(ra)
            break
        elif RRa == 6:
            # print(ra)
            break
        elif RRa == 7:
            # print(ra)
            break
    # Sessiz Harfler
    while True:
        if ra1 == 0:
            # print(ra1)
            break
        elif ra1 == 1:
            # print(ra1)
            break
        elif ra1 == 2:
            # print(ra1)
            break
        elif ra1 == 3:
            # print(ra1)
            break
        elif ra1 == 4:
            # print(ra1)
            break
        elif ra1 == 5:
            # print(ra1)
            break
        elif ra1 == 6:
            # print(ra1)
            break
        elif ra1 == 7:
            # print(ra1)
            break
        elif ra1 == 8:
            # print(ra1)
            break
        elif ra1 == 9:
            # print(ra1)
            break
        elif ra1 == 10:
            # print(ra1)
            break
        elif ra1 == 11:
            # print(ra1)
            break
        elif ra1 == 12:
            # print(ra1)
            break
        elif ra1 == 13:
            # print(ra1)
            break
        elif ra1 == 14:
            # print(ra1)
            break
        elif ra1 == 15:
            # print(ra1)
            break
        elif ra1 == 16:
            # print(ra1)
            break
        elif ra1 == 17:
            # print(ra1)
            break
        elif ra1 == 18:
            # print(ra1)
            break
        elif ra1 == 19:
            # print(ra1)
            break
        elif ra1 == 20:
            # print(ra1)
            break
    # Sessiz Harfler
    while True:
        if Ra1 == 0:
            # print(ra1)
            break
        elif Ra1 == 1:
            # print(ra1)
            break
        elif Ra1 == 2:
            # print(ra1)
            break
        elif Ra1 == 3:
            # print(ra1)
            break
        elif Ra1 == 4:
            # print(ra1)
            break
        elif Ra1 == 5:
            # print(ra1)
            break
        elif Ra1 == 6:
            # print(ra1)
            break
        elif Ra1 == 7:
            # print(ra1)
            break
        elif Ra1 == 8:
            # print(ra1)
            break
        elif Ra1 == 9:
            # print(ra1)
            break
        elif Ra1 == 10:
            # print(ra1)
            break
        elif Ra1 == 11:
            # print(ra1)
            break
        elif Ra1 == 12:
            # print(ra1)
            break
        elif Ra1 == 13:
            # print(ra1)
            break
        elif Ra1 == 14:
            # print(ra1)
            break
        elif Ra1 == 15:
            # print(ra1)
            break
        elif Ra1 == 16:
            # print(ra1)
            break
        elif Ra1 == 17:
            # print(ra1)
            break
        elif Ra1 == 18:
            # print(ra1)
            break
        elif Ra1 == 19:
            # print(ra1)
            break
        elif Ra1 == 20:
            # print(ra1)
            break

    sesli = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
    sessiz = ["b", "c", "ç", "d", "f", "g", "ğ", "h", "j", "k", "l", "m", "n", "p", "r", "s", "ş", "t", "v", "y", "z"]

    harf = sesli[ra]
    Harf = sesli[Ra]
    HHarf = sesli[RRa]
    harf2 = sessiz[ra1]
    Harf2 = sessiz[Ra1]

    piece = harf + harf2 + Harf + Harf2 + HHarf
    print("\n")
    print("Oluşturulan isim : ", piece)
    words.append(piece)
    print("\n")

    cont = input("Devam etmek için 'Enter', Çıkmak için 'q' tuşuna basın : ")

    if cont == "":
        clear()

    elif cont == "q":
        sys.exit()

    else:
        print("\nLütfen geçerli değer girin!")
        time.sleep(3)
        clear()

# 5 harfli sessiz ile başlayıp sessiz ile biten kelime üretir
def create1():
    ra = random.randint(0, 7)  # sesli
    ra1 = random.randint(0, 20)  # sessiz

    Ra = random.randint(0, 7)  # sesli
    Ra1 = random.randint(0, 20)  # sessiz

    rr = random.randint(0, 20)  # sessiz

    # Sesli Harfler
    while True:
        if ra == 0:
            # print(ra)
            break
        elif ra == 1:
            # print(ra)
            break
        elif ra == 2:
            # print(ra)
            break
        elif ra == 3:
            # print(ra)
            break
        elif ra == 4:
            # print(ra)
            break
        elif ra == 5:
            # print(ra)
            break
        elif ra == 6:
            # print(ra)
            break
        elif ra == 7:
            # print(ra)
            break
    # Sesli Harfler
    while True:
        if Ra == 0:
            # print(ra)
            break
        elif Ra == 1:
            # print(ra)
            break
        elif Ra == 2:
            # print(ra)
            break
        elif Ra == 3:
            # print(ra)
            break
        elif Ra == 4:
            # print(ra)
            break
        elif Ra == 5:
            # print(ra)
            break
        elif Ra == 6:
            # print(ra)
            break
        elif Ra == 7:
            # print(ra)
            break
    # Sessiz Harfler
    while True:
        if ra1 == 0:
            # print(ra1)
            break
        elif ra1 == 1:
            # print(ra1)
            break
        elif ra1 == 2:
            # print(ra1)
            break
        elif ra1 == 3:
            # print(ra1)
            break
        elif ra1 == 4:
            # print(ra1)
            break
        elif ra1 == 5:
            # print(ra1)
            break
        elif ra1 == 6:
            # print(ra1)
            break
        elif ra1 == 7:
            # print(ra1)
            break
        elif ra1 == 8:
            # print(ra1)
            break
        elif ra1 == 9:
            # print(ra1)
            break
        elif ra1 == 10:
            # print(ra1)
            break
        elif ra1 == 11:
            # print(ra1)
            break
        elif ra1 == 12:
            # print(ra1)
            break
        elif ra1 == 13:
            # print(ra1)
            break
        elif ra1 == 14:
            # print(ra1)
            break
        elif ra1 == 15:
            # print(ra1)
            break
        elif ra1 == 16:
            # print(ra1)
            break
        elif ra1 == 17:
            # print(ra1)
            break
        elif ra1 == 18:
            # print(ra1)
            break
        elif ra1 == 19:
            # print(ra1)
            break
        elif ra1 == 20:
            # print(ra1)
            break
    # Sessiz Harfler
    while True:
        if Ra1 == 0:
            # print(ra1)
            break
        elif Ra1 == 1:
            # print(ra1)
            break
        elif Ra1 == 2:
            # print(ra1)
            break
        elif Ra1 == 3:
            # print(ra1)
            break
        elif Ra1 == 4:
            # print(ra1)
            break
        elif Ra1 == 5:
            # print(ra1)
            break
        elif Ra1 == 6:
            # print(ra1)
            break
        elif Ra1 == 7:
            # print(ra1)
            break
        elif Ra1 == 8:
            # print(ra1)
            break
        elif Ra1 == 9:
            # print(ra1)
            break
        elif Ra1 == 10:
            # print(ra1)
            break
        elif Ra1 == 11:
            # print(ra1)
            break
        elif Ra1 == 12:
            # print(ra1)
            break
        elif Ra1 == 13:
            # print(ra1)
            break
        elif Ra1 == 14:
            # print(ra1)
            break
        elif Ra1 == 15:
            # print(ra1)
            break
        elif Ra1 == 16:
            # print(ra1)
            break
        elif Ra1 == 17:
            # print(ra1)
            break
        elif Ra1 == 18:
            # print(ra1)
            break
        elif Ra1 == 19:
            # print(ra1)
            break
        elif Ra1 == 20:
            # print(ra1)
            break
    # Sessiz Harfler
    while True:
        if rr == 0:
            # print(ra1)
            break
        elif rr == 1:
            # print(ra1)
            break
        elif rr == 2:
            # print(ra1)
            break
        elif rr == 3:
            # print(ra1)
            break
        elif rr == 4:
            # print(ra1)
            break
        elif rr == 5:
            # print(ra1)
            break
        elif rr == 6:
            # print(ra1)
            break
        elif rr == 7:
            # print(ra1)
            break
        elif rr == 8:
            # print(ra1)
            break
        elif rr == 9:
            # print(ra1)
            break
        elif rr == 10:
            # print(ra1)
            break
        elif rr == 11:
            # print(ra1)
            break
        elif rr == 12:
            # print(ra1)
            break
        elif rr == 13:
            # print(ra1)
            break
        elif rr == 14:
            # print(ra1)
            break
        elif rr == 15:
            # print(ra1)
            break
        elif rr == 16:
            # print(ra1)
            break
        elif rr == 17:
            # print(ra1)
            break
        elif rr == 18:
            # print(ra1)
            break
        elif rr == 19:
            # print(ra1)
            break
        elif rr == 20:
            # print(ra1)
            break

    sesli = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
    sessiz = ["b", "c", "ç", "d", "f", "g", "ğ", "h", "j", "k", "l", "m", "n", "p", "r", "s", "ş", "t", "v", "y", "z"]

    harf = sesli[ra]  # sesli
    Harf = sesli[Ra]  # sesli
    HHarf = sessiz[rr]  # Sessiz Harfler
    harf2 = sessiz[ra1]  # Sessiz Harfler
    Harf2 = sessiz[Ra1]  # Sessiz Harfler

    piece = HHarf + harf + harf2 + Harf + Harf2
    words.append(piece)

    print("\n")
    print("Oluşturulan isim : ", piece)
    words.append(piece)
    print("\n")

    cont = input("Devam etmek için 'Enter', Çıkmak için 'q' tuşuna basın : ")

    if cont == "":
        clear()

    elif cont == "q":
        sys.exit()

    else:
        print("\nLütfen geçerli değer girin!")
        time.sleep(3)
        clear()

# 5 harfli sesli ile başlayıp sessiz ile biten kelime üretir
def create2():
    ra = random.randint(0, 7)  # sesli
    ra1 = random.randint(0, 20)  # sessiz

    Ra = random.randint(0, 7)  # sesli
    Ra1 = random.randint(0, 20)  # sessiz

    rr = random.randint(0, 7)  # sesli

    # Sesli Harfler
    while True:
        if ra == 0:
            # print(ra)
            break
        elif ra == 1:
            # print(ra)
            break
        elif ra == 2:
            # print(ra)
            break
        elif ra == 3:
            # print(ra)
            break
        elif ra == 4:
            # print(ra)
            break
        elif ra == 5:
            # print(ra)
            break
        elif ra == 6:
            # print(ra)
            break
        elif ra == 7:
            # print(ra)
            break
    # Sesli Harfler
    while True:
        if Ra == 0:
            # print(ra)
            break
        elif Ra == 1:
            # print(ra)
            break
        elif Ra == 2:
            # print(ra)
            break
        elif Ra == 3:
            # print(ra)
            break
        elif Ra == 4:
            # print(ra)
            break
        elif Ra == 5:
            # print(ra)
            break
        elif Ra == 6:
            # print(ra)
            break
        elif Ra == 7:
            # print(ra)
            break
    # Sessiz Harfler
    while True:
        if ra1 == 0:
            # print(ra1)
            break
        elif ra1 == 1:
            # print(ra1)
            break
        elif ra1 == 2:
            # print(ra1)
            break
        elif ra1 == 3:
            # print(ra1)
            break
        elif ra1 == 4:
            # print(ra1)
            break
        elif ra1 == 5:
            # print(ra1)
            break
        elif ra1 == 6:
            # print(ra1)
            break
        elif ra1 == 7:
            # print(ra1)
            break
        elif ra1 == 8:
            # print(ra1)
            break
        elif ra1 == 9:
            # print(ra1)
            break
        elif ra1 == 10:
            # print(ra1)
            break
        elif ra1 == 11:
            # print(ra1)
            break
        elif ra1 == 12:
            # print(ra1)
            break
        elif ra1 == 13:
            # print(ra1)
            break
        elif ra1 == 14:
            # print(ra1)
            break
        elif ra1 == 15:
            # print(ra1)
            break
        elif ra1 == 16:
            # print(ra1)
            break
        elif ra1 == 17:
            # print(ra1)
            break
        elif ra1 == 18:
            # print(ra1)
            break
        elif ra1 == 19:
            # print(ra1)
            break
        elif ra1 == 20:
            # print(ra1)
            break
    # Sessiz Harfler
    while True:
        if Ra1 == 0:
            # print(ra1)
            break
        elif Ra1 == 1:
            # print(ra1)
            break
        elif Ra1 == 2:
            # print(ra1)
            break
        elif Ra1 == 3:
            # print(ra1)
            break
        elif Ra1 == 4:
            # print(ra1)
            break
        elif Ra1 == 5:
            # print(ra1)
            break
        elif Ra1 == 6:
            # print(ra1)
            break
        elif Ra1 == 7:
            # print(ra1)
            break
        elif Ra1 == 8:
            # print(ra1)
            break
        elif Ra1 == 9:
            # print(ra1)
            break
        elif Ra1 == 10:
            # print(ra1)
            break
        elif Ra1 == 11:
            # print(ra1)
            break
        elif Ra1 == 12:
            # print(ra1)
            break
        elif Ra1 == 13:
            # print(ra1)
            break
        elif Ra1 == 14:
            # print(ra1)
            break
        elif Ra1 == 15:
            # print(ra1)
            break
        elif Ra1 == 16:
            # print(ra1)
            break
        elif Ra1 == 17:
            # print(ra1)
            break
        elif Ra1 == 18:
            # print(ra1)
            break
        elif Ra1 == 19:
            # print(ra1)
            break
        elif Ra1 == 20:
            # print(ra1)
            break
    # Sesli Harfler
    while True:
        if rr == 0:
            # print(ra1)
            break
        elif rr == 1:
            # print(ra1)
            break
        elif rr == 2:
            # print(ra1)
            break
        elif rr == 3:
            # print(ra1)
            break
        elif rr == 4:
            # print(ra1)
            break
        elif rr == 5:
            # print(ra1)
            break
        elif rr == 6:
            # print(ra1)
            break
        elif rr == 7:
            # print(ra1)
            break

    sesli = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
    sessiz = ["b", "c", "ç", "d", "f", "g", "ğ", "h", "j", "k", "l", "m", "n", "p", "r", "s", "ş", "t", "v", "y", "z"]

    harf = sesli[ra]  # sesli
    Harf = sesli[Ra]  # sesli
    HHarf = sesli[rr]  # sesli Harfler
    harf2 = sessiz[ra1]  # Sessiz Harfler
    Harf2 = sessiz[Ra1]  # Sessiz Harfler

    piece = HHarf + harf + harf2 + Harf + Harf2
    print("\n")
    print("Oluşturulan isim : ", piece)
    words.append(piece)
    print("\n")

    cont = input("Devam etmek için 'Enter', Çıkmak için 'q' tuşuna basın : ")

    if cont == "":
        clear()

    elif cont == "q":
        sys.exit()

    else:
        print("\nLütfen geçerli değer girin!")
        time.sleep(3)
        clear()

# 5 harfli sessiz ile başlayıp sesli ile biten kelime üretir
def create3():
    ra = random.randint(0, 7)  # sesli
    ra1 = random.randint(0, 20)  # sessiz

    Ra = random.randint(0, 7)  # sesli
    Ra1 = random.randint(0, 7)  # sessiz

    rr = random.randint(0, 20)  # sessiz

    # Sesli Harfler
    while True:
        if ra == 0:
            # print(ra)
            break
        elif ra == 1:
            # print(ra)
            break
        elif ra == 2:
            # print(ra)
            break
        elif ra == 3:
            # print(ra)
            break
        elif ra == 4:
            # print(ra)
            break
        elif ra == 5:
            # print(ra)
            break
        elif ra == 6:
            # print(ra)
            break
        elif ra == 7:
            # print(ra)
            break
    # Sesli Harfler
    while True:
        if Ra == 0:
            # print(ra)
            break
        elif Ra == 1:
            # print(ra)
            break
        elif Ra == 2:
            # print(ra)
            break
        elif Ra == 3:
            # print(ra)
            break
        elif Ra == 4:
            # print(ra)
            break
        elif Ra == 5:
            # print(ra)
            break
        elif Ra == 6:
            # print(ra)
            break
        elif Ra == 7:
            # print(ra)
            break
    # Sessiz Harfler
    while True:
        if ra1 == 0:
            # print(ra1)
            break
        elif ra1 == 1:
            # print(ra1)
            break
        elif ra1 == 2:
            # print(ra1)
            break
        elif ra1 == 3:
            # print(ra1)
            break
        elif ra1 == 4:
            # print(ra1)
            break
        elif ra1 == 5:
            # print(ra1)
            break
        elif ra1 == 6:
            # print(ra1)
            break
        elif ra1 == 7:
            # print(ra1)
            break
        elif ra1 == 8:
            # print(ra1)
            break
        elif ra1 == 9:
            # print(ra1)
            break
        elif ra1 == 10:
            # print(ra1)
            break
        elif ra1 == 11:
            # print(ra1)
            break
        elif ra1 == 12:
            # print(ra1)
            break
        elif ra1 == 13:
            # print(ra1)
            break
        elif ra1 == 14:
            # print(ra1)
            break
        elif ra1 == 15:
            # print(ra1)
            break
        elif ra1 == 16:
            # print(ra1)
            break
        elif ra1 == 17:
            # print(ra1)
            break
        elif ra1 == 18:
            # print(ra1)
            break
        elif ra1 == 19:
            # print(ra1)
            break
        elif ra1 == 20:
            # print(ra1)
            break
    # Sesli Harfler
    while True:
        if Ra1 == 0:
            # print(ra1)
            break
        elif Ra1 == 1:
            # print(ra1)
            break
        elif Ra1 == 2:
            # print(ra1)
            break
        elif Ra1 == 3:
            # print(ra1)
            break
        elif Ra1 == 4:
            # print(ra1)
            break
        elif Ra1 == 5:
            # print(ra1)
            break
        elif Ra1 == 6:
            # print(ra1)
            break
        elif Ra1 == 7:
            # print(ra1)
            break
    # Sessiz Harfler
    while True:
        if rr == 0:
            # print(ra1)
            break
        elif rr == 1:
            # print(ra1)
            break
        elif rr == 2:
            # print(ra1)
            break
        elif rr == 3:
            # print(ra1)
            break
        elif rr == 4:
            # print(ra1)
            break
        elif rr == 5:
            # print(ra1)
            break
        elif rr == 6:
            # print(ra1)
            break
        elif rr == 7:
            # print(ra1)
            break
        elif rr == 8:
            # print(ra1)
            break
        elif rr == 9:
            # print(ra1)
            break
        elif rr == 10:
            # print(ra1)
            break
        elif rr == 11:
            # print(ra1)
            break
        elif rr == 12:
            # print(ra1)
            break
        elif rr == 13:
            # print(ra1)
            break
        elif rr == 14:
            # print(ra1)
            break
        elif rr == 15:
            # print(ra1)
            break
        elif rr == 16:
            # print(ra1)
            break
        elif rr == 17:
            # print(ra1)
            break
        elif rr == 18:
            # print(ra1)
            break
        elif rr == 19:
            # print(ra1)
            break
        elif rr == 20:
            # print(ra1)
            break

    sesli = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
    sessiz = ["b", "c", "ç", "d", "f", "g", "ğ", "h", "j", "k", "l", "m", "n", "p", "r", "s", "ş", "t", "v", "y", "z"]

    harf = sesli[ra]  # sesli
    Harf = sesli[Ra]  # sesli
    HHarf = sessiz[rr]  # sessiz Harfler
    harf2 = sessiz[ra1]  # Sessiz Harfler
    Harf2 = sesli[Ra1]  # Sesli Harfler

    piece = harf2 + harf + HHarf + Harf + Harf2
    print("\n")
    print("Oluşturulan isim : ", piece)
    words.append(piece)
    print("\n")

    cont = input("Devam etmek için 'Enter', Çıkmak için 'q' tuşuna basın : ")

    if cont == "":
        clear()

    elif cont == "q":
        sys.exit()

    else:
        print("\nLütfen geçerli değer girin!")
        time.sleep(3)
        clear()

## -----------------------------------------------------------------
## 6 harfliler

# 6 harfli sesli ile başlayıp sesli ile biten kelime üretir
def create4():
    ra = random.randint(0, 7)  # sesli
    ra1 = random.randint(0, 20)  # sessiz

    Ra = random.randint(0, 7)  # sesli
    Ra1 = random.randint(0, 20)  # sessiz

    RRa = random.randint(0, 7)  # sesli
    rRa = random.randint(0, 7)  # sesli

    # Sesli Harfler
    while True:
        if ra == 0:
            # print(ra)
            break
        elif ra == 1:
            # print(ra)
            break
        elif ra == 2:
            # print(ra)
            break
        elif ra == 3:
            # print(ra)
            break
        elif ra == 4:
            # print(ra)
            break
        elif ra == 5:
            # print(ra)
            break
        elif ra == 6:
            # print(ra)
            break
        elif ra == 7:
            # print(ra)
            break
    # Sesli Harfler
    while True:
        if Ra == 0:
            # print(ra)
            break
        elif Ra == 1:
            # print(ra)
            break
        elif Ra == 2:
            # print(ra)
            break
        elif Ra == 3:
            # print(ra)
            break
        elif Ra == 4:
            # print(ra)
            break
        elif Ra == 5:
            # print(ra)
            break
        elif Ra == 6:
            # print(ra)
            break
        elif Ra == 7:
            # print(ra)
            break
    # Sesli Harfler
    while True:
        if RRa == 0:
            # print(ra)
            break
        elif RRa == 1:
            # print(ra)
            break
        elif RRa == 2:
            # print(ra)
            break
        elif RRa == 3:
            # print(ra)
            break
        elif RRa == 4:
            # print(ra)
            break
        elif RRa == 5:
            # print(ra)
            break
        elif RRa == 6:
            # print(ra)
            break
        elif RRa == 7:
            # print(ra)
            break
    # Sessiz Harfler
    while True:
        if ra1 == 0:
            # print(ra1)
            break
        elif ra1 == 1:
            # print(ra1)
            break
        elif ra1 == 2:
            # print(ra1)
            break
        elif ra1 == 3:
            # print(ra1)
            break
        elif ra1 == 4:
            # print(ra1)
            break
        elif ra1 == 5:
            # print(ra1)
            break
        elif ra1 == 6:
            # print(ra1)
            break
        elif ra1 == 7:
            # print(ra1)
            break
        elif ra1 == 8:
            # print(ra1)
            break
        elif ra1 == 9:
            # print(ra1)
            break
        elif ra1 == 10:
            # print(ra1)
            break
        elif ra1 == 11:
            # print(ra1)
            break
        elif ra1 == 12:
            # print(ra1)
            break
        elif ra1 == 13:
            # print(ra1)
            break
        elif ra1 == 14:
            # print(ra1)
            break
        elif ra1 == 15:
            # print(ra1)
            break
        elif ra1 == 16:
            # print(ra1)
            break
        elif ra1 == 17:
            # print(ra1)
            break
        elif ra1 == 18:
            # print(ra1)
            break
        elif ra1 == 19:
            # print(ra1)
            break
        elif ra1 == 20:
            # print(ra1)
            break
    # Sessiz Harfler
    while True:
        if Ra1 == 0:
            # print(ra1)
            break
        elif Ra1 == 1:
            # print(ra1)
            break
        elif Ra1 == 2:
            # print(ra1)
            break
        elif Ra1 == 3:
            # print(ra1)
            break
        elif Ra1 == 4:
            # print(ra1)
            break
        elif Ra1 == 5:
            # print(ra1)
            break
        elif Ra1 == 6:
            # print(ra1)
            break
        elif Ra1 == 7:
            # print(ra1)
            break
        elif Ra1 == 8:
            # print(ra1)
            break
        elif Ra1 == 9:
            # print(ra1)
            break
        elif Ra1 == 10:
            # print(ra1)
            break
        elif Ra1 == 11:
            # print(ra1)
            break
        elif Ra1 == 12:
            # print(ra1)
            break
        elif Ra1 == 13:
            # print(ra1)
            break
        elif Ra1 == 14:
            # print(ra1)
            break
        elif Ra1 == 15:
            # print(ra1)
            break
        elif Ra1 == 16:
            # print(ra1)
            break
        elif Ra1 == 17:
            # print(ra1)
            break
        elif Ra1 == 18:
            # print(ra1)
            break
        elif Ra1 == 19:
            # print(ra1)
            break
        elif Ra1 == 20:
            # print(ra1)
            break
    # Sesli Harfler
    while True:
        if rRa == 0:
            # print(ra)
            break
        elif rRa == 1:
            # print(ra)
            break
        elif rRa == 2:
            # print(ra)
            break
        elif rRa == 3:
            # print(ra)
            break
        elif rRa == 4:
            # print(ra)
            break
        elif rRa == 5:
            # print(ra)
            break
        elif rRa == 6:
            # print(ra)
            break
        elif rRa == 7:
            # print(ra)
            break

    sesli = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
    sessiz = ["b", "c", "ç", "d", "f", "g", "ğ", "h", "j", "k", "l", "m", "n", "p", "r", "s", "ş", "t", "v", "y", "z"]

    harf = sesli[ra]
    Harf = sesli[Ra]
    HHarf = sesli[RRa]
    harf2 = sessiz[ra1]
    Harf2 = sessiz[Ra1]
    harf3 = sesli[rRa]

    piece = harf + harf2 + Harf + Harf2 + HHarf + harf3
    print("\n")
    print("Oluşturulan isim : ", piece)
    words.append(piece)
    print("\n")

    cont = input("Devam etmek için 'Enter', Çıkmak için 'q' tuşuna basın : ")

    if cont == "":
        clear()

    elif cont == "q":
        sys.exit()

    else:
        print("\nLütfen geçerli değer girin!")
        time.sleep(3)
        clear()

# 6 harfli sessiz ile başlayıp sessiz ile biten kelime üretir
def create5():
    ra = random.randint(0, 7)  # sesli
    ra1 = random.randint(0, 20)  # sessiz

    Ra = random.randint(0, 7)  # sesli
    Ra1 = random.randint(0, 20)  # sessiz

    rr = random.randint(0, 20)  # sessiz
    rRa = random.randint(0, 20)  # sessiz

    # Sesli Harfler
    while True:
        if ra == 0:
            # print(ra)
            break
        elif ra == 1:
            # print(ra)
            break
        elif ra == 2:
            # print(ra)
            break
        elif ra == 3:
            # print(ra)
            break
        elif ra == 4:
            # print(ra)
            break
        elif ra == 5:
            # print(ra)
            break
        elif ra == 6:
            # print(ra)
            break
        elif ra == 7:
            # print(ra)
            break
    # Sesli Harfler
    while True:
        if Ra == 0:
            # print(ra)
            break
        elif Ra == 1:
            # print(ra)
            break
        elif Ra == 2:
            # print(ra)
            break
        elif Ra == 3:
            # print(ra)
            break
        elif Ra == 4:
            # print(ra)
            break
        elif Ra == 5:
            # print(ra)
            break
        elif Ra == 6:
            # print(ra)
            break
        elif Ra == 7:
            # print(ra)
            break
    # Sessiz Harfler
    while True:
        if ra1 == 0:
            # print(ra1)
            break
        elif ra1 == 1:
            # print(ra1)
            break
        elif ra1 == 2:
            # print(ra1)
            break
        elif ra1 == 3:
            # print(ra1)
            break
        elif ra1 == 4:
            # print(ra1)
            break
        elif ra1 == 5:
            # print(ra1)
            break
        elif ra1 == 6:
            # print(ra1)
            break
        elif ra1 == 7:
            # print(ra1)
            break
        elif ra1 == 8:
            # print(ra1)
            break
        elif ra1 == 9:
            # print(ra1)
            break
        elif ra1 == 10:
            # print(ra1)
            break
        elif ra1 == 11:
            # print(ra1)
            break
        elif ra1 == 12:
            # print(ra1)
            break
        elif ra1 == 13:
            # print(ra1)
            break
        elif ra1 == 14:
            # print(ra1)
            break
        elif ra1 == 15:
            # print(ra1)
            break
        elif ra1 == 16:
            # print(ra1)
            break
        elif ra1 == 17:
            # print(ra1)
            break
        elif ra1 == 18:
            # print(ra1)
            break
        elif ra1 == 19:
            # print(ra1)
            break
        elif ra1 == 20:
            # print(ra1)
            break
    # Sessiz Harfler
    while True:
        if Ra1 == 0:
            # print(ra1)
            break
        elif Ra1 == 1:
            # print(ra1)
            break
        elif Ra1 == 2:
            # print(ra1)
            break
        elif Ra1 == 3:
            # print(ra1)
            break
        elif Ra1 == 4:
            # print(ra1)
            break
        elif Ra1 == 5:
            # print(ra1)
            break
        elif Ra1 == 6:
            # print(ra1)
            break
        elif Ra1 == 7:
            # print(ra1)
            break
        elif Ra1 == 8:
            # print(ra1)
            break
        elif Ra1 == 9:
            # print(ra1)
            break
        elif Ra1 == 10:
            # print(ra1)
            break
        elif Ra1 == 11:
            # print(ra1)
            break
        elif Ra1 == 12:
            # print(ra1)
            break
        elif Ra1 == 13:
            # print(ra1)
            break
        elif Ra1 == 14:
            # print(ra1)
            break
        elif Ra1 == 15:
            # print(ra1)
            break
        elif Ra1 == 16:
            # print(ra1)
            break
        elif Ra1 == 17:
            # print(ra1)
            break
        elif Ra1 == 18:
            # print(ra1)
            break
        elif Ra1 == 19:
            # print(ra1)
            break
        elif Ra1 == 20:
            # print(ra1)
            break
    # Sessiz Harfler
    while True:
        if rr == 0:
            # print(ra1)
            break
        elif rr == 1:
            # print(ra1)
            break
        elif rr == 2:
            # print(ra1)
            break
        elif rr == 3:
            # print(ra1)
            break
        elif rr == 4:
            # print(ra1)
            break
        elif rr == 5:
            # print(ra1)
            break
        elif rr == 6:
            # print(ra1)
            break
        elif rr == 7:
            # print(ra1)
            break
        elif rr == 8:
            # print(ra1)
            break
        elif rr == 9:
            # print(ra1)
            break
        elif rr == 10:
            # print(ra1)
            break
        elif rr == 11:
            # print(ra1)
            break
        elif rr == 12:
            # print(ra1)
            break
        elif rr == 13:
            # print(ra1)
            break
        elif rr == 14:
            # print(ra1)
            break
        elif rr == 15:
            # print(ra1)
            break
        elif rr == 16:
            # print(ra1)
            break
        elif rr == 17:
            # print(ra1)
            break
        elif rr == 18:
            # print(ra1)
            break
        elif rr == 19:
            # print(ra1)
            break
        elif rr == 20:
            # print(ra1)
            break
    # Sessiz Harfler
    while True:
        if rRa == 0:
            # print(ra1)
            break
        elif rRa == 1:
            # print(ra1)
            break
        elif rRa == 2:
            # print(ra1)
            break
        elif rRa == 3:
            # print(ra1)
            break
        elif rRa == 4:
            # print(ra1)
            break
        elif rRa == 5:
            # print(ra1)
            break
        elif rRa == 6:
            # print(ra1)
            break
        elif rRa == 7:
            # print(ra1)
            break
        elif rRa == 8:
            # print(ra1)
            break
        elif rRa == 9:
            # print(ra1)
            break
        elif rRa == 10:
            # print(ra1)
            break
        elif rRa == 11:
            # print(ra1)
            break
        elif rRa == 12:
            # print(ra1)
            break
        elif rRa == 13:
            # print(ra1)
            break
        elif rRa == 14:
            # print(ra1)
            break
        elif rRa == 15:
            # print(ra1)
            break
        elif rRa == 16:
            # print(ra1)
            break
        elif rRa == 17:
            # print(ra1)
            break
        elif rRa == 18:
            # print(ra1)
            break
        elif rRa == 19:
            # print(ra1)
            break
        elif rRa == 20:
            # print(ra1)
            break

    sesli = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
    sessiz = ["b", "c", "ç", "d", "f", "g", "ğ", "h", "j", "k", "l", "m", "n", "p", "r", "s", "ş", "t", "v", "y", "z"]

    harf = sesli[ra]  # sesli
    Harf = sesli[Ra]  # sesli
    HHarf = sessiz[rr]  # Sessiz Harfler
    harf2 = sessiz[ra1]  # Sessiz Harfler
    Harf2 = sessiz[Ra1]  # Sessiz Harfler
    harf3 = sessiz[rRa]  # sessiz

    piece = HHarf + harf + harf2 + Harf + Harf2 + harf3
    print("\n")
    print("Oluşturulan isim : ", piece)
    words.append(piece)
    print("\n")

    cont = input("Devam etmek için 'Enter', Çıkmak için 'q' tuşuna basın : ")

    if cont == "":
        clear()

    elif cont == "q":
        sys.exit()

    else:
        print("\nLütfen geçerli değer girin!")
        time.sleep(3)
        clear()

# 6 harfli sesli ile başlayıp sessiz ile biten kelime üretir
def create6():
    ra = random.randint(0, 7)  # sesli
    ra1 = random.randint(0, 20)  # sessiz

    Ra = random.randint(0, 7)  # sesli
    Ra1 = random.randint(0, 20)  # sessiz

    rr = random.randint(0, 7)  # sesli
    rRa = random.randint(0, 20)  # sessiz

    # Sesli Harfler
    while True:
        if ra == 0:
            # print(ra)
            break
        elif ra == 1:
            # print(ra)
            break
        elif ra == 2:
            # print(ra)
            break
        elif ra == 3:
            # print(ra)
            break
        elif ra == 4:
            # print(ra)
            break
        elif ra == 5:
            # print(ra)
            break
        elif ra == 6:
            # print(ra)
            break
        elif ra == 7:
            # print(ra)
            break
    # Sesli Harfler
    while True:
        if Ra == 0:
            # print(ra)
            break
        elif Ra == 1:
            # print(ra)
            break
        elif Ra == 2:
            # print(ra)
            break
        elif Ra == 3:
            # print(ra)
            break
        elif Ra == 4:
            # print(ra)
            break
        elif Ra == 5:
            # print(ra)
            break
        elif Ra == 6:
            # print(ra)
            break
        elif Ra == 7:
            # print(ra)
            break
    # Sessiz Harfler
    while True:
        if ra1 == 0:
            # print(ra1)
            break
        elif ra1 == 1:
            # print(ra1)
            break
        elif ra1 == 2:
            # print(ra1)
            break
        elif ra1 == 3:
            # print(ra1)
            break
        elif ra1 == 4:
            # print(ra1)
            break
        elif ra1 == 5:
            # print(ra1)
            break
        elif ra1 == 6:
            # print(ra1)
            break
        elif ra1 == 7:
            # print(ra1)
            break
        elif ra1 == 8:
            # print(ra1)
            break
        elif ra1 == 9:
            # print(ra1)
            break
        elif ra1 == 10:
            # print(ra1)
            break
        elif ra1 == 11:
            # print(ra1)
            break
        elif ra1 == 12:
            # print(ra1)
            break
        elif ra1 == 13:
            # print(ra1)
            break
        elif ra1 == 14:
            # print(ra1)
            break
        elif ra1 == 15:
            # print(ra1)
            break
        elif ra1 == 16:
            # print(ra1)
            break
        elif ra1 == 17:
            # print(ra1)
            break
        elif ra1 == 18:
            # print(ra1)
            break
        elif ra1 == 19:
            # print(ra1)
            break
        elif ra1 == 20:
            # print(ra1)
            break
    # Sessiz Harfler
    while True:
        if Ra1 == 0:
            # print(ra1)
            break
        elif Ra1 == 1:
            # print(ra1)
            break
        elif Ra1 == 2:
            # print(ra1)
            break
        elif Ra1 == 3:
            # print(ra1)
            break
        elif Ra1 == 4:
            # print(ra1)
            break
        elif Ra1 == 5:
            # print(ra1)
            break
        elif Ra1 == 6:
            # print(ra1)
            break
        elif Ra1 == 7:
            # print(ra1)
            break
        elif Ra1 == 8:
            # print(ra1)
            break
        elif Ra1 == 9:
            # print(ra1)
            break
        elif Ra1 == 10:
            # print(ra1)
            break
        elif Ra1 == 11:
            # print(ra1)
            break
        elif Ra1 == 12:
            # print(ra1)
            break
        elif Ra1 == 13:
            # print(ra1)
            break
        elif Ra1 == 14:
            # print(ra1)
            break
        elif Ra1 == 15:
            # print(ra1)
            break
        elif Ra1 == 16:
            # print(ra1)
            break
        elif Ra1 == 17:
            # print(ra1)
            break
        elif Ra1 == 18:
            # print(ra1)
            break
        elif Ra1 == 19:
            # print(ra1)
            break
        elif Ra1 == 20:
            # print(ra1)
            break
    # Sesli Harfler
    while True:
        if rr == 0:
            # print(ra1)
            break
        elif rr == 1:
            # print(ra1)
            break
        elif rr == 2:
            # print(ra1)
            break
        elif rr == 3:
            # print(ra1)
            break
        elif rr == 4:
            # print(ra1)
            break
        elif rr == 5:
            # print(ra1)
            break
        elif rr == 6:
            # print(ra1)
            break
        elif rr == 7:
            # print(ra1)
            break
    # Sessiz Harfler
    while True:
        if rRa == 0:
            # print(ra1)
            break
        elif rRa == 1:
            # print(ra1)
            break
        elif rRa == 2:
            # print(ra1)
            break
        elif rRa == 3:
            # print(ra1)
            break
        elif rRa == 4:
            # print(ra1)
            break
        elif rRa == 5:
            # print(ra1)
            break
        elif rRa == 6:
            # print(ra1)
            break
        elif rRa == 7:
            # print(ra1)
            break
        elif rRa == 8:
            # print(ra1)
            break
        elif rRa == 9:
            # print(ra1)
            break
        elif rRa == 10:
            # print(ra1)
            break
        elif rRa == 11:
            # print(ra1)
            break
        elif rRa == 12:
            # print(ra1)
            break
        elif rRa == 13:
            # print(ra1)
            break
        elif rRa == 14:
            # print(ra1)
            break
        elif rRa == 15:
            # print(ra1)
            break
        elif rRa == 16:
            # print(ra1)
            break
        elif rRa == 17:
            # print(ra1)
            break
        elif rRa == 18:
            # print(ra1)
            break
        elif rRa == 19:
            # print(ra1)
            break
        elif rRa == 20:
            # print(ra1)
            break

    sesli = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
    sessiz = ["b", "c", "ç", "d", "f", "g", "ğ", "h", "j", "k", "l", "m", "n", "p", "r", "s", "ş", "t", "v", "y", "z"]

    harf = sesli[ra]  # sesli
    Harf = sesli[Ra]  # sesli
    HHarf = sesli[rr]  # sesli Harfler
    harf2 = sessiz[ra1]  # Sessiz Harfler
    Harf2 = sessiz[Ra1]  # Sessiz Harfler
    harf3 = sessiz[rRa]  # sessiz

    piece = HHarf + harf2 + Harf + Harf2 + harf + harf3
    print("\n")
    print("Oluşturulan isim : ", piece)
    words.append(piece)
    print("\n")

    cont = input("Devam etmek için 'Enter', Çıkmak için 'q' tuşuna basın : ")

    if cont == "":
        clear()

    elif cont == "q":
        sys.exit()

    else:
        print("\nLütfen geçerli değer girin!")
        time.sleep(3)
        clear()

# 6 harfli sessiz ile başlayıp sesli ile biten kelime üretir
def create7():
    ra = random.randint(0, 7)  # sesli
    ra1 = random.randint(0, 20)  # sessiz

    Ra = random.randint(0, 7)  # sesli
    Ra1 = random.randint(0, 20)  # sessiz

    rr = random.randint(0, 20)  # sessiz
    rRa = random.randint(0, 7)  # sessiz

    # Sesli Harfler
    while True:
        if ra == 0:
            # print(ra)
            break
        elif ra == 1:
            # print(ra)
            break
        elif ra == 2:
            # print(ra)
            break
        elif ra == 3:
            # print(ra)
            break
        elif ra == 4:
            # print(ra)
            break
        elif ra == 5:
            # print(ra)
            break
        elif ra == 6:
            # print(ra)
            break
        elif ra == 7:
            # print(ra)
            break
    # Sesli Harfler
    while True:
        if Ra == 0:
            # print(ra)
            break
        elif Ra == 1:
            # print(ra)
            break
        elif Ra == 2:
            # print(ra)
            break
        elif Ra == 3:
            # print(ra)
            break
        elif Ra == 4:
            # print(ra)
            break
        elif Ra == 5:
            # print(ra)
            break
        elif Ra == 6:
            # print(ra)
            break
        elif Ra == 7:
            # print(ra)
            break
    # Sessiz Harfler
    while True:
        if ra1 == 0:
            # print(ra1)
            break
        elif ra1 == 1:
            # print(ra1)
            break
        elif ra1 == 2:
            # print(ra1)
            break
        elif ra1 == 3:
            # print(ra1)
            break
        elif ra1 == 4:
            # print(ra1)
            break
        elif ra1 == 5:
            # print(ra1)
            break
        elif ra1 == 6:
            # print(ra1)
            break
        elif ra1 == 7:
            # print(ra1)
            break
        elif ra1 == 8:
            # print(ra1)
            break
        elif ra1 == 9:
            # print(ra1)
            break
        elif ra1 == 10:
            # print(ra1)
            break
        elif ra1 == 11:
            # print(ra1)
            break
        elif ra1 == 12:
            # print(ra1)
            break
        elif ra1 == 13:
            # print(ra1)
            break
        elif ra1 == 14:
            # print(ra1)
            break
        elif ra1 == 15:
            # print(ra1)
            break
        elif ra1 == 16:
            # print(ra1)
            break
        elif ra1 == 17:
            # print(ra1)
            break
        elif ra1 == 18:
            # print(ra1)
            break
        elif ra1 == 19:
            # print(ra1)
            break
        elif ra1 == 20:
            # print(ra1)
            break
    # Sesli Harfler
    while True:
        if Ra1 == 0:
            # print(ra1)
            break
        elif Ra1 == 1:
            # print(ra1)
            break
        elif Ra1 == 2:
            # print(ra1)
            break
        elif Ra1 == 3:
            # print(ra1)
            break
        elif Ra1 == 4:
            # print(ra1)
            break
        elif Ra1 == 5:
            # print(ra1)
            break
        elif Ra1 == 6:
            # print(ra1)
            break
        elif Ra1 == 7:
            # print(ra1)
            break
        elif Ra1 == 8:
            # print(ra1)
            break
        elif Ra1 == 9:
            # print(ra1)
            break
        elif Ra1 == 10:
            # print(ra1)
            break
        elif Ra1 == 11:
            # print(ra1)
            break
        elif Ra1 == 12:
            # print(ra1)
            break
        elif Ra1 == 13:
            # print(ra1)
            break
        elif Ra1 == 14:
            # print(ra1)
            break
        elif Ra1 == 15:
            # print(ra1)
            break
        elif Ra1 == 16:
            # print(ra1)
            break
        elif Ra1 == 17:
            # print(ra1)
            break
        elif Ra1 == 18:
            # print(ra1)
            break
        elif Ra1 == 19:
            # print(ra1)
            break
        elif Ra1 == 20:
            # print(ra1)
            break
    # Sessiz Harfler
    while True:
        if rr == 0:
            # print(ra1)
            break
        elif rr == 1:
            # print(ra1)
            break
        elif rr == 2:
            # print(ra1)
            break
        elif rr == 3:
            # print(ra1)
            break
        elif rr == 4:
            # print(ra1)
            break
        elif rr == 5:
            # print(ra1)
            break
        elif rr == 6:
            # print(ra1)
            break
        elif rr == 7:
            # print(ra1)
            break
        elif rr == 8:
            # print(ra1)
            break
        elif rr == 9:
            # print(ra1)
            break
        elif rr == 10:
            # print(ra1)
            break
        elif rr == 11:
            # print(ra1)
            break
        elif rr == 12:
            # print(ra1)
            break
        elif rr == 13:
            # print(ra1)
            break
        elif rr == 14:
            # print(ra1)
            break
        elif rr == 15:
            # print(ra1)
            break
        elif rr == 16:
            # print(ra1)
            break
        elif rr == 17:
            # print(ra1)
            break
        elif rr == 18:
            # print(ra1)
            break
        elif rr == 19:
            # print(ra1)
            break
        elif rr == 20:
            # print(ra1)
            break
    # Sessiz Harfler
    while True:
        if rRa == 0:
            # print(ra1)
            break
        elif rRa == 1:
            # print(ra1)
            break
        elif rRa == 2:
            # print(ra1)
            break
        elif rRa == 3:
            # print(ra1)
            break
        elif rRa == 4:
            # print(ra1)
            break
        elif rRa == 5:
            # print(ra1)
            break
        elif rRa == 6:
            # print(ra1)
            break
        elif rRa == 7:
            # print(ra1)
            break

    sesli = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
    sessiz = ["b", "c", "ç", "d", "f", "g", "ğ", "h", "j", "k", "l", "m", "n", "p", "r", "s", "ş", "t", "v", "y", "z"]

    harf = sesli[ra]  # sesli
    Harf = sesli[Ra]  # sesli
    HHarf = sessiz[rr]  # sessiz Harfler
    harf2 = sessiz[ra1]  # Sessiz Harfler
    Harf2 = sessiz[Ra1]  # Sesli Harfler | sessiz yap bir kerede |
    harf3 = sesli[rRa] # sessiz

    piece = harf2 + harf + HHarf + Harf + Harf2 + harf3
    print("\n")
    print("Oluşturulan isim : ", piece)
    words.append(piece)
    print("\n")

    cont = input("Devam etmek için 'Enter', Çıkmak için 'q' tuşuna basın : ")

    if cont == "":
        clear()

    elif cont == "q":
        sys.exit()

    else:
        print("\nLütfen geçerli değer girin!")
        time.sleep(3)
        clear()

while True:
    try:
        how_many = input("Kaç harflik isim oluşturmak istiyorsunuz [5/6] | Çıkmak için q : ")

        if how_many == "5":
            print("""
1-> Sesli ile başlayıp sesli ile bitsin
2-> Sesli ile başlayıp sessiz ile bitsin
3-> Sessiz ile başlayıp sessiz ile bitsin
4-> Sessiz ile başlayıp sesli ile bitsin
""")

            how = int(input("İsim nasıl başlayıp nasıl bitsin? : "))

            if how == 1:
                create()

            elif how == 2:
                create2()

            elif how == 3:
                create1()

            elif how == 4:
                create3()

            else:
                print("\nLütfen 1 ile 4 arasında bir sayı girin!")
                time.sleep(2)
                clear()


        elif how_many == "6":
            print("""
1-> Sesli ile başlayıp sesli ile bitsin
2-> Sessiz ile başlayıp sessiz ile bitsin 
3-> Sesli ile başlayıp sessiz ile bitsin
4-> Sessiz ile başlayıp sesli ile bitsin
""")

            how2 = int(input("İsim nasıl başlayıp nasıl bitsin? : "))

            if how2 == 1:
                create4()

            elif how2 == 2:
                create5()

            elif how2 == 3:
                create6()

            elif how2 == 4:
                create7()

            else:
                print("\nLütfen 1 ile 4 arasında bir sayı girin!")
                time.sleep(2)
                clear()

        elif how_many == "q":
            break

        else:
            print("\nLütfen sadece geçerli rakamlardan birini girin!")
            time.sleep(2)
            clear()
            continue

        for i in words:
            words2 = i

    except ValueError:
        print("\nLütfen geçerli değer girin!")
        time.sleep(2)
        clear()
        continue