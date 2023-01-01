# Skript, was die Abfrage der KK's durchführt
import core as c
import importKK as iK
import random as r


def getQueriedSet(allSets):
    chosenSetName = input("Bitte wählen Sie ein importiertes Set aus: ")

    allKeys = []
    for key in allSets:
        allKeys.append(key)

    if chosenSetName not in allKeys:
        falseSet = True
        while falseSet:
            print("Dieses Set wurde nicht importiert. Wenn Sie dies nachträglich tun wollen, dann geben Sie 'import()' ein.")
            chosenSetName = input(
                "Bitte wählen Sie ein importiertes Set aus: ")

            if chosenSetName in allKeys:
                falseSet = False
            elif chosenSetName == "import()":
                return
            else:
                continue
    else:
        pass

    chosenSet = allSets[chosenSetName]
    return chosenSet


def Querry(allSets):
    chosenSet = getQueriedSet(allSets)
    if chosenSet == None:
        return
    else:
        pass

    indexes = []
    d = len(chosenSet)
    # d steht für duration (Dauer) der for-Schleife nach diesem Comment
    for i in range(d):
        indexes.append(i)

    r.shuffle(indexes)

    rightAnswers = 0
    dkAnswers = 0  # Der abgefragte wusste die Antwort gar nicht
    totalAns = len(chosenSet)
    falseAnswers = 0

    kkV: str()
    kkR: str()
    givenAnswer: str()

    for a in indexes:
        kkV = chosenSet[a].split(":")[0]
        kkR = chosenSet[a].split(":")[1]

        givenAnswer = input(f"{kkV}: ")

        if givenAnswer == kkR:
            print("Richtig!")
            c.horizontalLine()
            rightAnswers += 1
        elif givenAnswer == "idk()":
            dkAnswers += 1
            c.horizontalLine()
        else:
            print("Leider Falsch!")
            c.horizontalLine()
            falseAnswers += 1

    print(f"""Sie haben von {totalAns} Antworten: \n
                - {rightAnswers} richtig \n  
                - {dkAnswers} wussten Sie nicht \n
                - {falseAnswers} falsch
            """)
    c.horizontalLine()


if __name__ == "__main__":
    AIS = {"Test": ["Hallo:Hello", "Major:Haupt", "Remis:Unentschieden"]}
    Querry(AIS)
