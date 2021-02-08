
import string
import random

def ZahlenRaten():

    

    while True:
        Untergrenze = input("Geben Sie eine Untergrenze der zu erratenden Zahl ein:\n")
        Obergrenze = input("Geben Sie eine Obergrenze der zu erratenden Zahl ein:\n")

        try:
            Untergrenze = int(Untergrenze)
            Obergrenze = int(Obergrenze)
            if Obergrenze > Untergrenze:
                break
            else:
                print("Die Obergrenze muss GRÖßER sein!")
        except:
            print("Ungültige Eingabe!")

    print("\nBitte versuchen Sie nun die Zahl zwischen ", Untergrenze, " und ", Obergrenze, " zu erraten")

    z = int(random.randrange(Untergrenze, Obergrenze, 1))
    i = 0
    zahlen = []

    while True:
        i += 1
        if i < 10:
            a = input("Ihr 0"+ str(i) +". Versuch:\n")
        else:
            a = input(str("Ihr "+ str(i) +". Versuch:\n"))

        try:
            if int(a) > Obergrenze or int(a) < Untergrenze:
                print("Der Bereich liegt zwischen ", Untergrenze, " und ", Obergrenze, "!")
            elif int(a) not in zahlen:
                if int(a) == z:
                    break
                zahlen.append(int(a))
                if int(a) > z:
                    print("Die gesuchte Zahl ist kleiner")
                elif int(a) < z:
                    print("Die gesuchte Zahl ist größer")
            else:
                print("Sie haben diese Zahl schon geraten!")
        except:
            print("Ungültige Eingabe!")

    
    print("Sie haben die Zahl erraten, Glückwunsch!")
    print("Sie haben ", i, " Versuche gebraucht")

ZahlenRaten()