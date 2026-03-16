from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from collections import Counter
p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20.0)
p3 = ProdottoRecord("Auricolari", 250.0)

carrello = [p1, p2, p3, ProdottoRecord("Tablet", 700.0)]

print("Prodotti nel carrello:")
for i, p in enumerate(carrello):
    print(f"{i}) {p.name} - {p.prezzo_unitario}")

#Aggiungere ad una lista
carrello.append(ProdottoRecord("Monitor", 150.0))

carrello.sort(key = lambda x: x.prezzo_unitario)

print("Prodotti nel carrello:")
for i, p in enumerate(carrello):
    print(f"{i}) {p.name} - {p.prezzo_unitario}")

tot = sum(p.prezzo_unitario for p in carrello)
print(f"Totale del carrelo: {tot}")

#Aggiungere
carrello.append(ProdottoRecord("Propdo", 100.0))
#carrello.sort([ProdottoRecord("aaa", 100.0), ProdottoRecord("bbb", 100.0)])
carrello.insert(2, ProdottoRecord("ccc", 100.0))

#Rimuovere
carrello.pop() #rimuovere l'ultimo elemento
carrello.pop(2) #rimuovere l'elemento in posizione 2
carrello.remove(p1) #elimino la prima occorrenza di p1
#carrello.clear()

#Sorting
#carrello.sort() #ordina seguendo ordinamento naturale
carrello.sort(reverse=True) #ordina al contrario
#carrello.sort(key = function)
carrello_ordinato = sorted(carrello) #nuova lista

#Copie ed altro
carrello.reverse() #inverte l'ordine
carrello_copia = carrello.copy() #shallow copy --> il contenuto è lo stesso
carrello_copia2 = carrello.copy.deepcopy(carrello)  #oggetti di carrello_copia2 distinti da carrello

#Tuple
sede_principale = (45, 8) #lat e long della sede di torino
sede_milano = (45,9) #lat e long della sede di milano

print(f"Sede principale lat: {sede_principale[0]}, long: {sede_principale[1]}")

AliquoteIVA = (
    ("Standard", 0.22),
    ("Ridotta", 0.10),
    ("Alimentari", 0.84),
    ("Esente", 0.0)
)

for descr, valore in AliquoteIVA:
    print(f"{descr} - {valore*100}%")

def calcola_statistiche_carrello (carrello):
    """Restituisce prezzo totale, prezzo medio, massimo e minimo"""
    prezzi = [p.prezzo_unitario for p in carrello]
    return (sum(prezzi), sum(prezzi)/len(prezzi), max(prezzi), min(prezzi))

tot, media, max, min = calcola_statistiche_carrello(carrello) #unpacking elementi

tot, *altri_campi = calcola_statistiche_carrello(carrello)
print(tot)

#Set
categorie = {"Gold", "Silver", "Bronze", "Gold"}
print(categorie)
print(len(categorie))
cateogrie2 = {"Platinum", "Elite", "Gold"}
categorie_all = categorie.union(cateogrie2)
categorie_all2 = categorie | cateogrie2 #unione
print(categorie_all)

categorie_comuni = categorie & cateogrie2 #solo elementi comuni
print(categorie_comuni)

categorie_esclusive = categorie - cateogrie2 #solo gli elementi presenti in uno dei due
print(categorie_esclusive)

categorie_esclusive_simmetriche = categorie ^ cateogrie2 #differenza simmetrica
print(categorie_esclusive_simmetriche)

prodotti_ordine_A = {ProdottoRecord("Laptop", 1200.0),
                     ProdottoRecord("Mouse", 20.0),
                     ProdottoRecord("Tablet", 700.0)}


prodotti_ordine_B = {ProdottoRecord("Laptop2", 1200.0),
                     ProdottoRecord("Mouse2", 20.0),
                     ProdottoRecord("Tablet", 700.0)}

#Metodi utili per i set
s = set()
s1 = set()
s.add(ProdottoRecord("aaa", 20.0)) #aggiungere un elemento
s.update(ProdottoRecord("aaa", 20.0), ProdottoRecord("bbb", 20.0)) #aggiungo più elementi

#Togliere
s.remove(elem) #rimuove un elemento; se non esiste Raise KeyError
s.discard(elem) #rimuove un elemento, senza arrabbiarsi se non esiste
s.pop() #rimuove e restituisce un elemento
s.clear() #svuota il set

#Operazioni insiemistiche
s.union(s1) #s | s1 ovvero genera un set che unisce i due set di partenza
s.intersection(s1) #s & s1 ovvero solo elementi comuni
s.difference(s1) #s - s1 elementi di s che non sono contenuti in s1
s.symmetric_difference(s1) #s ^ s1 ovvero elementi di s non contenuti in s1 e elementi di s1 non contenuti in s
s1.issubset(s) #se gli elementi di s1 sono contenuti in s
s1.issuperset(s) #se gli elementi di s sono contenuti in s1 (sovrainsieme)
s1.isdisjoint(s) #se gli elementi di  s e s1 sono diversi

