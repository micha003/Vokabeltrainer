# Importieren von Lernsets


def importSet(importedSets):
    os.chdir(os.getcwd())


# Definiert eine Funktion importSet(importedSets), in den Klammern steht ein Parameter
def importSet(importedSets: dict):
# startet eine Dauerschleife
    while True:
        print("Stellen Sie sicher, dass das Lernset in diesem Verzeichnis abgelegt ist!")
        # Erstellt eine Variable setname, die als zugewiesenen Wert eine Benutzereingabe (String) bekommt
        setname = input("Bitte geben Sie den Namen des Sets ein: ")
        # Fügt der Variable setname den String ".txt" hinzu
        setname = setname + ".txt"
        # Versucht die Datei zu öffnen im read-only Modus
        try:
            importedSet = open(setname, "r")
        # Wenn die Datei nicht gefunden wird, wird die Schleife von vorne gestartet
        except FileNotFoundError:
            continue
        
        # Wenn die Datei gefunden wurde, wird die Schleife beendet
        break

    # Erstellt eine Liste, die aus den Zeilen der Datei besteht
    importedKK = importedSet.read().split("\n")

    importedSet.close()
    # Löscht den letzten Eintrag der Liste

    del importedKK[-1]

    # fügt dem Dictionary importedSets ein neues Element hinzu, dessen Schlüssel der Dateiname ist und dessen Wert die Liste mit den Zeilen
    importedSets[setname.replace(".txt", "")] = importedKK

# die Funktion wird nur ausgeführt, wenn das Programm direkt ausgeführt wird
if __name__ == "__main__":
    test = {}
    importSet(test)
