def MergeSort(liste):                                       #MergeSort ist kompliziert, guckt euch am besten ein Video an oderlest ein Artikel dazu, ums zu verstehen

    if len(liste) > 1:                                      #Das Programm läuft, solange die Länge der Eingabe größe als 1 ist

        mitte = len(liste)//2                               #Ermitteln der Mitte des eingegebenen Arrays                               
        links = liste[:mitte]                               #Teilen des Arrays in zwei Hälften, Links und Rechts
        rechts = liste[mitte:]

        MergeSort(links)                                    #Programm wird neu ausgeführt, diesmal mit der geteilten Hälfte (Sprich, so oft, wie die Länge größer 1 ist)
        MergeSort(rechts)                                   #Ebenso für die zweite Hälfte

        i=j=k=0                                             #Variabken, um durch die Listen zu Laufen

        while i < len(links) and j < len(rechts):           #Schleife, die läuft, bis entweder links oder rechts die Länge erreicht wurde
            if links[i] < rechts[j]:                        #Prüfen, ob Links Kleiner rechts
                liste[k] = links[i]                             #Dann momentaner Listeneintrag durch Links ersetzen
                i += 1                                          #Und i um eins erhöhen
            else:                                           #Sonst (Sprich Rechts ist kleiner)
                liste[k] = rechts[j]                            #Momentaner Listeneintrag durch Rechts ersetzen
                j += 1                                          #Und j um eins erhöhen    
            k += 1                                          #Immer k um eins erhöhen

        while i < len(links):                               #Wenn Links noch nicht fertig war, dann Links fertig machen
            liste[k] = links[i]
            i += 1
            k += 1

        while j < len(rechts):                              #Wenn Rechts noch nicht fertig war, dann Rechts fertig machen
            liste[k] = rechts[j]
            j += 1
            k += 1



def main():
    zahlen = [7, 9, 22, 30, 1, 40, 8, 5, 12, 15, 19, 20, 33, 2, 28, 21, 17, 18, 10, 29, 5, 1, 40, 1, 12, 35, 20, 16, 32, 40, 5, 24, 34, 35, 1, 15, 24, 37, 13, 39]
    MergeSort(zahlen)
    print(zahlen)

if __name__ == "__main__":
    main()
        
