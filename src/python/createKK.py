# Erstellung von KK's und Lernsets
import core as c
temp = []


def getKK():
    kk_v = input("Vorderseite: ")

    if kk_v.strip() == "":
        emptyValue = True
        while emptyValue:
            print("Leere Eingabe nicht zulässig!")
            kk_v = input("Vorderseite: ")

            if kk_v.strip == "":
                continue
            else:
                emptyValue = False

    kk_r = input("Rückseite: ")

    if kk_r.strip() == "":
        emptyValue = True
        while emptyValue:
            print("Leere Eingabe nicht zulässig!")
            kk_r = input("Vorderseite: ")

            if kk_r.strip == "":
                continue
            else:
                emptyValue = False

    return f"{kk_v}:{kk_r} \n"


def getSet():
    inputMode = True

    while inputMode:
        KK = getKK()
        temp.append(KK)

        try:
            finishInput = int(
                input("1: weitere KKs | 2: weiter zu Export  \n"))

            if finishInput == 1 or finishInput == 2:
                pass
            else:
                raise ValueError
        except ValueError:
            falseValue = True
            while falseValue:
                print("Bitte geben Sie 1 oder 2 ein!")
                try:
                    finishInput = int(
                        input("1: weitere KKs | 2: weiter zu Export \n"))
                    if finishInput == 1 or finishInput == 2:
                        pass
                    else:
                        raise ValueError
                except ValueError:
                    continue

                falseValue = False

        if finishInput == 1:
            continue
        else:
            print(temp)
            return temp


def export():
    setname = input("Name des Sets: ")
    lernset = getSet()

    newset = open(f"{setname}.txt", "w")

    for i in range(len(lernset)):
        newset.write(lernset[i])

    newset.close()


if __name__ == "__main__":
    export()
