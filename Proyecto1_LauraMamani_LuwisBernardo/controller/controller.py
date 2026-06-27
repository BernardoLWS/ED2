class DiccionarioController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def insertar(self):
        es = self.vista.entry_es.get()
        en = self.vista.entry_en.get()
        self.modelo.insertar(es, en)
        self.vista.mostrar_mensaje(f"Insertado: {es} -> {en}")

    def buscar(self):
        es = self.vista.entry_es.get()
        traduccion = self.modelo.buscar(es)
        if traduccion:
            self.vista.mostrar_mensaje(f"{es} -> {traduccion}")
        else:
            self.vista.mostrar_mensaje(f"{es} no encontrado")

    def listar(self):
        lista = self.modelo.inorden()
        texto = "\n".join([f"{es} -> {en}" for es, en in lista])
        self.vista.mostrar_mensaje(texto)
