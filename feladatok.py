import random
import math

def feladat1():
    print("1. feladat")
    """Kérj be 1 páros számot a felhasználótól. Amennyiben nem páros számot ad meg a felhasználó, akkor kérd be újra a számot, addig, amíg páros számot nem ad meg!"""
    szam:int = int(input("Adjon meg egy páros számot: "))
    while not(szam % 2 == 0):
        szam: int = int (input("Ez nem egy páros szám! Adjon meg egy másikat: "))
    print(szam)

def feladat2():
    print("2. feladat")
    """Írass ki a konzolra 13 db  [10, 150] zárt intervallumba eső véletlen számot. Hány 3-mal osztható van közöttük? A kiírás formátuma: „A számok között X db 3-mal osztható van!”"""
    i: int = 0
    oszthato_harommal: int = 0
    while i < 13:
        szam: int = math.floor(random.random()*141+10)
        print(szam, end = " ")
        i += 1
        if szam % 3 == 0:
            oszthato_harommal += 1
    print(" ")
    print(f"A számok között {oszthato_harommal} db 3-mal osztható szám van!")

def feladat3(szoveg:str, N:int):
    print("3. feladat")
    """Írj eljárást, mely paraméterként kap egy text szöveget, és egy N számot. 
    Amennyiben a szöveg rövidebb, mint a megadott N szám, akkor írjuk ki „Nincs N. karakter!”
    Ha hosszabb, akkor a text szövegnek az N. karakterét írjuk ki csupa nagybetűvel 3-szor! 
    """
    
    i:int = 0
    szoveg_hossz: int = int(szoveg)
    while szoveg_hossz < N:
        print("blabla")


def feladat4():
    print("4. feladat")
    """Írj metódust, mely neveket kér a felhasználótól, amíg a @ jelet nem kapja.
    Hány nevet adott meg a felhasználó? 
    A kiírás formája: „A felhasználó 12 nevet adott meg.”
    """
    i:int = 0
    jel: str = "@"
    nevszamok:int = 0
    nevek: str = str(input("Adjon meg egy nevet: "))
    while not(jel in nevek):
         nevek: str = str(input("Adjon meg egy nevet: "))
         i += 1
         nevszamok += 1
    print(f"A felhasználó {nevszamok} nevet adott meg.")

def feladat5():
    print("5. feladat")
    """Szimuláljuk a kő-papír-olló játékot. 
    Írj eljárást, amiben: 
    A felhasználótól bekérjük a tippjét, ami kő/papír/olló lehet. Alakítsd át csupa kisbetűssé a szöveget, majd tárold el a felhasznalo_tippje változóban. 
    Ezután a gép generál egy egész számot [1,3] között.  1- kő, 2- papír – 3 olló. Tárold el a gep_tippje változóban
    Ezután írd ki, hogy ki nyert!
	Ha a két szó ugyanaz, írja ki, hogy Döntetlen. 
	Egyéb esetben azt írja ki, aki győzött!
    ++ Ha valami más szót ad meg a felhasznló  a kő, papír, ollón kívül, akkor kérje be újra!
    """
    i: int = 0
    
    tipp: str = str(input("Adja meg a tippjét: "))
    while not((tipp == "kő") or (tipp == "papír") or (tipp == "olló")):
        tipp: str = str(input("Nem jó! Adja meg a tippjét újra: "))
    gep_tippje: int = math.floor(random.random() * 3 + 1)
    if gep_tippje == 1:
        gep_tipp:str = "kő"
        print("1 - kő")
    elif gep_tippje == 2:
        gep_tipp:str = "papír"
        print("2 - papír")
    elif gep_tippje == 3:
        gep_tipp:str = "olló"
        print("3 - olló")       

