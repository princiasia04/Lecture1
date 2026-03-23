import flet as ft

from gestionale.vendite.GestoreOrdini import GestoreOrdini


class Controller:
    def __init__(self, view):
        self._view = v
        self._model = GestoreOrdini
    def add_ordine(self, e):
        #Prodotto
        nomePstr = self._view.txtInNomeP.value
        if nomePstr == "":
            self._view.lvOut.controls.append(ft.Text("Attennzione, il campo nome prodotto è vuoto", color="red"))
            self._view.update_page()
            return
        try:
            prezzo =float(self._view.txtInPrezzo.value)
        except ValueError:
            self._view.lvOut.controls.append(ft.Text("Attenzione il prezzo deve essere un numero", color="red"))
            self._view.update_page()
            return
        try:
            quantita = int(self._view.txtInQuantita.value)
        except ValueError:
            self._view.lvOut.controls.append(ft.Text("Attenzione il prezzo deve essere un numero", color="red"))
            self._view.update_page()
            return

        #Cliente
        nomeC = self._view.txtInNomeC.value
        if nomeC == "":
            self._view.lvOut.controls.append(ft.Text("Attennzione, il campo nome cliente è vuoto", color="red"))
            self._view.update_page()
            return
        mail = self._view.txtInMail.value
        if mail == "":
            self._view.lvOut.controls.append(ft.Text("Attennzione, il campo mail è vuoto", color="red"))
            self._view.update_page()
            return
        categoria = self._view.txtInCategoria.value
        if categoria == "":
            self._view.lvOut.controls.append(ft.Text("Attennzione, il campo categoria è vuoto", color="red"))
            self._view.update_page()
            return

        ordine = self._model.crea_ordine(nomePstr, prezzo, quantita, nomeC, mail, categoria)
        self._model.add_ordine(ordine)

        self._view.txtInNomeP.value = ""
        self._view.txtInPrezzo.value = ""
        self._view.txtInQuantita.value = ""
        self._view.txtInNomeC.value = ""
        self._view.txtInMail.value = ""
        self._view.txtInCategoria.value = ""
        self._view.lvOut.controls.append(ft.Text("Ordine correttamente inserito", color="green"))
        self._view.lvOut.controls.append(ft.Text(ordine.riepilogo()))
        self._view.update_page()
    def gestisci_ordine(self, e):
        self._view.lvOut.controls.clear()
        res, ordine = self._model.processa_prossimo_ordine()

        if res:
            self._view.lvOut.controls.append(ft.Text("Ordine processato con successo", color="green"))
            self._view.lvOut.controls.append(ft.Text(ordine.riepilogo()))
            self._view.update_page()
        else:
            self._view.lvOut.controls.append(ft.Text("Non ci sono ordini in coda", color="blue"))
            self._view.update_page()

    def gestisci_all_ordini(self, e):
        self._view.lvOut.controls.clear()
        ordini = self._model.processa_tutti_ordini()
        if not ordini:
            self._view.lvOut.controls.append(ft.Text("Non ci sono ordini in coda", color="blue"))
            self._view.update_page()
        else:
            self._view.lvOut.controls.append(ft.Text(f"Ho processato correttamente {len(ordini)} ordini", color="green"))
            for o in ordini:
                self._view.lvOut.controls.append(ft.Text("\n"))
                self._view.lvOut.controls.append(ft.Text(o.riepilogo()))
            self._view.update_page()

    def stampa_sommario(self, e):
        self._view.lvOut.controls.clear()
        self._view.lvOut.controls.append(ft.Text("Di seguito il sommario dello stato del business", color = "orange"))
        self._view.lvOut.controls.append(ft.Text(self._model.get_riepilogo()))
        self._view.update_page()
