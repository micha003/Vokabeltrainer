# Skript, was die Abfrage der KK's durchführt
import core as c
import importKK as iK
import random as r
import time as t


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
    elif chosenSetName == "import()":
        return
    else:
        pass

    chosenSet = allSets[chosenSetName]
    # simple tests
    print(chosenSet)
    print(chosenSetName)
    return chosenSet, chosenSetName

def getQuerriedKK(Set: list, currentIndex: int):
    kkV = Set[currentIndex].split(":")[0]
    kkR = Set[currentIndex].split(":")[1]

    print(Set)
    print(currentIndex)
    print(kkV)
    print(kkR)
    return kkV, kkR


def Querry(allSets):
    value = getQueriedSet(allSets)[0]
    chosenSet = value[0]
    chosenSetName = value[1]

    indizes = [i for i in range(len(chosenSet))]
    # Test
    print(indizes)
    r.shuffle(indizes)
    print(indizes)


    rightAnswers = 0
    dkAnswers = 0  # Der abgefragte wusste die Antwort gar nicht
    totalAns = len(chosenSet)
    falseAnswers = 0


    for a in indizes:
        fullKK = getQuerriedKK(chosenSet, a)
        kkV = fullKK[0]
        kkR = fullKK[1]

        givenAnswer = input(f"{kkV}: ").strip()

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

    statsFile = open(f"{chosenSetName}_stats.csv", "a")
    statsFile.write(
        f"{str(t.strftime('%d.%m.%Y %H:%M'))}, {totalAns}, {rightAnswers}, {dkAnswers}, {falseAnswers}\n")
    statsFile.close()
    c.horizontalLine()


if __name__ == "__main__":
    AIS = {"Test": ["Hallo:Hello", "Major:Haupt", "Remis:Unentschieden"]}
    Querry(AIS)
    #getQueriedSet(AIS)
    getQuerriedKK(AIS["Test"], 1)