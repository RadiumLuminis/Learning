
def Selectionsort(liste):
    laenge = len(liste)                                             #Länge des Arrays als Variable speichern                                                        

    for i in range(laenge):                                         #Schleife, die über jedes Element des Arrays einmal drüber läuft
        jMin = i                                                    #Variable, die angibt, dass nur noch der unsortierte Teil des Arrays geprüft werden muss
                                                                    #Sprich: Alles bis i = Sortiert, ab i = Unsortiert
        for j in range(i+1, laenge):                                #Schleife, die den unsortierten Teil der Liste durchläuft
            if liste[j] < liste[jMin]:                              #Prüft, ob das angenommene Minimum auch größer als die geprüfte Zahl ist
                jMin = j                                            #Wenn größer, dann ist die neue geprüfte Zahl jetzt das angenommene Maximun

        if jMin != i:                                               #Prüft, ob Zahlen identisch sind
            liste[i], liste[jMin] = liste[jMin], liste[i]           #Tauscht die Zahlen, sodass die kleinste Zahl nach vorne kommt
            
    print(liste)


def main():
    zahlen = [7, 9, 22, 30, 1, 40, 8, 5, 12, 15, 19, 20, 33, 2, 28, 21, 17, 18, 10, 29, 5, 1, 40, 1, 12, 35, 20, 16, 32, 40, 5, 24, 34, 35, 1, 15, 24, 37, 13, 39]
    Selectionsort(zahlen)

if __name__ == "__main__":
    main()
