import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def dd_role(self):
        self._view.popola_dropdown_ruolo(self._model._role)


    def handle_crea_grafo(self, e):
        self._view.btn_classifica.disabled = False
        print(self._view.dd_ruolo.value)
        self._model.build_graph(self._view.dd_ruolo.value)

        self._view.list_risultato.controls.clear()
        self._view.list_risultato.controls.append(ft.Text(f'Nodi: {self._model.num_nodes()} | archi: {self._model.num_edges()}'))

        self._view.update()



    def handle_classifica(self, e):
        pass