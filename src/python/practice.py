# Skript, was die Abfrage der KK's durchführt
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

    rightAnswers = 0
    dkAnswers = 0  # Der abgefragte wusste die Antwort gar nicht
    totalAns = len(chosenSet)
    falseAnswers = 0

    for a in indizes:
        kkV = getQuerriedKK(chosenSet, a)[0]
        kkR = getQuerriedKK(chosenSet, a)[1]

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

    with open(f"{chosenSetName}_stats.csv", "a") as statsFile:
        statsFile.write(
            f"{str(t.strftime('%d.%m.%Y %H:%M'))}, {totalAns}, {rightAnswers}, {dkAnswers}, {falseAnswers}\n")
        c.horizontalLine()


if __name__ == "__main__":
    AIS = {"Test": ["1:2", "2:1", "3:4", "4:3",
                    "5:6", "6:5", "7:8", "8:7", "9:10", "10:9"]}
    Querry(AIS)
    # getQueriedSet(AIS)
    # getQuerriedKK(AIS["Test"], 1)
