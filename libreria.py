
from libro import Aggiungi
from libro import Prestito
from libro import Riporta
from libro import DisponibilitàLibro
from libro import DisponibilitàLibreria
from libro import LibriOccupati


#prima scelta dell'operazione da fare
print(" ")
print("Buongiorno e benvenuto, quale operazione desidera effettuare oggi sul sito della nostra biblioteca? Digiti i seguenti numeri per eseguire l'operazione corrispondente")

print(" 0 - Finisci programma ")
print(" 1 - Aggiunta libro ")
print(" 2 - Prestito libro ")
print(" 3 - Riporta libro ")
print(" 4 - Vedere la disponibilità di un libro specifico")
print(" 5 - Vedere la disponibilità del nostro database")
print(" 6 - Vedere i nostri libri occupati ")

listaLibri = ["libro1", "libro2", "libro3"]
listaPrestati = ["prestato1", "prestato2", "prestato3"]

scelta = input()

while scelta != "0":

    if scelta == "1" :
        Aggiungi(listaLibri)
        
    elif scelta == "2":
        Prestito(listaLibri, listaPrestati)

    elif scelta == "3":
        Riporta(listaLibri, listaPrestati)

    elif scelta == "4":
        DisponibilitàLibro(listaLibri, listaPrestati)

    elif scelta == "5":
        DisponibilitàLibreria(listaLibri)

    elif scelta == "6":
        LibriOccupati(listaPrestati)

    print(" ")
    #scelte seguenti alla prima
    print(" 0 - Finisci programma ")
    print(" 1 - Aggiunta libro ")
    print(" 2 - Prestito libro ")
    print(" 3 - Riporta libro ")
    print(" 4 - Vedere la disponibilità di un libro specifico")
    print(" 5 - Vedere la disponibilità del nostro database")
    print(" 6 - Vedere i nostri libri occupati ")
    print(" ")
    scelta = input ("Vuole continuare ad operare? Scelga tra queste opzioni riportate sopra: ")


#uscita dal programma
print(" ")
print("Grazie per esser passato, spero le sia piaciuto il servizio. Buona giornata!")
print(" ")
print("Fine programma")

