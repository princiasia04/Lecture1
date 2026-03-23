#Scrivere un sftware gestionale che abbia le seguenti caratteristiche
#1) supportare l'arrivo e la gestine degli ordini
#1bis) quando arriva un nuovo ordine, lo aggiungo ad una coda, assicurandomi che sia eseguito solo dopo gli altri
#2) avere delle funzionalità per avere statistiche sugli ordini
#3)fornire statistiche sulla distribuzione di ordini per categoria di cliente
from collections import deque, Counter, defaultdict

import self

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine
from main import ordine


class GestoreOrdini:
    def __init__(self):
        self._ordini_da_processare = deque()
        self._ordini_processati = []
        self._statistiche_prodotti = Counter()
        self._ordini_per_categoria = defaultdict(list)

    def add_ordine (self, ordine: Ordine):
        #aggiunge un nuovo ordine agli elementi da gestire
        self._ordini_da_processare.append(ordine)
        print(f"Ricevuto un nuovo ordine da parte di {ordine.cliente}")
        print(f"Ordini ancora da evadere: {len(self._ordini_da_processare)}")

    def crea_ordine(self, nomeP, prezzoP, quantitaP, nomeC, mailC, categoriaC):
        return Ordine([RigaOrdine(ProdottoRecord(nomeP, prezzoP), quantitaP)], ClienteRecord(nomeC, mailC, categoriaC))

    def processa_prossimo_ordine(self):
        #questo metodo legge il prossimo ordine in coda e lo gestisce
        if not self._ordini_da_processare:
            print("Non ci sono ordini in coda")
            return False, Ordine([], ClienteRecord("", "", ""))
        ordine = self._ordini_da_processare.popleft() #logica FIFO
        print(f"Sto processando l'ordine: {ordine.cliente}")
        print(ordine.riepilogo())

         for riga in ordine.righe:
             self._statistiche_prodotti[riga.prodotto.name] += riga.quantita

         #raggruppare gli ordini per categoria
        self._ordini_per_categoria[ordine.cliente.categoria].append(ordine)

        #archiviamo l'ordine
        self._ordini_processati.append(ordine)
        print("Ordine correttamente processato")
        return True, ordine



    def processa_tutti_ordini(self):
        #processa tutti gli ordini attualmente presenti in coda
        print(f"Processando {len(self._ordini_da_processare)} ordini")
        ordini=[]
        while self._ordini_da_processare:
            _, ordine = self.processa_prossimo_ordine
            ordini.append(ordine)
        print("Tutti gli ordini sono stati processati")
        return ordini

    def get_statistiche_prodotti(self, top_n: int=5, quantita):
        #questo metodo restituisce info su quante unità sono state vendute di un certo prodotto
        valori = []
        for prodotto, quantità in self._statistiche_prodotti.most_common(top_n):
            valori.append((prodotto, quantita))


    def get_distribuzione_categoria(self):
        valori = []
        for cat in self._ordini_per_categoria.keys():
            ordini = self._ordini_per_categoria[cat]
            totale_fatturato = sum(ordini.totale_lordo(0.22) for o in ordini)
            valori.append((cat, totale_fatturato))
        return valori


    def get_riepilogo(self):
        #stampa info di massimo
        sommario = ""
        sommario +="\n"" +""=" *60
        sommario += f"Ordini correttamente gestiti: {len(self._ordini_processati)}"
        sommario +=f"ordini in coda: {len(self._ordini_da_processare)}"

        sommario += ("Prodotti più venduti:")
        for prod, quantita in self.statistiche_prodotti():
            sommario += f"{prod}: {quantita}"
        sommario += f"Fatturato per categoria"
        for cat, fatturato in self.get_distribuzione_categoria():
            sommario += f"{cat}: {fatturato}"
        sommario += "\n" + "=" * 60
        return sommario


def test_modulo():
    sistema = GestoreOrdini()

    ordini = [
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1)], ClienteRecord("Mario Rossi", "mario@gmail.com", "Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Ipad", 600.0), 2)], ClienteRecord("Jhonny Bravo", "jhonny@gmail.com", "Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Mouse", 20.0), 3)], ClienteRecord("Asia Princigalli", "asia@gmail.com", "Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Televisore", 500.0), 2)], ClienteRecord("Chiara Raimondetto", "mario@gmail.com", "Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Iphone", 1600.0), 1)], ClienteRecord("Tania Giraudo", "mario@gmail.com", "Gold"))
    ]
    for o in ordini:
        sistema.add_ordine(o)
    sistema.processa_tutti_ordini()
    sistema.stampa_riepilogo()
if __name__ == "__main__":
    test_modulo()