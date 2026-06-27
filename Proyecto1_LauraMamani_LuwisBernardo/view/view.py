import tkinter as tk

class DiccionarioView:
    def __init__(self, ventana, controlador=None):
        self.ventana = ventana
        self.controlador = controlador
        ventana.title("Diccionario Bilingüe")

        self.entry_es = tk.Entry(ventana)
        self.entry_en = tk.Entry(ventana)
        self.entry_es.pack()
        self.entry_en.pack()

        tk.Button(ventana, text="Insertar", command=self._on_insertar).pack()
        tk.Button(ventana, text="Buscar", command=self._on_buscar).pack()
        tk.Button(ventana, text="Listar", command=self._on_listar).pack()

        self.texto = tk.Text(ventana, height=10, width=40)
        self.texto.pack()

    def set_controlador(self, controlador):
        self.controlador = controlador

    def _on_insertar(self):
        if self.controlador:
            self.controlador.insertar()

    def _on_buscar(self):
        if self.controlador:
            self.controlador.buscar()

    def _on_listar(self):
        if self.controlador:
            self.controlador.listar()

    def mostrar_mensaje(self, mensaje):
        self.texto.delete("1.0", tk.END)
        self.texto.insert(tk.END, mensaje)