import string

def main():

    rom = ["M","D","C","L","X","V","I"]

    while True:
        zahl = input("Bitte geben Sie ihre Zahl ein:\n")
    
        if zahl[0] in string.digits:
            umw = 0
        else:
            umw = 1

        for i in zahl:
            if umw == 0:
                if i not in string.digits:
                    umw = 2

            elif umw == 1:
                if i not in rom:
                    umw = 2

            else:
                break

        if umw == 1:
            Römisch(zahl)
            break
        elif umw == 0:
            Lateinisch(zahl)
            break

        print("Ungültige Eingabe!")


def Römisch(zahl):
    
    ausgabe = 0
    zahl = list(zahl)

    while True:
        if zahl[0] == "M":
            zahl.pop(0)
            ausgabe += 1000
        elif zahl[0] == "D":
            zahl.pop(0)
            ausgabe += 500
        elif zahl[0] == "C":
            if zahl[1] == "M":
                zahl.pop(0)
                zahl.pop(0)
                ausgabe += 900
            elif zahl[1] == "D":
                zahl.pop(0)
                zahl.pop(0)
                ausgabe += 400
            else:
                zahl.pop(0)
                ausgabe += 100
        elif zahl[0] == "L":
            zahl.pop(0)
            ausgabe += 50
        elif zahl[0] == "X":
            if zahl[1] == "C":
                zahl.pop(0)
                zahl.pop(0)
                ausgabe += 90
            elif zahl[1] == "L":
                zahl.pop(0)
                zahl.pop(0)
                ausgabe += 40
            else:
                zahl.pop(0)
                ausgabe += 10
        elif zahl[0] == "V":
            zahl.pop(0)
            ausgabe += 5
        else:
            if len(zahl) == 1:
                ausgabe += 1
                break
            elif zahl[1] == "X":
                zahl.pop(0)
                zahl.pop(0)
                ausgabe += 9
            elif zahl[1] == "V":
                zahl.pop(0)
                zahl.pop(0)
                ausgabe += 4
            else:
                zahl.pop(0)
                ausgabe += 1

        if len(zahl) == 0:
            break

    print(ausgabe)

def Lateinisch(zahl):

    zahl = int(zahl)
    ausgabe = ""

    while True:
        if zahl >= 1000:
            zahl -= 1000
            ausgabe += "M"
        elif zahl >= 900:
            zahl -= 900
            ausgabe += "CM"
        else:
            break

    while True:
        if zahl >= 500:
            zahl -= 500
            ausgabe += "D"
        elif zahl >= 400:
            zahl -= 400
            ausgabe += "CD"
        else:
            break        

    while True:
       if zahl >= 100:
            zahl -= 100
            ausgabe += "C"
       elif zahl >= 90:
            zahl -= 90
            ausgabe += "XC"
       else:
            break        

    while True:
       if zahl >= 50:
            zahl -= 50
            ausgabe += "L"
       elif zahl >= 40:
            zahl -= 40
            ausgabe += "XL"
       else:
            break
        
    while True:
       if zahl >= 10:
            zahl -= 10
            ausgabe += "X"
       elif zahl >= 9:
            zahl -= 9
            ausgabe += "IX"
       else:
            break      

    while True:
       if zahl >= 5:
            zahl -= 5
            ausgabe += "V"
       elif zahl >= 4:
            zahl -= 4
            ausgabe += "IV"
       elif zahl >= 1:
           zahl -= 1
           ausgabe += "I"
       else:
           break

    print("Die Zahl in Römischer Schreibweise:")
    print(ausgabe)


if __name__ == "__main__":
    main()
