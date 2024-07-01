import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):
        self._listColor = self._model.getColori()
        for colore in self._listColor:
            self._view._ddcolor.options.append(ft.dropdown.Option(key=colore, text=str(colore)))  # da pulire la formattazione
        self._view.update_page()


    def handle_graph(self, e):
        # connessione = self._model.buildGrafo(str(self._view._ddyear.value), self._view._ddcolor.value)
        # numArchi = self._model.getNumEdges()
        # numNodi = self._model.getNumNodes()
        # self._view.txtOut2.clean()
        # self._view.txtOut2.controls.append(ft.Text(f"Numero di vertici: {numNodi} Numero di archi: {numArchi}"))
        # for arco in connessione:
        #     self._view.txtOut2.controls.append(ft.Text(f"Arco da {arco[0].Product_number} a {arco[1].Product_number}"))
        # self._view.update_page()
        u, v, w = self._model.buildGrafo(str(self._view._ddyear.value), self._view._ddcolor.value)
        numArchi = self._model.getNumEdges()
        numNodi = self._model.getNumNodes()
        self._view.txtOut2.clean()
        self._view.txtOut2.controls.append(ft.Text(f"Numero di vertici: {numNodi} Numero di archi: {numArchi}"))
        for i in range(u):
            self._view.txtOut2.controls.append(ft.Text(f"Arco da {u[i].Product_number} a {v[i].Product_number}, peso={w[i]}"))
        self._view.update_page()



    def fillDDProduct(self):
        pass


    def handle_search(self, e):
            pass
