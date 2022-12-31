# Importieren von Lernsets
import core as c
import os


def importSet(importedSets):
    print("Stellen Sie sicher, dass das Lernset in diesem Verzeichnis abgelegt ist!")
    setname = input("Bitte geben Sie den Namen des Sets ein: ")
    setname = setname + ".txt"

    os.chdir(c.workspace)

    importedSet = open(setname, "r")
    importedKK = importedSet.read().split("\n")
    # Löscht den letzten Eintrag der Liste
    del importedKK[-1]

    importedSets[setname.replace(".txt", "")] = importedKK


if __name__ == "__main__":
    test = {}
    importSet(test)
