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

    return f"{kk_v}:{kk_r}"


# Definiert eine Funktion getSet(), die keine Parameter hat
def getSet() -> list:
    # startet eine Dauerschleife
    while True:
        # Fügt der Liste temp einen neuen Eintrag hinzu, der aus der Funktion getKK() besteht
        KK = getKK()

        temp.append(KK + "\n")
        # reversed KK
        kk_v = KK.split(":")[1]
        kk_r = KK.split(":")[0]
        temp.append(f"{kk_v}:{kk_r} \n")

        try:
            finishInput = int(
                input("1: weitere KKs | 2: weiter zu Export  \n"))
            c.horizontalLine()

            if finishInput == 1 or finishInput == 2:
                pass
            else:
                raise ValueError
        except ValueError:
            while True:
                print("Bitte geben Sie 1 oder 2 ein!")
                try:
                    finishInput = int(
                        input("1: weitere KKs | 2: weiter zu Export \n"))
                    if finishInput == 1 or finishInput == 2:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    continue

        # Wenn die Eingabe 1 ist, wird die Schleife von vorne gestartet
        if finishInput == 1:
            continue
        elif finishInput == 2:
            # Wenn die Eingabe 2 ist, wird die Schleife beendet, die Liste temp zurückgegeben
            print(temp)
            return temp
        else:
            while True:
                print("Bitte geben Sie 1 oder 2 ein!")
                try:
                    finishInput = int(
                        input("1: weitere KKs | 2: weiter zu Export \n"))
                    if finishInput == 1 or finishInput == 2:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    continue

# Definiert eine Funktion export(), die keine Parameter hat


def export():
    setname = input("Name des Sets: ")
    print("Bitte beachten Sie, dass die dazugehörige .csv-Datei stets im gleichen Verzeichnis abgelegt ist!")
    c.horizontalLine()

    # Erstellt eine Variable lernset, die als zugewiesenen Wert die Liste aus der Funktion getSet() bekommt
    lernset = getSet()
    # Erstellt eine Datei mit dem Namen der Variable setname und dem String ".txt" und fügt die Liste lernset in die Datei ein
    with open(f"{setname}.txt", "w") as newset:
        # startet eine Schleife, die so oft durchläuft, wie die Länge der Liste lernset
        for i in range(len(lernset)):
            # Fügt der Datei newset den Eintrag der Liste lernset hinzu
            newset.write(lernset[i])

    # Erstellt eine Datei für die Statistiken
    setStats = open(f"{setname}_stats.csv", "w")
    setStats.write(
        "Datum & Uhrzeit, Anzahl gesamt, Anzahl Richtig, Anzahl nicht gewusst, Anzahl Falsch \n")
    setStats.close()


# die Funktion wird nur ausgeführt, wenn das Programm direkt ausgeführt wird
if __name__ == "__main__":
    export()

# TODO: das ist irgendwo eine dauerschleife... dringend!!!
