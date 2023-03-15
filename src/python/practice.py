# Skript, was die Abfrage der KK's durchführt
# importiert Module
import core as c
import importKK as iK
import random as r
import time as t


def getQueriedSet(allSets: dict) -> tuple:
    chosenSetName = input("Bitte wählen Sie ein importiertes Set aus: ")

    if chosenSetName in allSets.keys():
        chosenSet = allSets[chosenSetName]
        return chosenSet, chosenSetName
    else:
        while True:
            chosenSetName = input(
                "Bitte wählen Sie ein importiertes Set aus: ")
            if chosenSetName in allSets.keys():
                chosenSet = allSets[chosenSetName]
                return chosenSet, chosenSetName

            else:
                print("Das Set existiert nicht!")



def getQuerriedKK(Set: list, currentIndex: int) -> tuple:
    kkV = Set[currentIndex].split(":")[0]
    kkR = Set[currentIndex].split(":")[1]
    return kkV, kkR


def Querry(allSets: dict):
    value = getQueriedSet(allSets)
    chosenSet = value[0]
    chosenSetName = value[1]

    indizes = [i for i in range(len(chosenSet))]
    r.shuffle(indizes)


    # Erstellt eine Variable rightAnswers, die als zugewiesenen Wert 0 bekommt
    rightAnswers = 0
    # Erstellt eine Variable dkAnswers, die als zugewiesenen Wert 0 bekommt
    dkAnswers = 0  # Der abgefragte wusste die Antwort gar nicht
    # Erstellt eine Variable totalAns, die als zugewiesenen Wert die Länge des chosenSets bekommt
    totalAns = len(chosenSet)
    # Erstellt eine Variable falseAnswers, die als zugewiesenen Wert 0 bekommt
    falseAnswers = 0


    for a in indizes:
        kkV = getQuerriedKK(chosenSet, a)[0]
        kkR = getQuerriedKK(chosenSet, a)[1]


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

    with open(f"{chosenSetName}_stats.csv", "a") as statsFile:
        statsFile.write(
            f"{str(t.strftime('%d.%m.%Y %H:%M'))}, {totalAns}, {rightAnswers}, {dkAnswers}, {falseAnswers}\n")
        c.horizontalLine()

# Wenn das Skript direkt ausgeführt wird, wird die Funktion Querry() ausgeführt
if __name__ == "__main__":
    AIS = {"Test": ["1:2", "2:1", "3:4", "4:3",
                    "5:6", "6:5", "7:8", "8:7", "9:10", "10:9"]}
    Querry(AIS)
    # getQueriedSet(AIS)
    # getQuerriedKK(AIS["Test"], 1)
