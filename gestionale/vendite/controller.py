import flet as ft

from gestionale.vendite.GestoreOrdini import GestoreOrdini


class Controller:
    def __init__(self, view):
        self._view = v
        self._model = GestoreOrdini
    def add_ordine(self, e):
        #Prodotto
        nomePstr = self._view.txtInNomeP.value
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
        mail = self._view.txtInMail.value
        categoria = self._view.txtInCategoria.value

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
    def gestisci_ordine(self, e):
        pass

    def gestisci_all_ordini(self, e):
        pass

    def stampa_sommario(self, e):
        pass
