
#mi permette di aggiungere un libro alla lista di libri
def Aggiungi (listaLibri):

    aggiuntaLibro = ( input ("Aggiungi il nome del libro: "))

    if aggiuntaLibro in listaLibri:

        print("Libro gia' presente nella lista")

    else: 

        listaLibri.append(aggiuntaLibro)
        print("E' stato aggiunto:'"+ aggiuntaLibro, "alla lista")
    
    print(" ")
    DisponibilitàLibreria(listaLibri)


#mi permette di togliere un libro alla lista di libri e aggioungerlo alla lista degli occupati
def Prestito (listaLibri, listaPrestati):

    prestitoLibro = input ("Quale libro viene dato in prestito? (Aggiungi i dati) ")

    if prestitoLibro in listaLibri:

        listaLibri.remove(prestitoLibro)
        listaPrestati.append(prestitoLibro)

    else:

        print("Libro non presente nella lista")

#mi permette di aggiungere un libro alla lista di libri e toglierlo alla lista degli occupati
def Riporta(listaLibri, listaPrestati):

    riportaLibro = input ("Quale libro è stato riportato? (Aggiungi dati) ")

    if riportaLibro in listaPrestati:

        listaLibri.append(riportaLibro) 
        listaPrestati.remove(riportaLibro)

    else:

        print("Mi sa che hai sbagliato biblioteca.")

#mi permette di vedere la disponibilità di un libro specifico
def DisponibilitàLibro(listaLibri, listaPrestati):

    richiesta = input("Quale libro stai cercando? ")
    
    if richiesta in listaLibri:

        risposta= input(richiesta, "e' disponibile nella nostra biblioteca, vuoi prenderlo in prestito? ")

        if risposta == "Si" or risposta=="si":
            Prestito(listaLibri, listaPrestati)
        elif risposta == "No" or risposta=="no":
            print("D'accordo, buona giornata.")

    elif richiesta in listaPrestati:

        risposta = input ("Il libro e' momentaneamente occupato, mi spiace.")

    else:

        print("Il libro non si trova nel nostro database, mi spiace")

#mi permette di vedere la disponibilità dei nostri libri liberi al momento
def DisponibilitàLibreria(listaLibri):

    #print("I libri disponibili sono: ", listaLibri)
    i = int (1)
    for el in listaLibri:
        print(i, ") ", el)
        i = i +1
    

#mi permette di vedere i nostri libri occupati al momento
def LibriOccupati(listaPrestati):
    
    #print("I libri occupati sono: ", listaPrestati)
    i = int (1)
    for el in listaPrestati:
        print(i, ") ", el)
        i = i +1

#operazioni possibili
def Operazioni(scelta, listaLibri, listaPrestati):
    if scelta == 1 :
        Aggiungi(listaLibri)

    elif scelta == 2:
        Prestito (listaLibri, listaPrestati)

    elif scelta == 3:
        Riporta (listaLibri, listaPrestati)

    elif scelta == 4:
        DisponibilitàLibro (listaLibri, listaPrestati)

    elif scelta == 5:
        DisponibilitàLibreria (listaLibri, listaPrestati)

    elif scelta == 6:
        LibriOccupati (listaPrestati)

