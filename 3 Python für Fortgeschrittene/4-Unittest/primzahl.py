# Modul primzahl.py 

def ist_primzahl(n):
    """ 
    Testet ob eine Zahl eine Primzahl ist. 
    """
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    if ist_primzahl(2) == True and ist_primzahl(6) == False and ist_primzahl(1) == True:
        print("Test fuer Primzahl-Funktion erfolgreich")
    else:
        print("Primzahl-Funktion liefert fehlerhafte Werte")