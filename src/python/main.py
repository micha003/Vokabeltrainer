# Vokabeltrainer

# importiert alle Module
import core as c
import createKK as cK
import importKK as iK
import practice as pra

# Erstellt ein Dictionary, wo alle importieten Sets gespeichert werden
allImportedSets = {}


def printStartpage():
    c.horizontalLine()
    print("Willkommen zu Michaels Vokabeltrainer!")
    print("Wenn Sie eine Übersicht aller Befehle haben wollen, dann geben Sie -help ein.")
    c.horizontalLine()


def printHelp():
    # Übersicht über alle Befehle
    print("""
    -help: zeigt alle Befehle an \n
    -create: erstellt ein neues Lernset \n
    -import: importiert ein Lernset \n
    -edit: editiert ein Lernset \n
    -pra: Lernset üben \n
    -xxx: Beendet das Programm
    """)
    c.horizontalLine()

# Erstellt die Funktion main mit dem Parameter AIS (All Imported Sets)


def main(AIS):
    printStartpage()

    while True:
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
