# importiert das modul os (= operating system)
import os

# Definiert eine Funktion horizontalLine(), die eine Trennlinie ausgeben soll
def horizontalLine():
    print("----------------------")

# definiert eine Variable workspace, die als zugewiesenen Wert den aktuellen Arbeitsordner bekommt
workspace = os.getcwd()
