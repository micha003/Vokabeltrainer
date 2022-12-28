# Importieren von Lernsets
import core as c


def importSet(importedSets):
    print("Stellen Sie sicher, dass das Lernset in diesem Verzeichnis abgelegt ist!")
    setname = input("Bitte geben Sie den Namen des Sets ein: ")
    setname = setname + ".txt"
    # TODO: delete the print-statement
    print(setname)

    importedSet = open(setname, "r")
    importedKK = importedSet.read().split("\n")
    # Löscht den letzten Eintrag der Liste
    del importedKK[-1]

    print(importedKK)

    importedSets[setname.replace(".txt", " ")] = importedKK
    print(importedSets)


if __name__ == "__main__":
    test = {}
    importSet(test)
