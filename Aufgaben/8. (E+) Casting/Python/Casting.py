
def ByteCast(int):

    byte = []
    i = 0
    
    while int > 0:
        if 2**i > int:
            byte.append(i-1)
            int -= 2**(i-1)
            i = 0
        else:
            i += 1
    
    #print(byte)
    ausgabe = []
    a = byte[0]

    for z in range(byte[0] + 1):
        if a in byte:
            ausgabe.append(1)
        else:
            ausgabe.append(0)
        a -= 1

    ausgabe = "".join(str(e) for e in ausgabe)

    return ausgabe


def DecCast(int):

    ein = list(int)

    while True:
        if len(ein) > 1:
            if ein[0] == "0":
                ein.pop(0)
            else:
                break
        else:
            break

    ausgabe = 0

    a = len(ein) - 1
    for i in range(len(ein)):
        if ein[-(i+1)] == "1":
            ausgabe += 2**i

    return(ausgabe)

def main():
    while True:
        uw = input("Umwandlung in Dezimal oder Binär? (d / b) :\n")
        if uw == "d" or uw == "b":
            break
        else:
            print("Ungültige Eingabe!")

    while True:
        if uw == "b":
            zahl = input("Geben Sie eine Dezimale Zahl ein: ")
            try:
                zahl = int(zahl)
                break
            except:
                print("Ungültige Eingabe!")
        elif uw == "d":
            zahl = input("Geben Sie eine Binäre Zahl ein: ")
            if "1" not in zahl and "0" not in zahl:
                print("Ungültige Eingabe!")
            else:
                break
    
    if uw == "b":
        zahl = ByteCast(zahl)
        print("Die Zahl in Binär: ", zahl)
    elif uw == "d":
        zahl = DecCast(zahl)
        print("Die Zahl in Dezimal: ", zahl)


if __name__ == "__main__":
    main()
