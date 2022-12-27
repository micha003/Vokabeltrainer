# Erstellung von KK's und Lernsets

temp = []

def getKK():
    kk_v = input("Vorderseite: ")
    kk_r = input("Rückseite: ")

    return f"{kk_v}: {kk_r} \n"

def getSet():
    inputMode = True

    while inputMode:
        KK = getKK()
        temp.append(KK)

        try:
            finishInput = int(input("1: weitere KKs | 2: weiter zu Export  \n"))
            
            if finishInput == 1 or finishInput == 2:
                pass
            else:
                raise ValueError
        except ValueError: # FIXME: it does execute the commands below, if the input is not 1 or 2
            falseValue = True
            while falseValue:
                print("Bitte geben Sie 1 oder 2 ein!")
                try:
                    finishInput = int(input("1: weitere KKs | 2: weiter zu Export \n")) 
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

# TODO: Disallow empty entries