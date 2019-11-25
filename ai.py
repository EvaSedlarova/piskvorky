from random import randrange

def tah_pocitace(pole):
    "Vrátí herní pole se zaznamenaným tahem počítače"
    while True:
        cislo_policka = randrange(20)

        if pole[cislo_policka] == 'o' or pole[cislo_policka] == 'x':
            continue
        else:
            break

    return pole[:cislo_policka] + 'o' + pole[(cislo_policka + 1):]