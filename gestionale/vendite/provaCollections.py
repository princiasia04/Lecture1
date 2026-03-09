from gestionale.core.prodotti import ProdottoRecord

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