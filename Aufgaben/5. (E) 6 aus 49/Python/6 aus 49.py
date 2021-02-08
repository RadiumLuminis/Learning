import random

def main():
    eingabe = set()
    print("Bitte geben Sie 6 verschiedene Zahlen ein: ")

    while len(eingabe) != 6:
        x = int(input())
        if x < 1 or x > 49:
            print("Es sind nur Zahlen zwischen 1 und 49 erlaubt!")
        elif x in eingabe:
            print("Keine doppelten Zahlen sind erlaubt!")
        else:
            eingabe.add(x)
            
    print("Sie haben folgende Zahlen eingegeben: ")
    print(", ".join(str(e) for e in eingabe))

    versuche = 0
    dreier = 0
    vierer = 0
    fünfer = 0

    while True:

        versuche += 1
        zahlen = set()

        while len(zahlen) != 6:
            x = random.randint(1, 49)
            if x not in zahlen:
                zahlen.add(x)
        
        länge =  6 - len(eingabe - zahlen)

        if länge == 3:
            dreier += 1
        elif länge == 4:
            vierer += 1
        elif länge == 5:
            fünfer += 1
        elif länge == 6:
            break

    print("Sie haben ", versuche," Versuche gebraucht, um 6 richtige zu bekommen")
    print("Sie haben dabei", dreier," Mal Drei richtige gezogen, ", vierer," Mal Vier richtige gezogen und ", fünfer," Mal Fünf Richtige gezogen")


if __name__ == "__main__":
    main()