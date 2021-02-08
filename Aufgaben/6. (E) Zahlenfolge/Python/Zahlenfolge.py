
def FolgeWandeln(zahlenfolge):
    print(zahlenfolge)
    zf = list(zahlenfolge)

    anzahl = 1
    zeichen = zf[0]
    ausgabe = []

    for i in range(1, len(zf)):
        if zf[i] == zeichen:
            anzahl += 1
        else:
            ausgabe.append(anzahl)
            ausgabe.append(zeichen)
            anzahl = 1
            zeichen = zf[i]
    ausgabe.append(anzahl)
    ausgabe.append(zeichen)

    ausgabe = "".join(str(e) for e in ausgabe)
    
    return ausgabe


def main():
    zf = "122"
    for i in range(14):
        zf = FolgeWandeln(zf)

    print(zf)



if __name__ == "__main__":
    main()
