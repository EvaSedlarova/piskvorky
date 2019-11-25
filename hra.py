
# Dnešní projekty jsou součástí projektu 1D Piškvorky. Dělej je jeden po druhém.
# 0. Rozděl 1D Piškvorky na čtyři moduly:
# • ai.py, kde bude funkce tah_pocitace,
# • piskvorky.py, kde budou ostatní funkce,
# • hra.py, kde bude import a volání hlavní funkce z piskvorky.py (a nic jiného),
# • test_piskvorky.py, kde budou testy.
# Připomínám: Až to bude fungovat, dej to do Gitu! A kdybys něco nedopatřením rozbila, git diff HEAD ukáže změny od poslední
# revize.
# 1. Napiš aspoň dva testy na každou funkci z Piškvorek, ke které testy napsat umíš.
# Testy pravděpodobně neumíš napsat na funkci input a všechny funkce, které ji (byť nepřímo) volají. A taky asi neumíš otestovat
# účinek funkce print.
# 2. Zkus program přepsat t
# from random import randrange


#pocitac má hraje s o, hráč s x
from ai import tah_pocitace
      
def tah_hrace(pole, cislo_policka):
    "Vrátí herní pole se symbolem x umístěným na danou pozici podle zadání hráče"
    return pole[:(cislo_policka - 1)] + 'x' + pole[(cislo_policka):]

def zadej_pole(pole):
    "Hráč zadá políčko, na kterém chce hrát"
    while True:
        vstup_uzivatele = input("Zadej číslo pole v rozmezí od 1 do 20: ")
        try:
            cislo_policka = int(vstup_uzivatele)
        except ValueError:
            print("Nejedná se o číslo ve správném formátu")
            continue
        
        if cislo_policka not in range(1, 21, 1):
            print('Nejedná se o číslo v rozmezí 1 - 20')
            continue
        elif pole[cislo_policka - 1] == 'o' or pole[cislo_policka - 1] == 'x':
            print('Na tomto políčku se nemůže hrát.')
            continue
        else:
            break
          
    return cislo_policka
      
def stav_hry(pole, hrac):
    "Vrátí True, pokud jsou tři stejné znaky za sebou a False, pokud ne"
    # stačí mi, když kontroluji do třetího znaku u konce
    for i in range(len(pole) - 2):
        if pole[i] == hrac and pole[i + 1] == hrac and pole[i + 2] == hrac:
            return True
    return False

def vyhodnot(pole):
    "Vrátí, v jakém stavu je pole, jestli někdo vyhrál, zda hra skončila nebo stále pokračuje"
    if stav_hry(pole, 'x'): # vyhrál hráč
        return 'x'
    elif stav_hry(pole, 'o'): #vyhrál počítač
        return 'o'
    elif '-' in pole: #hra pokračuje
        return '-'
    else:
        return '!' #došlo k remíze

def piskvorky1d():
    "Vytvoří řetězec s herním polem a střídavě volá funkce tah_hrace a tah_pocitace, dokud někdo nevyhraje nebo nedojde k remíze"
    pole =  '--------------------'

    while True:

        pole = tah_hrace(pole, zadej_pole(pole))
        print(pole)         
        if not vyhodnot(pole) == '-':
            break

        pole = tah_pocitace(pole)
        print(pole)
        if not vyhodnot(pole) == '-':
            break
       
    if vyhodnot(pole) == 'x':
        print("Vyhrál jsi!")
    elif vyhodnot(pole) == 'o':
        print("Počítač vyhrál!")
    else:
        print("Došlo k remíze!")
 
    return None

