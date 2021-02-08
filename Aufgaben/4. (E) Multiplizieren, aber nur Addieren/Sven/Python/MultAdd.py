def eingabe():
    x = True
    while x:
        global eingabe1 
        eingabe1 = input("Bitte geben Sie eine Zahl ein: ")
        if eingabe1.isnumeric():
            break
        print("Nur Zahlen sind erlaubt!")
    while x:
        global eingabe2 
        eingabe2 = input("Bitte geben Sie eine zweite Zahl ein: ")
        if eingabe2.isnumeric():
            break
        print("Nur Zahlen sind erlaubt!")

    return(eingabe1, eingabe2)



def rechnung(e1, e2):
    z = 0
    a = int(eingabe1)
    b = int(eingabe2) +1
    for i in range(1, b):
        z += a
    print("Ihr Ergebnis ist: ", z)


def main():
    eingabe()
    rechnung(eingabe1, eingabe2)





if __name__ == "__main__":
    main()
