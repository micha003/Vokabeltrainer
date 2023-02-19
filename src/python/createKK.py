# Erstellung von KK's und Lernsets
# importiert das Modul core
import core as c
# Erstellt eine leere Liste temp
temp = []

# Definiert eine Funktion getKK(), die keine Parameter hat
def getKK() -> str:
    # Erstellt eine Variable kk_v, die als zugewiesenen Wert eine Benutzereingabe (String) bekommt
    kk_v = input("Vorderseite: ")

    # Wenn die Eingabe leer ist, wird eine Fehlermeldung ausgegeben und eine Dauerschleife gestartet
    if kk_v.strip() == "":
        while True:
            print("Leere Eingabe nicht zulässig!")
            kk_v = input("Vorderseite: ")

            if kk_v.strip == "":
                continue
            else:
                break

    # Erstellt eine Variable kk_r, die als zugewiesenen Wert eine Benutzereingabe (String) bekommt
    kk_r = input("Rückseite: ")

    # Wenn die Eingabe leer ist, wird eine Fehlermeldung ausgegeben und eine Dauerschleife gestartet
    if kk_r.strip() == "":
        while True:
            print("Leere Eingabe nicht zulässig!")
            kk_r = input("Vorderseite: ")

            if kk_r.strip == "":
                continue
            else:
                break
    # Gibt die beiden Variablen als String zurück
    return f"{kk_v}:{kk_r} \n"

# Definiert eine Funktion getSet(), die keine Parameter hat
def getSet() -> list:
    # startet eine Dauerschleife
    while True:
        # Fügt der Liste temp einen neuen Eintrag hinzu, der aus der Funktion getKK() besteht
        KK = getKK()
        temp.append(KK)
        # Erstellt eine Variable kk_v, die als zugewiesenen Wert den ersten Teil der Variable KK (Vorderseite) bekommt
        kk_v = KK.split(":")[1]
        kk_r = KK.split(":")[0]
        # Fügt der Liste temp einen neuen Eintrag hinzu, der aus der Funktion getKK() besteht
        temp.append(f"{kk_v}:{kk_r} \n")

        # startet eine Dauerschleife
        while True:
            # Erstellt eine Variable finishInput, die als zugewiesenen Wert eine Benutzereingabe (Integer) bekommt
            try:
                finishInput = int(
                    input("1: weitere KKs | 2: weiter zu Export  \n"))
                c.horizontalLine()
                # Wenn die Eingabe 1 oder 2 ist, wird die Schleife beendet
                if finishInput == 1 or finishInput == 2:
                    break
                else:
                    # Wenn die Eingabe nicht 1 oder 2 ist, wird eine Fehlermeldung ausgegeben und die Schleife von vorne gestartet
                    raise ValueError
            # Wenn die Eingabe keine Zahl ist, wird eine Fehlermeldung ausgegeben und die Schleife von vorne gestartet
            except ValueError:
                    print("Bitte geben Sie 1 oder 2 ein!")
                    continue
        # Wenn die Eingabe 1 ist, wird die Schleife von vorne gestartet
        if finishInput == 1:
            continue
        else:
            # Wenn die Eingabe 2 ist, wird die Schleife beendet, die Liste temp zurückgegeben
            print(temp)
            return temp

# Definiert eine Funktion export(), die keine Parameter hat
def export():
    # Erstellt eine Variable setname, die als zugewiesenen Wert eine Benutzereingabe (String) bekommt
    setname = input("Name des Sets: ")
    c.horizontalLine()
    # Erstellt eine Variable lernset, die als zugewiesenen Wert die Liste aus der Funktion getSet() bekommt
    lernset = getSet()
    # Erstellt eine Datei mit dem Namen der Variable setname und dem String ".txt" und fügt die Liste lernset in die Datei ein
    with open(f"{setname}.txt", "w") as newset:
        # startet eine Schleife, die so oft durchläuft, wie die Länge der Liste lernset
        for i in range(len(lernset)):
            # Fügt der Datei newset den Eintrag der Liste lernset hinzu
            newset.write(lernset[i])

# die Funktion wird nur ausgeführt, wenn das Programm direkt ausgeführt wird
if __name__ == "__main__":
    export()
