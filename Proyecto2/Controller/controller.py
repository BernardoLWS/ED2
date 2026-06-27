import tkinter as tk

class controller:
    def __init__(self, vista, modelo):
        self.model = modelo
        self.view = vista

        self.view.btn_agregar_usuario.config(command=self.agregar_usuario)
        self.view.btn_agregar_amigo.config(command=self.agregar_amigo)
        self.view.btn_grafo.config(command=self.dibujar_grafo)
        self.view.listbox_usuarios.bind("<<ListboxSelect>>", self.mostrar_amigos)

    def agregar_usuario(self):
        nombre = self.view.entry_nombre.get().strip()
        self.model.agregar_usuario(nombre)
        self.view.mostrar_usuarios(self.model.usuarios.keys())
        self.view.entry_nombre.delete(0, tk.END)

    def agregar_amigo(self):
        seleccion = self.view.listbox_usuarios.curselection()
        if seleccion:
            usuario = self.view.listbox_usuarios.get(seleccion[0])
            amigo = self.view.entry_nombre.get().strip()
            self.model.agregar_amigo(usuario, amigo)
            self.view.mostrar_amigos(self.model.get_amigos(usuario))
            self.view.entry_nombre.delete(0, tk.END)

    def mostrar_amigos(self, event):
        seleccion = self.view.listbox_usuarios.curselection()
        if seleccion:
            usuario = self.view.listbox_usuarios.get(seleccion[0])
            amigos = self.model.get_amigos(usuario)
            self.view.mostrar_amigos(amigos)
    
    def dibujar_grafo(self):
          self.view.mostrar_grafo()