#Dictionary
catalogo={
    "LAP001" : ProdottoRecord("Laptop",1200),
    "LAP002" : ProdottoRecord("Laptop Pro",2300),
    "MAU001": ProdottoRecord("Mouse",20.0),
    "AUR001": ProdottoRecord("Auricolari",250.0)
}

cod="LAP002"
prod=catalogo[cod]

print(f"Il prodotto con codice {cod} è {prod}")

prod1=catalogo.get("NonEsiste")
if prod1 is None:
    print("Prodotto non trovato")

prod2= catalogo.get("NonEsiste2", ProdottoRecord("Sconosciuto",0)) #se è una frase non presente nel dizionario viene restituito un prodotto che costa 0

keys= list(catalogo.keys())
values= list(catalogo.values())

for k in keys:
    print(k)
for v in values:
    print (v)

for key,value in catalogo.items():
    print(f"Cod {key} è associata a: {value}")

rimosso= catalogo.pop("LAP002")
print(rimosso)

#dict comprehesion
prezzi={codice: prod.prezzo_unitario for codice, prod in catalogo.items()}

#DA RICORDARE PER DICT
"""v= d[Key] # scrivo sul dizionario
v= d[Key]# legge e restituisce key error se non esiste
v= d.get(key,default) #legge senza rischiare keyerror, se non esiste restituisce il default
d.pop(key)#restituisce un valore e lo cancella dal diz
d.clear()#elimina tutto
d.keys() #,i restiusice tutte le chiavi definite nel diz
d.values( )#,mi restituisce tutti i valori salvati nel diz
d.item()#restituisce le coppie
key i  d#condizione che verifica se key è presente nel diz"""


#ESERCIZIO
#per ciascuno dei seguenti casi decidere quale struttura usare

#caso 1: memorizzare una lista di ordini che dovranno essere processati in ordine di arrivo
ordini=[]
o1=Ordine([],ClienteRecord("Mario Rossi","mario@polito.it", "Gold"))
o2=Ordine([],ClienteRecord("Mario Bianchi","mario@polito.it", "Silver"))
o3=Ordine([],ClienteRecord("Fulvio Rossi","mario@polito.it", "Bronze"))
o4=Ordine([],ClienteRecord("Carlo Masone","mario@polito.it", "Gold"))
"""ordini.append(o1,0) #segno l'ordine e il momento di arrivo
ordini.append(o2,10)
ordini.append(o3,3)
ordini.append(o4,45)"""

#caso 2: memorizzare il codici fiscali dei clienti
codici_fiscali={"RMNCHR8922W","GHFNDK77892","KOILLN39909"} #uso un set


#caso 3: creare un database di prodotti che posso cercare con un codice univoco
listino_prodotti= {"LAP001": ProdottoRecord("Laptop",1200.0),"KEY001": ProdottoRecord("Keyboard",20.0)}


#caso 4: memorizzare le cordinate GPS della nuova sede di Roma
magazzino_roma=(45,7) #tupla

#caso 5: tenere traccia delle categorie di clienti che hanno fatto un ordine in un certo range temporale
categorie_perriodo=set()
categorie_perriodo.add("Gold")
categorie_perriodo.add("Bronze")

print("=========================================================")
#COUNTER
lista_clienti=[
    ClienteRecord("Mario Rossi","mario@polito.it", "Gold"),
    ClienteRecord("Mario Bianchi","mario@polito.it", "Silver"),
    ClienteRecord("Fulvio Rossi","mario@polito.it", "Bronze"),
    ClienteRecord("Carlo Masone","mario@polito.it", "Gold"),
    ClienteRecord("Mario Verdi","mario@polito.it", "Gold"),
    ClienteRecord("Chiara Raimondetto","mario@polito.it", "Silver"),
    ClienteRecord("Fulvio Neri","mario@polito.it", "Bronze"),
    ClienteRecord("Carlo Missne","mario@polito.it", "Gold"),
    ClienteRecord("Fulvio Corno","mario@polito.it", "Gold"),
    ]
categorie= [c.categoria for c in lista_clienti]
categorie_counter=Counter(categorie)
print("Distribuzione categorie clienti")
print(categorie_counter)

print("Categoria più frequente:")
print(categorie_counter.most_common(1)) #se volgio le due categorie più frequenti metto 2 al posto di 1

print("totale:")
print(categorie_counter.total())

vendite_gennaio= Counter({"Laptop": 13,"Tablet" : 15})

vendite_febbraio= Counter({"Laptop": 3,"Stampante" : 1})

#Aggregare informazione
vendite_bimestre=vendite_gennaio +vendite_febbraio
print(f"Vendite Gennaio: {vendite_gennaio}")
print(f"Vendite Febbraio: {vendite_febbraio}")
print(f"Vendite bimestre: {vendite_bimestre}")

#fare differenza
print(f"Differenza di vendite: {vendite_gennaio-vendite_febbraio}")

#modificare i valori in the fly
vendite_gennaio["Laptop"]+=4
print(f"Vendite gennaio: {vendite_gennaio}")

#metodi da ricordare
#c.most_common(n)#restituisce fli n elementi più frequenti
#c.total() #somma dei conteggi

#defauldicts
