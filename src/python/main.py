# Vokabeltrainer
import core as c
import createKK as cK
import importKK as iK

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
    
    """)

if __name__ == "__main__":
    printStartpage()