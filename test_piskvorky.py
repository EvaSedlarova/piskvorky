import hra
import ai
import pytest
from io import StringIO

@pytest.mark.parametrize('pole, output', [('--------------------', '-'), # prázdné pole
                                          ('--------------------X','-'), # 21 znaků
                                          ('oxoxoxoxoxoxoxoxoxox', '!'), # plné pole
                                          ('oooxxxxoooxxxoooxxxx', 'x')] # při více vítězích vyhraje hráč - funkce vyhodnot to má v ifu první
)

def test_vyhodnot(pole, output):
    # vyhodnot má pouze argument pole, u kterého zjistí, kdo vyhrál, podle toho vrátí x, o, - nebo !
    # odvolává se na funkci stav hry
    # už mě nenapadá jak funkci dále otestovat
    assert hra.vyhodnot(pole) == output

def test_stav_hry_empty():
    # "Vrátí True, pokud jsou tři stejné znaky za sebou a False, pokud ne", má argumenty pole a znak
    assert hra.stav_hry('--------------------', 'x') == False

def test_stav_hry_full():
    # "Vrátí True, pokud jsou tři stejné znaky za sebou a False, pokud ne", má argumenty pole a znak
    assert hra.stav_hry('oxoxoxoxoxoxoxoxoxox', 'x') == False

def test_stav_hry_winner():
    # "Vrátí True, pokud jsou tři stejné znaky za sebou a False, pokud ne", má argumenty pole a znak
    assert hra.stav_hry('oooxxxxoooxxxoooxxxx', 'x') == True

def test_tah_hrace_empty():
    # Vrátí herní pole se symbolem x umístěným na danou pozici podle zadání hráče
    # Zadám pole a políčko, na které chci zadat x
    assert hra.tah_hrace('--------------------', 20) == '-------------------x'

def test_tah_hrace_out_of_bounds():
    # Vrátí herní pole se symbolem x umístěným na danou pozici podle zadání hráče
    # Zadám pole a políčko, na které chci zadat x
    # testuji, co se stane, pokud velikost políčka bude > 20 - jen se x přidá na konec... zajímavé
    assert hra.tah_hrace('--------------------', 233) == '--------------------x'

# zadej_pole ještě moc otestovat neumím kvůli user inputu, ale něco jsem o tom četla, tak to zkusím
# bere to input stávající pole a zeptá se inputem na číslo políčka
inputs = StringIO('19\n')

def test_zadej_pole_empty(monkeypatch):
    monkeypatch.setattr('sys.stdin', inputs)
    assert hra.zadej_pole('--------------------') == 19

# dál opravdu nevím, je tam while cyklus, pokud tam zadám třeba 21 nebo jiný neplatný znak, vrátí se to na začátek cyklu

# čas otestovat tah počítače, ale znovu se dostávám do konců
# výsledek předvídat nemůžu, protože je tam funkce random
# jedině při téměř plném poli
# ale taky mě zajímalo, za by funkce řekla, kdybych jí dala plné pole - nedostalo by se to z funkce while
def test_tah_pocitace():
    assert ai.tah_pocitace('oxoxoxoxoxoxoxoxoxo-') == 'oxoxoxoxoxoxoxoxoxoo'


