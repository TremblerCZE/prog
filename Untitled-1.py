#!/usr/bin/env python3

import math

def objem_kostka(delka):
    return delka ** 3

def objem_kvadr(delka, sirka, hloubka):
    return delka * sirka * hloubka

def objem_koule(polomer):
    from math import pi 
    return (4/3) * pi * (polomer ** 3)

def obvod_kostka(delka):
    return 12 * delka

def obvod_kvadr(delka, sirka, hloubka):
    return 4 * (delka + sirka + hloubka)

def obvod_koule(polomer):
    from math import pi
    return 2 * pi * polomer

def obvod_obdelnik(delka, delka2):
    return (delka + delka2) * 2

def obvod_ctverec(delka):
    return delka * 4

def obvod_kruznice(polomer):
    from math import pi
    return polomer * 2 * pi

def obsah_obdelnik(delka, delka2):
    return delka * delka2 

def obsah_ctverec(delka):
    return delka * delka

def obsah_kruznice(polomer):
    from math import pi
    return polomer * polomer * pi

while True:
    print("Co chcete počítat?")
    print("1. Objem")
    print("2. Obsah")
    print("3. Obvod")
    
    vyber = input("1 - objem, 2 - obsah, 3 - obvod:")

    teleso = input("jake teleso?\n1 kostka\n2 kvadr\n3 koule\n4 ctverec\n5 obdelnik\n6 kruznice\nzadej:")
    
    vysledek = None
    
    if vyber == '2':
        if teleso == '4':
            delka = float(input("zadej delku:"))
            vysledek = obsah_ctverec(delka)
        elif teleso == '5':
            delka = float(input("zadej delku:"))
            delka2 = float(input("zadej sirku:"))
            vysledek = obsah_obdelnik(delka, delka2)
        elif teleso == '6':
            polomer = float(input("zadej polomer:"))
            vysledek = obsah_kruznice(polomer)
        if vysledek is not None:
            print(f"obsah = {vysledek}")
         
        else:
            print("u těles nepočítáme obsah ale povrch") 
        
   

    if vyber == '1':
        if teleso == '1':
            delka = float(input("zadej delku:"))
            vysledek = objem_kostka(delka)
        elif teleso == '2':
            delka = float(input("zadej delku:"))
            sirka = float(input("zadej sirku:"))
            hloubka = float(input("zadej hloubku:"))
            vysledek = objem_kvadr(delka, sirka, hloubka)
        elif teleso == '3':
            polomer = float(input("zadej polomer:"))
            vysledek = objem_koule(polomer)         
        if vysledek is not None:
            print(f"obsah = {vysledek}")
         
        else:
            print("u rovinných útvarů nepočítáme objem") 
        

    if vyber == '3':
        if teleso == '1':
            delka = float(input("zadej delku:"))
            vysledek = obvod_kostka(delka)
        if teleso == '2':
            delka = float(input("zadej delku:"))
            sirka = float(input("zadej sirku:"))
            hloubka = float(input("zadej hloubku:"))
            vysledek = obvod_kvadr(delka, sirka, hloubka)
        if teleso == '3':
            polomer = float(input("zadej polomer:"))
            vysledek = obvod_koule(polomer) 
        if teleso == '4':
            delka = float(input("zadej delku:"))
            vysledek = obvod_ctverec(delka) 
        if teleso == '5':
            delka = float(input("zadej delku:"))
            delka2 = float(input("zadej sirku:"))
            vysledek = obvod_obdelnik(delka, delka2) 
        if teleso == '6':
            polomer = float(input("zadej polomer:"))
            vysledek = obvod_kruznice(polomer) 
        print(f"obvod = {vysledek}") 
    break