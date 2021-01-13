#Lösungdauer: Knapp 2 Stunden

def main():
    x = 1
    while x != 0:                                                       #Kurzer Loop, der wiederholt, wenn keine ganze Zahl
        global zahl                                                     #Globalität der Zahl außerhalb des Loops
        zahl = float(input("Geben Sie eine ganze Zahl ein: "))          #Eingabe einer Zahl        
        z = int(zahl)                                                   #Neue Variable, aber ohne Kommastellen
        b = zahl - z                                                    #Neue Variable, nur Kommastellen
        if b != 0:                                                      #Prüfen, ob Kommastellen = 0
            zahl = float(input("Geben Sie eine GANZE Zahl ein: "))      #Aufforderung zur Neueingabe, wenn nicht
            continue                                                    #Spring an Loop-Anfang, wenn nicht
        x -= 1                                                          #Beenden des Loop
    end = int(zahl/2+1)                                                 #Neue Variable, Hälfte der Eingabe +1  
    for i in range(2, end):                                             #Loop, zählt von 2 bis Hälfte der Eingabe
        if zahl%i == 0:                                                 #Immer, wenn die Zahl durch Zähler teilbar:
            print(i)                                                    #Gebe den Zähler aus
    

if __name__ == "__main__":                                              #Prüfen, ob das Programm kein Mist ist
    main()                                                              #Dann main() ausführen