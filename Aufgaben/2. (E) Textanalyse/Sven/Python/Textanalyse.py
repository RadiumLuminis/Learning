#Programm zur Analyse der Zeichenhäufigkeit eines Textes

#Eingabe und Aufteilung in Array

def Eingabe():
    txt = input("Geben Sie hier ihren Text ein:\n")
    txtlist = list(txt.upper())
    return txtlist

def Sortieren(txtlist):                           #Sortierverfahren nach Bubblesort, man könnte auch list.sort() verwenden
    länge = len(txtlist)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, länge):
            if txtlist[-i][1] > txtlist[-i-1][1]:
                txtlist[-i], txtlist[-i-1] = txtlist[-i-1], txtlist[-i]
                swapped = True
    return txtlist

def Umwandeln_Zählen(txtlist):
    Ergebnis = []
    i = 0
    while True:
        if len(txtlist) == 0:
            break
        Ergebnis.append([txtlist[0], txtlist.count(txtlist[0])])
        Bs = txtlist[0]
        Vk = txtlist.count(txtlist[0])
        for a in range(Vk):
            txtlist.remove(Bs)
        txtlist = list(txtlist)
        i += 1
        

    #print(Ergebnis)   
    return Ergebnis

def main():
    txtlist = Eingabe()
    txtlist = Umwandeln_Zählen(txtlist)
    txtlist = Sortieren(txtlist)

    #Ausgabe
    for i in range(len(txtlist)):

        print(txtlist[i][0], " kommt im Text ", txtlist[i][1], " Mal vor")
    
        

if __name__ == "__main__":
    main()