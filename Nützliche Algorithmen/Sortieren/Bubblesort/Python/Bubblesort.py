## Python program for implementation of Bubble Sort 

def bubbleSort(liste):                                          #Erfordert Eingabe einer Liste aus Zahlen
    laenge = len(liste)                                         #Variable mit Länge der Liste
    swapped = True                                              #Ersatz für eine do-while-Schleife
    while(swapped):                                             #Mach Folgendes solange, bis ich Stopp sage:
        swapped = False                                             #Ich sage zuerst Stopp
        for i in range(laenge-1):                                   #Mache Folgendes, bis die Länge der Liste erreicht ist:
            if liste[i] > liste[i+1]:                                   #Wenn die Zahl größer als die nächste Zahl ist:
                liste[i], liste[i+1] = liste[i+1], liste[i]                 #Tausche die Zahlen
                swapped = True                                              #Und mach dann doch weiter
                                                                #Sprich, wenn nicht getauscht wurde, dann höre auf
    print(liste)                                                #Gib die Liste aus                                                

def main():
    liste = [7, 9, 22, 30, 1, 40, 8, 5, 12, 15, 19, 20, 33, 2, 28, 21, 17, 18, 10, 29, 5, 1, 40, 1, 12, 35, 20, 16, 32, 40, 5, 24, 34, 35, 1, 15, 24, 37, 13, 39]
    bubbleSort(liste)

if __name__ == "__main__":
    main()





