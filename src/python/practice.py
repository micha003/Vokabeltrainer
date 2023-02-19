# Skript, was die Abfrage der KK's durchführt
# importiert Module
import core as c
import importKK as iK
import random as r

# Definiert eine Funktion getQueriedSet(), die als Parameter ein Dictionary mit allen Sets bekommt
def getQueriedSet(allSets: dict):
    # Erstellt eine Variable chosenSetName, die als zugewiesenen Wert eine Benutzereingabe (String) bekommt
    chosenSetName = input("Bitte wählen Sie ein importiertes Set aus: ")

    # Erstellt eine Liste mit allen Keys aus dem Dictionary allSets
    allKeys = []
    for key in allSets:
        allKeys.append(key)

    # Wenn der eingegebene Key nicht in der Liste allKeys ist, wird eine Fehlermeldung ausgegeben und eine Dauerschleife gestartet
    if chosenSetName not in allKeys:
        while True:
            print("Dieses Set wurde nicht importiert. Wenn Sie dies nachträglich tun wollen, dann geben Sie 'import()' ein.")
            # Erstellt eine Variable chosenSetName, die als zugewiesenen Wert eine Benutzereingabe (String) bekommt
            chosenSetName = input("Bitte wählen Sie ein importiertes Set aus: ")
            # Wenn der eingegebene Key in der Liste allKeys ist, wird die Schleife beendet
            if chosenSetName in allKeys:
                break
            # wenn der eingegebene Key "import()" ist, wird man in die main.py weitergeleitet
            elif chosenSetName == "import()":
                return
            else:
                continue
    else:
        pass

    # Erstellt eine Variable chosenSet, die als zugewiesenen Wert den Wert des Keys chosenSetName aus dem Dictionary allSets bekommt
    chosenSet = allSets[chosenSetName]
    # Gibt die Variable chosenSet zurück
    return chosenSet

# Definiert eine Funktion Querry(), die als Parameter ein Dictionary mit allen Sets bekommt
def Querry(allSets: dict):
    # Erstellt eine Variable chosenSet, die als zugewiesenen Wert die Funktion getQueriedSet() bekommt
    chosenSet = getQueriedSet(allSets)
    
    print("Hinweis: Wenn Sie die Antwort nicht wissen, geben Sie 'idk()' ein.")
    # Wenn chosenSet den Wert None hat, wird die Funktion beendet
    if chosenSet == None:
        return
    else:
        pass

    # Erstellt eine Liste mit allen Indezes des chosenSets
    indexes = []
    # Erstellt eine Schleife, die von 0 bis zur Länge des chosenSets geht
    for i in range(len(chosenSet)):
        # Fügt die Variable i in die Liste indexes ein
        indexes.append(i)

    # Mischt die Liste indexes
    r.shuffle(indexes)

    # Erstellt eine Variable rightAnswers, die als zugewiesenen Wert 0 bekommt
    rightAnswers = 0
    # Erstellt eine Variable dkAnswers, die als zugewiesenen Wert 0 bekommt
    dkAnswers = 0  # Der abgefragte wusste die Antwort gar nicht
    # Erstellt eine Variable totalAns, die als zugewiesenen Wert die Länge des chosenSets bekommt
    totalAns = len(chosenSet)
    # Erstellt eine Variable falseAnswers, die als zugewiesenen Wert 0 bekommt
    falseAnswers = 0

    # Erstellt eine Schleife, die von 0 bis zur Länge des chosenSets geht
    for a in indexes:
        # Erstellt eine Variable kkV, die als zugewiesenen Wert den ersten Teil des Strings aus dem chosenSet an der Stelle a bekommt
        kkV = chosenSet[a].split(":")[0].strip()
        # Erstellt eine Variable kkR, die als zugewiesenen Wert den zweiten Teil des Strings aus dem chosenSet an der Stelle a bekommt
        kkR = chosenSet[a].split(":")[1].strip()

        # Erstellt eine Variable givenAnswer, die als zugewiesenen Wert eine Benutzereingabe (String) bekommt
        givenAnswer = input(f"{kkV}: ").strip()

        # wenn die gegbenen Antwort gleich der richtigen Antwort ist, wird die Variable rightAnswers um 1 erhöht
        if givenAnswer == kkR:
            print("Richtig!")
            c.horizontalLine()
            rightAnswers += 1
        # Wenn der eingegebene Key "idk()" ist, wird die Variable dkAnswers um 1 erhöht
        elif givenAnswer == "idk()":
            dkAnswers += 1
            c.horizontalLine()
        else:
            # Wenn die gegbenen Antwort nicht gleich der richtigen Antwort ist, wird die Variable falseAnswers um 1 erhöht
            print("Leider Falsch!")
            c.horizontalLine()
            falseAnswers += 1

    # Gibt die Anzahl der richtigen, falschen und nicht gewussten Antworten aus
    print(f"""Sie haben von {totalAns} Antworten: \n
                - {rightAnswers} richtig \n  
                - {dkAnswers} wussten Sie nicht \n
                - {falseAnswers} falsch
            """)
    c.horizontalLine()

# Wenn das Skript direkt ausgeführt wird, wird die Funktion Querry() ausgeführt
if __name__ == "__main__":
    AIS = {"Test": ["Hallo:Hello", "Major:Haupt", "Remis:Unentschieden"]}
    Querry(AIS)
