
from libro import * #importa tutte le funzioni dal file 'libro'

#prima scelta dell'operazione da fare
print("\nBuongiorno e benvenuto, quale operazione desidera effettuare oggi sul sito della nostra biblioteca? Digiti i seguenti numeri per eseguire l'operazione corrispondente \n\n 0 - Finisci programma \n 1 - Aggiunta libro \n 2 - Prestito libro \n 3 - Riporta libro \n 4 - Vedere la disponibilità di un libro specifico \n 5 - Vedere la disponibilità del nostro database \n 6 - Vedere i nostri libri occupati \n")



listaLibri = ["libro1", "libro2", "libro3"]
listaPrestati = ["prestato1", "prestato2", "prestato3"]

scelta = input() #scegli cosa vuoi fare tramite digitazione di numero in input dall'utente

while scelta != "0": #ciclo di scelta, in modo da continuare a lavorare scegliendo nuovamente un'istruzione

    Operazioni(scelta, listaLibri, listaPrestati) #funzione che permette l'indirizzamento alle singole istruzioni

    #scelte seguenti alla prima
    print("\n 0 - Finisci programma \n 1 - Aggiunta libro \n 2 - Prestito libro \n 3 - Riporta libro \n 4 - Vedere la disponibilità di un libro specifico \n 5 - Vedere la disponibilità del nostro database \n 6 - Vedere i nostri libri occupati \n")
    scelta = input ("Vuole continuare ad operare? Scelga tra queste opzioni riportate sopra: ")


#uscita dal programma

print("\nGrazie per esser passato, spero le sia piaciuto il servizio. Buona giornata!")

print("\n\nFine programma")

