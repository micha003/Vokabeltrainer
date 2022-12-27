# Importieren von Lernsets

def importSet(importedSets):
    print("Stellen Sie sicher, dass das Lernset in diesem Verzeichnis abgelegt ist!")
    setname = input("Bitte geben Sie den Namen des Sets ein: ")
    setname = setname + ".txt"
    print(setname)

    importedSet = open(setname, "r")
    importedKK = importedSet.read().split("\n") 
    # FIXME: Löscht den letzten Eintrag der Liste

    print(importedKK)

    importedSets[setname.replace(".txt", " ")] = importedKK
    print(importedSets)

    

if __name__ == "__main__":
    test = {}
    importSet(test)