# Importieren von Lernsets
import core as c
import os


def importSet(importedSets):
    os.chdir(os.getcwd())

    while True:
        print("Stellen Sie sicher, dass das Lernset in diesem Verzeichnis abgelegt ist!")
        setname = input("Bitte geben Sie den Namen des Sets ein: ")
        setname = setname + ".txt"

        try:
            importedSet = open(setname, "r")
        except FileNotFoundError:
            continue

        break

    importedKK = importedSet.read().split("\n")
    importedSet.close()
    # Löscht den letzten Eintrag der Liste
    del importedKK[-1]

    importedSets[setname.replace(".txt", "")] = importedKK


if __name__ == "__main__":
    test = {}
    importSet(test)
