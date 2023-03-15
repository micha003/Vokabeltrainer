# Vokabeltrainer (main-script)

# importiert alle Module
import core as c
import createKK as cK
import importKK as iK
import practice as pra
import os # os = operating system

# Erstellt ein leeres Dictionary, wo alle importieten Sets gespeichert werden
allImportedSets = {}

# Setzt das Arbeitsverzeichnis auf das Verzeichnis, in dem das Programm liegt
os.chdir(c.workspace)

# Definiert eine Funktion printStartpage(), die beim Aufruf folgende Ausgaben macht
def printStartpage():
    c.horizontalLine()
    print("Willkommen zu Michaels Vokabeltrainer!")
    print("Wenn Sie eine Übersicht aller Befehle haben wollen, dann geben Sie -help ein.")
    c.horizontalLine()

# Definiert eine Funktion printHelp()
def printHelp():
    # Übersicht über alle Befehle
    print("""
    -help: zeigt alle Befehle an \n
    -create: erstellt ein neues Lernset \n
    -import: importiert ein Lernset \n
    -pra: Lernset üben \n
    -xxx: Beendet das Programm
    """)
    c.horizontalLine()

# Erstellt die Funktion main mit dem Parameter AIS (All Imported Sets)
def main(AIS: dict):
    # ruft printStartPage() auf
    printStartpage()

    # Beginn einer Dauerschleife
    while True:
        # Erstellt eine Variable command, die als zugewiesenen Wert eine Benutzereingabe (String) bekommt
        command = input(">>> ")
        # Es gibt in Python kein switch-case, deswegen wurden if-statements verwendet
        if command == "-help":
            printHelp()
        elif command == "-create":
            cK.export()
        elif command == "-import":
            iK.importSet(AIS)
        elif command == "-pra":
            pra.Querry(AIS)
        elif command == "-xxx":
            # Beendet das Programm
            exit()
        else:
            continue


# Führt die main-Funktion aus
main(allImportedSets)
